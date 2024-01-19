package test

import (
	"testing"
	"github.com/gruntwork-io/terratest/modules/terraform"
)

func TestTerraform(t *testing.T) {
	terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{
		// Set the path to the Terraform code that will be tested.
		TerraformDir: "../examples/", 
	})

	// Clean up resources 
	defer terraform.Destroy(t, terraformOptions)

	// Fail the test if there are any errors.
	terraform.InitAndApply(t, terraformOptions)

}
