plugin "terraform" {
  enabled = true
  preset  = "recommended"
}

rule "terraform_unused_declarations" {
  enabled = false
}

rule "terraform_typed_variables" {
  enabled = false
}
