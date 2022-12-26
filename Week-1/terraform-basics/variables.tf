locals {
  data_lake_bucket = "de_data_lake"
}

variable "project" {
  description = "My gcp project id"
  default = "data-engineer-312-372622"
  type = string
}

variable "region" {
  description = "Region nearest to me"
  default = "us-central1"
  type = string
}

variable "storage_class" {
  default = "STANDARD"
}

variable "BQ_DATASET" {
  description = "Bigquery Dataset that raw data will be writter to"
  default = "trips_data_all"
  type = string
}