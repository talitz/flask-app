# Flask App Pipeline
This repository contains a Flask web application enhanced with database interaction, authentication, rate limiting, and integrated with a CI/CD pipeline using GitHub Actions.

### Features
- Database Integration: Uses SQLite for storing user data.
- Authentication: Basic HTTP authentication for protecting routes.
- Rate Limiting: Limits the number of requests to prevent abuse.
- CI/CD Pipeline: Integrated with GitHub Actions for continuous integration and deployment.

### Setup Instructions
Prerequisites
- Python 3.8 or higher
- Docker and Docker Compose
- Git

### Local Development

#### 1. Run the Application locally
Clone the repository:
```
git clone https://github.com/talitz/flask-app-prod-pipeline.git
cd flask-app-prod-pipeline
```

#### Create a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

#### Install dependencies:
```pip install -r requirements.txt``` 

#### Set up environment variables:
Copy the example environment file and adjust the variables as needed.

#### Run the application:
```python3 -m flask --app src/app run --port 5000 --debug```

The application will be available at http://127.0.0.1:5000.

#### 2. Local Development using Docker

To build the Docker image for the Flask application, navigate to the root directory of the project where the Dockerfile is located and run the following command:

```docker build -t flask-app:latest .```

This command will build a Docker image named flask-app based on the instructions in the Dockerfile.

Once the image is built, you can run the container using the following command:

```docker run -p 5001:5000 flask-app```

This command starts the container and maps port 5000 inside the container to port 5001 on your local machine.

You can access the Flask application by navigating to the following URL in your web browser: http://127.0.0.1:5001/

#### 3. Local Development using Docker Compose

Building can be done:
```docker-compose up --build```

Now, you can access the Flask application by navigating to the following URL in your web browser: http://localhost/

For spinning down all containers:
```docker-compose down```

#### 4. GitHub Actions Pipeline Automation

### AWS Infrastructure

The infrastructure is deployed using terraform:
- VPC with two public subnets and two private subnets in two different availability zones for high-availability.
- Internet Gateway for internet traffic.
- NAT Gateway to the private subnets, so the private subnets can connect to the internet.
- Autoscaling group and launch templates to the EC2 Instances.
- Security groups and route tables to enable traffic between subnets, NAT, and Internet Gateways.
- Application Load Balancer for the EC2 auto scaling group.
- Bastion EC2 instance to SSH into the EC2 instances running in private subnets.

![alt text](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*p0PB24XPldiNMcx4nTzFEQ.png)

#### 1. Local Terraform Development

##### Setup Instructions
Prerequisites
- Terraform v1.5.7
- AWS Account

Configure the AWS Credentials: 
```
export TF_VAR_aws_key=""                           
export TF_VAR_aws_secret=""
```

Then, run the following commands:
```
terraform init                           
terraform plan
terraform apply
```

#### 2. GitHub Actions Pipeline Automation