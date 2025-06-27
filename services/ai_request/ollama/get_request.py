import requests, logging

def get_nomic_embedding(sentence):
    response = requests.post("http://localhost:11434/api/embeddings", json={
        "model": "nomic-embed-text",
        "prompt": sentence
    })
    logging.info("Processed response...")
    return (response.json())["embedding"]