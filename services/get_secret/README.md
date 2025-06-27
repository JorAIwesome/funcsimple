# Key Vault Secret Retrieval

This directory contains the code to manage connections to Azure Key Vault and retrieve secrets. The connection configuration depends on the environment mode (development or production).

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)

## Introduction

This script retrieves secrets from Azure Key Vault using the `azure-keyvault-secrets` package. It uses `DefaultAzureCredential` for authentication, suitable for both managed identity and service principal authentication.

## Usage

The script retrieves secrets from Azure Key Vault as follows:

- Uses `DefaultAzureCredential` for authentication.
- Connects to the Key Vault using the provided vault URL.
- Retrieves the secret specified by `secret_name`.

## Environment Variables

The script relies on the following environment variable:

- `VAULT_URL`: The URL of the Azure Key Vault.
  - Example: `https://kv-eridanos-ai-d1.vault.azure.net/`

## Dependencies

Ensure the following packages are installed:

- `azure-keyvault-secrets`: For interacting with Azure Key Vault.
- `azure-identity`: For authenticating with Azure Key Vault.
- `azure-functions`: For handling Azure Functions (if used in an Azure Function app).

Install the dependencies using:
```bash
pip install azure-keyvault-secrets azure-identity azure-functions
```

Or install all the requirements from the requirements.txt file using:
```bash
pip install -r requirements.txt
```

## Troubleshooting

- **Authentication Issues**:
  - Ensure the correct environment variable `VAULT_URL` is set.
  - Verify that the credentials used are correct and have the necessary permissions.

- **Secret Retrieval Errors**:
  - Check if the secret name is correct.
  - Ensure the secret exists in the Key Vault and is not disabled or expired.

- **Connection Errors**:
  - Check the Key Vault URL.
  - Ensure network connectivity and firewall settings allow access to Azure Key Vault.

For further assistance, refer to the official [Azure Key Vault documentation](https://docs.microsoft.com/en-us/azure/key-vault/).