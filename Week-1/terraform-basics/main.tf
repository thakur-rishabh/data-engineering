terraform {
  required_version = ">= 1.0"
  # can be gcs/s3/local
  backend "local" {}
  required_providers {
        google = {
            source = "hashicorp/google"
        }
    }
}

provider "google" {
    project = var.project
    region = var.region
    # credential = file(var.credential)
}

# data lake resource
resource "google_storage_bucket" "data-lake-bucket" {
    name            = "${local.data_lake_bucket}_${var.project}"
    location        = var.region
    storage_class   = var.storage_class

    uniform_bucket_level_access = true

    versioning {
        enabled = true
    }

    lifecycle_rule {
        action {
            type = "Delete"
        }
        condition {
            # days
            age = 30
        }
    }
    force_destroy = true
}

# data warehouse
resource "google_bigquery_dataset" "dataset" {
    dataset_id      = var.BQ_DATASET
    project         = var.project
    location        = var.region
}
