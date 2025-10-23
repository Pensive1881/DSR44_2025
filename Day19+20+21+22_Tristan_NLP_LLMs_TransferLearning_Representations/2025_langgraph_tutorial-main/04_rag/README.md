

Download the document:

```bash
wget -O document.pdf https://people.engr.tamu.edu/guni/csce625/slides/AI.pdf
mkdir documents
mv document.pdf documents/
```

Install PostgreSQL and create a database:

```bash
cd postgres
docker compose up -d
```

Update `.env` :

```bash
POSTGRES_CONNECTION_STRING=postgresql://postgres:example@localhost:7770/postgres
LANGCHAIN_EMBEDDING_MODEL=ollama:qwen3-embedding:0.6b
LANGCHAIN_EMBEDDING_MODEL_DIMENSIONS=1024
LANGCHAIN_CHAT_MODEL=ollama:qwen3:4b
```

You might want to pull the models locally with:

```bashollama pull qwen3
ollama pull qwen3-embedding:0.6b
```

Run the import script:

```bash
python importdocumentworkflow.py
```

Inspect the database by navigating to `http://localhost:7771` in your browser.