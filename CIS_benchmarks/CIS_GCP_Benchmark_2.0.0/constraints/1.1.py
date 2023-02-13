# CIS_NUMBER: 1.1
# TITLE: Ensure that Corporate Login Credentials are Used (Manual)

"""
This code uses the re module to perform regular expression searches on the email addresses in the policy bindings. The regular expression r"@[\w.-]+google.com" matches any email addresses in the Google domain, while the expression r"serviceAccount:" matches any Google-owned service accounts. If a member does not match either of these patterns, the code considers it unauthorized and prints a message indicating so.

Note that you need to replace "your_organization_id", "your_project_id", and "your_folder_id" with the actual values for your
"""
from google.cloud import iam
from google.cloud.iam import Policy
from google.cloud import resource_manager
import re

# The organization_id, project_id and folder_id
organization_id = "your_organization_id"
project_id = "your_project_id"
folder_id = "your_folder_id"

# Instantiates a client for the IAM API
iam_client = iam.PolicyManagerClient()

# Get the organization's IAM policy
organization_policy = iam_client.get_org_policy(request={"resource": f"organizations/{organization_id}"})

# Print the bindings in the organization policy
print("Organization Policy:")
for binding in organization_policy.bindings:
    print(f"Role: {binding.role}")
    for member in binding.members:
        if not re.search(r"@[\w.-]+google.com", member) and not re.search(r"serviceAccount:", member):
            print(f"Unauthorized Member: {member}")

# Get the project's IAM policy
project_policy = iam_client.get_policy(request={"resource": f"projects/{project_id}"})

# Print the bindings in the project policy
print("Project Policy:")
for binding in project_policy.bindings:
    print(f"Role: {binding.role}")
    for member in binding.members:
        if not re.search(r"@[\w.-]+google.com", member) and not re.search(r"serviceAccount:", member):
            print(f"Unauthorized Member: {member}")

# Instantiates a client for the Cloud Resource Manager API
resource_manager_client = resource_manager.Client()

# Get the folder's IAM policy
folder_policy = iam_client.get_folder_policy(request={"resource": f"folders/{folder_id}"})

# Print the bindings in the folder policy
print("Folder Policy:")
for binding in folder_policy.bindings:
    print(f"Role: {binding.role}")
    for member in binding.members:
        if not re.search(r"@[\w.-]+google.com", member) and not re.search(r"serviceAccount:", member):
            print(f"Unauthorized Member: {member}")