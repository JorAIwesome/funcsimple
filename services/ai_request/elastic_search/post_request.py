import os
from elasticsearch import Elasticsearch, helpers
import PyPDF2

def add_document_context(index_name, folder, extension = ".pdf"):
    # Connect to Elasticsearch
    client = Elasticsearch(
        os.getenv('ES_HOST'),
        api_key=os.getenv("ES_API_KEY"),
    )

    docs = []

    # Loop over all PDFs in the specified folder
    for filename in os.listdir(folder):
        if filename.lower().endswith(extension):
            file_path = os.path.join(folder, filename)
            text = ""
            try:
                with open(file_path, "rb") as pdf_file:
                    reader = PyPDF2.PdfReader(pdf_file)
                    # Extract text from each page
                    for page in reader.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n"
                # Append document with extracted text (and optionally the filename)
                docs.append({
                    "text": text,
                    "filename": filename  # Optional: include filename for reference
                })
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # Bulk index the documents into Elasticsearch
    helpers.bulk(client, docs, index=index_name)
