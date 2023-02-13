# CIS_NUMBER: 1.2
# TITLE: Ensure that Multi-Factor Authentication is 'Enabled' for All Non-Service Accounts (Manual)

"""
This code defines four functions: check_mfa, check_non_service_accounts, get_iam_policies, and list_non_mfa_accounts. The check_mfa function checks if an account has multi-factor authentication enabled by calling the get method of the UserAccountsClient class from the iam library. The check_non_service_accounts function returns a list of non-service accounts in a policy by iterating through the bindings in the policy and checking if each member is a service account or not. The get_iam_policies function returns the IAM policies for a project, folder, or organization by calling the get_iam_policy method of the Client class from the resource_manager library with the appropriate resource type. The `list_non_mfa
"""

from google.cloud import resource_manager
from google.cloud import iam

def check_mfa(account):
    """Check if an account has multi-factor authentication enabled."""
    try:
        client = iam.UserAccountsClient()
        user = client.get(account)
        return user.second_factor_required
    except:
        return False

def check_non_service_accounts(policy):
    """Return a list of non-service accounts in a policy."""
    non_service_accounts = []
    for binding in policy.bindings:
        members = binding.members
        role = binding.role
        for member in members:
            if "serviceAccount" not in member and "google.com" not in member:
                non_service_accounts.append((member, role))
    return non_service_accounts

def get_iam_policies(project_id=None, folder_id=None, organization_id=None):
    """Return the IAM policies for a project, folder, or organization."""
    policies = []
    if project_id:
        client = resource_manager.Client()
        policy = client.get_iam_policy(project_id)
        policies.append(policy)
    if folder_id:
        client = resource_manager.Client()
        policy = client.get_iam_policy(folder_id, "folder")
        policies.append(policy)
    if organization_id:
        client = resource_manager.Client()
        policy = client.get_iam_policy(organization_id, "organization")
        policies.append(policy)
    return policies

def list_non_mfa_accounts(project_id=None, folder_id=None, organization_id=None):
    """Return a list of non-service accounts without multi-factor authentication enabled."""
    policies = get_iam_policies(project_id, folder_id, organization_id)
    non_mfa_accounts = []
    for policy in policies:
        non_service_accounts = check_non_service_accounts(policy)
        for account, role in non_service_accounts:
            if not check_mfa(account):
                non_mfa_accounts.append((account, role))
    return non_mfa_accounts