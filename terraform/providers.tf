terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.65.0"
    }
  }
}

provider "aws" {
  shared_credentials_files = ["$HOME/.aws/credentials"]
  region                   = var.region
}