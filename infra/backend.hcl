# infra/backend.hcl
bucket       = "tfstate-calculadora-jalopezg4"
key          = "calculadora/terraform.tfstate"
region       = "us-east-1"
use_lockfile = true