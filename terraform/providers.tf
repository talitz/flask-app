terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.65.0"
    }
  }
  backend "s3" {
    bucket = "terraform-state-flask-app-infra"
    key    = "terraform.tfstate"
    region = "us-east-2"
  }
}

data "terraform_remote_state" "network" {
  backend = "s3"
  config = {
    bucket = "terraform-state-flask-app-infra"
    key    = "terraform.tfstate"
    region = "us-east-2"
  }
}

provider "aws" {
  shared_credentials_files = ["$HOME/.aws/credentials"]
  region                   = var.region
}