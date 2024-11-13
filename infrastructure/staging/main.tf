provider "google" {
    project = var.project
    region = var.region
}

provider "google-beta" {
  project = var.project
    region = var.region
}

terraform {
  required_version = "~> 1"
  required_providers {
    google = {
      version = "~> 6.11"
      source = "google/google"
    }
    google-beta = {
      version = "~> 3.83.0"
      source = "google/google-beta"
    }
  }
}

variable "project" {
  type = string
}

variable "region" {
  type = string
}


module "weather_app_staging" {
  source = "../_shared"
  app_id = "weather"
  env = "staging"
}