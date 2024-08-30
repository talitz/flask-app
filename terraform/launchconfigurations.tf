data "aws_iam_policy_document" "ec2" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}

resource "aws_iam_policy" "session-manager" {
  description = "session-manager"
  name        = "session-manager"
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Action" : "ec2:*",
        "Effect" : "Allow",
        "Resource" : "*"
      },
      {
        "Effect" : "Allow",
        "Action" : "elasticloadbalancing:*",
        "Resource" : "*"
      },
      {
        "Effect" : "Allow",
        "Action" : "cloudwatch:*",
        "Resource" : "*"
      },
      {
        "Effect" : "Allow",
        "Action" : "autoscaling:*",
        "Resource" : "*"
      },
      {
        "Effect" : "Allow",
        "Action" : "iam:CreateServiceLinkedRole",
        "Resource" : "*",
        "Condition" : {
          "StringEquals" : {
            "iam:AWSServiceName" : [
              "autoscaling.amazonaws.com",
              "ec2scheduled.amazonaws.com",
              "elasticloadbalancing.amazonaws.com",
              "spot.amazonaws.com",
              "spotfleet.amazonaws.com",
              "transitgateway.amazonaws.com"
            ]
          }
        }
      }
    ]
  })
}

resource "aws_iam_role" "session-manager" {
  assume_role_policy = data.aws_iam_policy_document.ec2.json
  name               = "session-manager"
  tags = {
    Name = "session-manager"
  }
}

resource "aws_iam_instance_profile" "session-manager" {
  name = "session-manager"
  role = aws_iam_role.session-manager.name
}

resource "aws_instance" "bastion" {
  ami                         = lookup(var.amis, var.region)
  instance_type               = var.instance_type
  key_name                    = aws_key_pair.terraform-lab.key_name
  iam_instance_profile        = aws_iam_instance_profile.session-manager.id
  associate_public_ip_address = true
  security_groups             = [aws_security_group.ec2.id]
  subnet_id                   = aws_subnet.public-subnet-1.id
  tags = {
    Name = "Bastion"
  }
}

resource "aws_launch_configuration" "ec2" {
  name                        = "${var.ec2_instance_name}-instances-lc"
  image_id                    = lookup(var.amis, var.region)
  instance_type               = var.instance_type
  security_groups             = [aws_security_group.ec2.id]
  key_name                    = aws_key_pair.terraform-lab.key_name
  iam_instance_profile        = aws_iam_instance_profile.session-manager.id
  associate_public_ip_address = false
  user_data                   = <<-EOL
  #!/bin/bash -xe
  sudo yum update -y
  sudo yum -y install docker
  sudo service docker start
  sudo usermod -a -G docker ec2-user
  sudo chmod 666 /var/run/docker.sock
  docker pull nginx
  docker tag nginx my-nginx
  docker run --rm --name nginx-server -d -p 80:80 -t my-nginx
  EOL
  depends_on                  = [aws_nat_gateway.terraform-lab-ngw]
}