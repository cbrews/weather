terraform {
  required_version = "~> 1.0.0"
}

variable "project" {}
variable "region" {}

provider "google" {
    project = var.project
    region = var.region
}

module "weather_app_production" {
  source = "../_shared"
  app_id = "weather"
  env = "production"
}