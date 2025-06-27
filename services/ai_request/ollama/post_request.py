import requests, ollama
import os
import logging
from langchain.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.llms import ollama

def get_sql_answer(question: str) -> str:
    """
    Convert a natural language question into SQL and execute it on the database.
    Uses the latest Ollama LLM interface (ensure this package is current).
    """
    # Retrieve and validate the SQL connection string from environment variables.
    connection_string = os.environ.get("SQL_CONNECTION_STRING2")
    if not connection_string:
        msg = "SQL connection string is not configured properly."
        logging.error(msg)
        raise ValueError(msg)
    
    # Initialize the SQL database connection.
    db = SQLDatabase.from_uri(connection_string)

    # Initialize the local LLM using Ollama.
    llm = ollama.Ollama(temperature=0)
    
    # Create the SQLDatabaseChain: converts natural language into SQL and retrieves results.
    agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)

    return agent_executor.invoke(
        {
            "input": question
        }
    )

def generate_deepseek_completion(user_prompt, question):
    # Ollama's REST API endpoint for generating completions.
    url = "http://localhost:11434/api/generate"  # Adjust if needed.
    
    payload = {
        "model": "deepseek-v3",
        "messages": [
            {"role": "system", "content": user_prompt},
            {"role": "user", "content": question}
        ]
    }
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    
    data = response.json()
    # Assuming the response JSON follows a structure similar to:
    # {"choices": [{"message": {"content": "..."}}]}
    return data["choices"][0]["message"]["content"]

def generate_ollama_image_description(image_path):
    
    response = ollama.chat(
        model="llama3.2-vision",
        messages=[
            {
                "role": "user",
                "content": "Describe this image:",
                "images": [image_path]
            }
        ]
    )
    caption = response["message"]["content"].strip()
    return caption