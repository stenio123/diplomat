"""
!pip install openai
import os
import openai

def GPT_Completion(texts):
## Call the API key under your account (in a secure way)
  openai.api_key = "YOUR-KEY"
  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt =  texts,
    temperature = 0.6,
    top_p = 1,
    max_tokens = 3640,
    frequency_penalty = 0,
    presence_penalty = 0
  )
  return print(response.choices[0].text)

# 1.1
query_prefix = "Use the GCP python client library and create python code that "
query = query_prefix + "retrieves all user and service accounts, and validates that their email address is from the same domain as the organization domain."
GPT_Completion(query)
"""

from google.cloud import iam

# Create a client
iam_client = iam.Client()

# Get the organization
org = iam_client.get_organization('id')

# Get all users and service accounts
for account in org.list_accounts():
    if account.primary_email.endswith(org.domain):
        print('Email address {} is valid for domain {}'.format(
            account.primary_email, org.domain))
    else:
        print('Email address {} is not valid for domain {}'.format(
            account.primary_email, org.domain))


"""
# 1.2

query="Use the GCP python client library and create python code that retrieves all user accounts, and checks if mfa is enabled or disabled"
GPT_Completion(query)
"""
import google.cloud.iam_v1

client = google.cloud.iam_v1.IAMClient()

for account in client.list_accounts():

    print('Account: {}'.format(account.name))

    if account.mfa_enabled:

        print('MFA enabled')

    else:

        print('MFA disabled')

"""
# 1.3

query="Use the GCP python client library and create python code that lists all user accounts with the \"roles/resourcemanager.organizationAdmin\" role and checks that they have Security Key Enforcement enabled"
GPT_Completion(query)
"""

import google.cloud.resourcemanager
import google.cloud.iam
from googleapiclient.discovery import build

# TODO(developer): # The GCP project id.
project_id = "YOUR_PROJECT_ID"
# The name of the role to check.
role_name = "roles/resourcemanager.organizationAdmin"
# Get the Cloud Resource Manager service.
service = build("cloudresourcemanager", "v1")
# Get the Cloud IAM service.
iam_service = build("iam", "v1")
# List all projects in the org.
projects_response = (
    service.projects().list(parent="organizations/" + project_id).execute()
)
for project in projects_response["projects"]:
    # List all IAM policies for the project.
    project_policies_response = (
        iam_service.projects().policies().list(resource=project["name"]).execute()
    )
    for policy in project_policies_response["policies"]:
        # Check if the role is present in any of the IAM policies.
        for binding in policy["bindings"]:
            if binding["role"] == role_name:
                # The role is present in at least one IAM policy.
                # Check if Security Key Enforcement is enabled.
                if "security_key_enforcement" not in binding["constraints"]:
                    print(
                        "Security Key Enforcement is not enabled for role "
                        + role_name
                        + " in project "
                        + project["name"]
                    )