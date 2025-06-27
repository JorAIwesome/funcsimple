from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from azure.identity import DefaultAzureCredential
from services.get_secret import get_secret
import os

credential = DefaultAzureCredential()

blob_service_client = BlobServiceClient(account_url=os.getenv('BLOB_ACCOUNT_URL'), credential=credential)

def get_blob_url(container_name, blob_name):
    # Maak een BlobClient voor het specifieke bestand
    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )
    
    sas_token = generate_blob_sas(
        account_name=blob_service_client.account_name,
        container_name=container_name,
        blob_name=blob_name,
        account_key=get_secret("BLOB-ACCOUNT-KEY"),
        permission=BlobSasPermissions(read=True),
        expiry=datetime.now() + timedelta(hours=1)  # Token expiry time
    )
    
    # Construct de URL met SAS token
    blob_url = blob_client.url + "?" + sas_token

    return blob_url

def saveblob(file_name,data,container_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    
    lease_duration = 60  # Lease duration in seconds, use -1 for infinite lease
    lease = blob_client.acquire_lease(lease_duration=lease_duration)

    blob_client.upload_blob(data=data, overwrite=True, lease=lease)
    
    sas_token = generate_blob_sas(
        account_name=blob_service_client.account_name,
        container_name=container_name,
        blob_name=file_name,
        account_key=get_secret("BLOB-ACCOUNT-KEY"),
        permission=BlobSasPermissions(read=True),
        expiry=datetime.now() + timedelta(hours=1)  # Token expiry time
    )
    
    return f"{blob_client.url}?{sas_token}"
