# ScrapeMatrix
ScrapeMatrix - Industrial-Grade Stock Analysis Desktop App

### RAG Architecture
```
rag_project/
├── data/                      # Raw documents (PDFs, text files)
├── vector_store/              # Local Vector DB storage (e.g., Chroma DB files)
├── src/                       # Main source code
│   ├── ingestion/             # Ingestion pipeline scripts
│   │   ├── loaders.py         # Functions to read PDFs/URLs
│   │   ├── chunkers.py        # Text splitting logic
│   │   └── embedder.py        # Pushing vectors to DB
│   ├── retrieval/             # Query pipeline scripts
│   │   ├── retriever.py       # Vector DB similarity search logic
│   │   └── generator.py       # LLM prompt construction and API calls
│   ├── api/                   # FastAPI endpoints
│   │   ├── routes.py          # /chat, /upload_doc endpoints
│   │   └── schemas.py         # Pydantic models for request/response
│   ├── config.py              # Environment variables and app settings
│   └── utils.py               # Helper functions (logging, error handling)
├── app.py                     # Streamlit frontend (if applicable)
├── main.py                    # FastAPI application entry point
├── requirements.txt           # Python dependencies
└── .env                       # API keys (OpenAI, Pinecone, etc.)

```
