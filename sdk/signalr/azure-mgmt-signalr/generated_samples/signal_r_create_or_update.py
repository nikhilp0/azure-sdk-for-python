# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.signalr import SignalRManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-signalr
# USAGE
    python signal_r_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SignalRManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.signal_r.begin_create_or_update(
        resource_group_name="myResourceGroup",
        resource_name="mySignalRService",
        parameters={
            "identity": {"type": "SystemAssigned"},
            "kind": "SignalR",
            "location": "eastus",
            "properties": {
                "cors": {"allowedOrigins": ["https://foo.com", "https://bar.com"]},
                "disableAadAuth": False,
                "disableLocalAuth": False,
                "features": [
                    {"flag": "ServiceMode", "properties": {}, "value": "Serverless"},
                    {"flag": "EnableConnectivityLogs", "properties": {}, "value": "True"},
                    {"flag": "EnableMessagingLogs", "properties": {}, "value": "False"},
                    {"flag": "EnableLiveTrace", "properties": {}, "value": "False"},
                ],
                "liveTraceConfiguration": {
                    "categories": [{"enabled": "true", "name": "ConnectivityLogs"}],
                    "enabled": "false",
                },
                "networkACLs": {
                    "defaultAction": "Deny",
                    "privateEndpoints": [
                        {"allow": ["ServerConnection"], "name": "mysignalrservice.1fa229cd-bf3f-47f0-8c49-afb36723997e"}
                    ],
                    "publicNetwork": {"allow": ["ClientConnection"]},
                },
                "publicNetworkAccess": "Enabled",
                "serverless": {"connectionTimeoutInSeconds": 5},
                "tls": {"clientCertEnabled": False},
                "upstream": {
                    "templates": [
                        {
                            "auth": {"managedIdentity": {"resource": "api://example"}, "type": "ManagedIdentity"},
                            "categoryPattern": "*",
                            "eventPattern": "connect,disconnect",
                            "hubPattern": "*",
                            "urlTemplate": "https://example.com/chat/api/connect",
                        }
                    ]
                },
            },
            "sku": {"capacity": 1, "name": "Premium_P1", "tier": "Premium"},
            "tags": {"key1": "value1"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/signalr/resource-manager/Microsoft.SignalRService/stable/2023-02-01/examples/SignalR_CreateOrUpdate.json
if __name__ == "__main__":
    main()
