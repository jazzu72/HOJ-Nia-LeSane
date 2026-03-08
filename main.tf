terraform {
  backend "remote" {
    organization = "your-org"

    workspaces {
      name = "your-workspace"
    }
  }
}

resource "null_resource" "example" {
  triggers = {
    value = "example"
  }
}
