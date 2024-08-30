#!/bin/bash
set -ex

sudo yum update -y

#docker
sudo amazon-linux-extras install docker
sudo yum install docker -y
sudo service docker start
sudo chmod 666 /var/run/docker.sock
sudo usermod -a -G docker ec2-user

#docker compose
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-composedocker-compose version

#git
sudo yum install git -y

#Install cloud watch for collecting logs
sudo dpkg -r amazon-ssm-agent
sudo yum install amazon-cloudwatch-agent

#pulling github repo and executing app using docker-compose
git clone https://github.com/talitz/flask-app.git
cd flask-app
sudo docker-compose up --build
