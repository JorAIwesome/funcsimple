from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import azure.functions as func
import logging
import os

def get_secret(secret_name):
    credential = DefaultAzureCredential()
    
    client = SecretClient(vault_url=os.getenv('SECRETS_VAULT_URL'), credential=credential)
    
    try:
        secret = client.get_secret(secret_name)
        logging.info(secret)
        if secret.value is None:
            logging.error("Error: "+ secret_name + " secret is None")
            return func.HttpResponse('Error: secret is None.', status_code=500)
        else: 
            return secret.value

    except Exception as ex:
        logging.error(f"Failed to retrieve secret '{secret_name}' from Azure Key Vault: {ex}")
        return None
