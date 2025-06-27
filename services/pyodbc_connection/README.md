# PyODBC Connection

This directory contains the code to manage connections to a SQL database using pyODBC. The connection configuration depends on the environment mode (development or production).

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)

## Introduction

This script sets up a connection to a SQL database using the `pyodbc` package. It supports different credentials and connection strings based on the environment mode (development or production).

## Usage

The script connects to the SQL database as follows:

- **Development Mode**:
  - Uses hardcoded credentials for the local SQL Server instance.
  - The connection string is built using environment variables for database name, user ID, and password.

- **Production Mode**:
  - Retrieves database credentials from Azure Key Vault using the `get_secret` function.
  - The connection string is built using the secrets retrieved for the database name, user ID, and password.

## Environment Variables

The script relies on the following environment variables:

- `ENV_MODE`: Determines whether to use development or production credentials.
  - Set to `production` for production environment.
  - Set to any other value for development environment.
- `EMULATOR_DATABASE_NAME`: The name of the database for the emulator (development mode).
- `EMULATOR_DATABASE_UID`: The user ID for the database emulator (development mode).
- `EMULATOR_DATABASE_PWD`: The password for the database emulator (development mode).

## Dependencies

Ensure the following packages are installed:

- `pyodbc`: For connecting to SQL databases using ODBC.
- `azure-keyvault-secrets`: For retrieving secrets from Azure Key Vault.
- `azure-identity`: For authenticating with Azure Key Vault.

Install the dependencies using:
```bash
pip install pyodbc azure-keyvault-secrets azure-identity
```

Or install all the requirements from the requirements.txt file using:
```bash
pip install -r requirements.txt
```

## Troubleshooting

- **Authentication Issues**:
  - Ensure the correct environment variable `ENV_MODE` is set.
  - Verify that the secrets retrieved from Azure Key Vault are correct and have the necessary permissions.

- **Connection Errors**:
  - Check the connection string for any syntax errors.
  - Ensure the SQL Server instance is running and accessible.
  - Verify network connectivity and firewall settings.

- **Secret Retrieval Errors**:
  - Ensure the secret names are correct.
  - Verify the secrets exist in the Azure Key Vault and are not disabled or expired.

For further assistance, refer to the official [pyODBC documentation](https://github.com/mkleehammer/pyodbc) and [Azure Key Vault documentation](https://docs.microsoft.com/en-us/azure/key-vault/).