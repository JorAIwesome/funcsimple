# Blob Connection

This directory contains the code to manage connections to Azure Blob Storage. The connection configuration depends on the environment mode (development or production).

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)

## Introduction

This script sets up a connection to Azure Blob Storage using the `azure-storage-blob` package. It supports different credentials based on the environment mode (development or production).

## Usage

The script connects to Azure Blob Storage as follows:

- **Development Mode**:
  - Uses the azurite emulator..
  - Example credentials and URL are provided in the script.

- **Production Mode**:
  - Uses `DefaultAzureCredential` for managed identity or service principal authentication.


## Environment Variables

The script relies on the following environment variable:

- `ENV_MODE`: Determines whether to use development or production credentials. 
  - Set to `production` for production environment.
  - Set to any other value for development environment.

## Dependencies

Ensure the following packages are installed:

- `azure-storage-blob`: For interacting with Azure Blob Storage.
- `azure-identity`: For authenticating in production environment.

Install the dependencies using:
```bash
pip install azure-storage-blob azure-identity
```

Or install all the requirements from requirements.txt file using:
```bash
pip install -r requirements.txt
```

## Troubleshooting

- **Authentication Issues**:
  - Ensure the correct environment variable `ENV_MODE` is set.
  - Verify that the credentials used are correct and have the necessary permissions.
  
- **Connection Errors**:
  - Check the account URL.
  - Ensure network connectivity and firewall settings allow access to Azure Blob Storage.

For further assistance, refer to the official [Azure Storage Blob documentation](https://docs.microsoft.com/en-us/azure/storage/blobs/).