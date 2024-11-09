variable "app_id" {
    type = string
}

variable "env" {
    type = string
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

      volume_mounts {
        name       = "cloudsql"
        mount_path = "/cloudsql"
      }
    }
    volumes {
      name = "cloudsql"
      cloud_sql_instance {
        instances = [google_sql_database_instance.db_instance.connection_name]
      }
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

# resource "google_sql_database_instance" "db_instance" {
#   name             = "${local.prefix}-db-instance"
#   region           = local.region
#   database_version = "POSTGRES_15"

#   settings {
#     tier = "db-f1-micro"
#   }

#   deletion_protection  = false
# }

# resource "google_sql_database" "db" {
#   name     = "${local.prefix}-db"
#   instance = google_sql_database_instance.db_instance.name
# }

# resource "google_sql_user" "iam_group_user" {
#   name     = var.app_id
#   instance = google_sql_database_instance.db_instance.name
#   password = ""
# }