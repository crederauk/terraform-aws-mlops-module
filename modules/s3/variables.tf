##########################################
# Naming and Tagging
##########################################

variable "resource_naming_prefix" {
  description = "Naming prefix to be attached to every resource created by this module."
  type        = string
}
variable "tags" {
  description = "Tags applied to your resources"
  default     = {}
  type        = map(string)
}


