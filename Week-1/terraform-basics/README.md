# Terraform

1. Setup gcloud project (refer [gcloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects))
2. Create IAM service user with below rples:
    -   Viewer
    -   Storage Object Admin
    -   Storage Admin
    -   BigQuery Admin
3. Install terraform:
    ```
    brew tap hashicorp/tap
    brew install hashicorp/tap/terraform
    ```
4. File structure:
    -   main.tf
    -   variable.tf
    -   .terraform_version

5. Execution steps:
    -   `terraform init`
    -   `terraform plan`
    -   `terraform apply`
    -   `terraform destroy`
