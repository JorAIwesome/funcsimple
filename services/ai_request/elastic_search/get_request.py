import os
from elasticsearch import Elasticsearch

def get_related_context(query, field, index, size = 3):
    es_client = Elasticsearch(
        os.getenv("ES_HOST"),
        api_key=os.getenv("ES_API_KEY")
    )
    
    es_query = {
        "retriever": {
            "standard": {
                "query": {
                    "multi_match": {
                        "query": query,
                        "fields": [
                            field
                        ]
                    }
                }
            }
        },
        "size": size
    }

    result = es_client.search(index=index, body=es_query)
    return result["hits"]["hits"]
