# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.devcenter import DevCenterMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-devcenter
# USAGE
    python project_environment_types_patch.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DevCenterMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="0ac520ee-14c0-480f-b6c9-0a90c58ffff",
    )

    response = client.project_environment_types.update(
        resource_group_name="rg1",
        project_name="ContosoProj",
        environment_type_name="DevTest",
        body={
            "identity": {
                "type": "UserAssigned",
                "userAssignedIdentities": {
                    "/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/identityGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/testidentity1": {}
                },
            },
            "properties": {
                "deploymentTargetId": "/subscriptions/00000000-0000-0000-0000-000000000000",
                "status": "Enabled",
                "userRoleAssignments": {
                    "e45e3m7c-176e-416a-b466-0c5ec8298f8a": {"roles": {"4cbf0b6c-e750-441c-98a7-10da8387e4d6": {}}}
                },
            },
            "tags": {"CostCenter": "RnD"},
        },
    )
    print(response)


# x-ms-original-file: specification/devcenter/resource-manager/Microsoft.DevCenter/stable/2023-04-01/examples/ProjectEnvironmentTypes_Patch.json
if __name__ == "__main__":
    main()
