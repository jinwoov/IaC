terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.5.0" // no more than 3.5
    }
  }
}

provider "aws" {
  region = "us-central"
}

resource "aws_budgets_budget" "budget-demo" {
  name              = "monthly-budget"
  budget_type       = "COST"
  limit_amount      = "10.0"
  limit_unit        = "USD"
  time_unit         = "monthly"
  time_period_start = "2021-02-05_00:01"
}
// init first - terraform init
// terraform fmt - change the format to check the lint error
// look at the code block and see if the the code seems good.