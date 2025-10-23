import os
from langgraph.store.postgres import PostgresStore
from langgraph.store.postgres import AsyncPostgresStore

def create_store():

    # Get the connection string.
    db_connection_string = os.environ["POSTGRES_CONNECTION_STRING"]
    if not db_connection_string:
        raise ValueError("POSTGRES_CONNECTION_STRING environment variable is not set.")

    # Get the embedding model.
    embedding_model = os.environ["LANGCHAIN_EMBEDDING_MODEL"]
    if not embedding_model:
        raise ValueError("LANGCHAIN_EMBEDDING_MODEL environment variable is not set.")

    # Get the embedding model dimensions.
    embedding_model_dimensions = int(os.environ["LANGCHAIN_EMBEDDING_MODEL_DIMENSIONS"])
    if not embedding_model_dimensions:
        raise ValueError("LANGCHAIN_EMBEDDING_MODEL_DIMENSIONS environment variable is not set.")
    
    # Create and return the store.
    store = PostgresStore.from_conn_string(
        db_connection_string,
        index={
            "embed": embedding_model,
            "dims": embedding_model_dimensions,
        }
    )

    return store


def create_async_store():

    # Get the connection string.
    db_connection_string = os.environ["POSTGRES_CONNECTION_STRING"]
    if not db_connection_string:
        raise ValueError("POSTGRES_CONNECTION_STRING environment variable is not set.")

    # Get the embedding model.
    embedding_model = os.environ["LANGCHAIN_EMBEDDING_MODEL"]
    if not embedding_model:
        raise ValueError("LANGCHAIN_EMBEDDING_MODEL environment variable is not set.")

    # Get the embedding model dimensions.
    embedding_model_dimensions = int(os.environ["LANGCHAIN_EMBEDDING_MODEL_DIMENSIONS"])
    if not embedding_model_dimensions:
        raise ValueError("LANGCHAIN_EMBEDDING_MODEL_DIMENSIONS environment variable is not set.")
    
    # Create and return the store.
    store = AsyncPostgresStore.from_conn_string(
        db_connection_string,
        index={
            "embed": embedding_model,
            "dims": embedding_model_dimensions,
        }
    )
    return store