variable "app_id" {
    type = string
}

variable "env" {
    type = string
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

locals {
  prefix = "${var.app_id}-${var.env}"
  region = "us-central1"
}

resource "google_cloud_run_v2_service" "api" {
  name = "${local.prefix}-api"
  location = local.region
  deletion_protection = false
  ingress = "INGRESS_TRAFFIC_ALL"
    
  template {
    containers {
      image = "us-docker.pkg.dev/cloudrun/container/hello:latest"
    }
  }
  client     = "terraform"
}

resource "google_cloud_run_service_iam_binding" "api_binding" {
    location  = google_cloud_run_v2_service.api.location
    service = google_cloud_run_v2_service.api.name
    role = "roles/run.invoker"
    members = [
        "allUsers"
    ]
}