"""Knowledge base management for RAG system."""
import json
import logging
from pathlib import Path
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field, asdict
from datetime import datetime

logger = logging.getLogger(__name__)


@dataclass
class Document:
    """Represents a document in the knowledge base."""
    
    id: str
    title: str
    content: str
    file_type: str  # pdf, txt, docx, etc.
    file_path: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert document to dictionary."""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Document":
        """Create document from dictionary."""
        return cls(**data)


@dataclass
class Chunk:
    """Represents a chunk of text from a document."""
    
    id: str
    document_id: str
    content: str
    chunk_index: int
    start_char: int
    end_char: int
    embedding: Optional[List[float]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert chunk to dictionary."""
        data = asdict(self)
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Chunk":
        """Create chunk from dictionary."""
        return cls(**data)


class KnowledgeBase:
    """Manages documents and chunks for RAG system."""
    
    def __init__(self, kb_dir: Path = None):
        """Initialize knowledge base.
        
        Args:
            kb_dir: Directory to store knowledge base files
        """
        self.kb_dir = kb_dir or Path.home() / ".scrapematrix" / "knowledge_base"
        self.kb_dir.mkdir(parents=True, exist_ok=True)
        
        self.documents_file = self.kb_dir / "documents.json"
        self.chunks_file = self.kb_dir / "chunks.json"
        
        self.documents: Dict[str, Document] = {}
        self.chunks: Dict[str, List[Chunk]] = {}
        
        self._load_from_disk()
    
    def _load_from_disk(self) -> None:
        """Load documents and chunks from disk."""
        try:
            if self.documents_file.exists():
                with open(self.documents_file, 'r') as f:
                    docs_data = json.load(f)
                    self.documents = {
                        doc_id: Document.from_dict(doc)
                        for doc_id, doc in docs_data.items()
                    }
                logger.info(f"Loaded {len(self.documents)} documents")
            
            if self.chunks_file.exists():
                with open(self.chunks_file, 'r') as f:
                    chunks_data = json.load(f)
                    self.chunks = {
                        doc_id: [Chunk.from_dict(c) for c in chunks]
                        for doc_id, chunks in chunks_data.items()
                    }
                logger.info(f"Loaded chunks for {len(self.chunks)} documents")
        except Exception as e:
            logger.error(f"Error loading knowledge base: {e}")
    
    def save_to_disk(self) -> None:
        """Save documents and chunks to disk."""
        try:
            # Save documents
            docs_data = {
                doc_id: doc.to_dict()
                for doc_id, doc in self.documents.items()
            }
            with open(self.documents_file, 'w') as f:
                json.dump(docs_data, f, indent=2)
            
            # Save chunks
            chunks_data = {
                doc_id: [chunk.to_dict() for chunk in chunks]
                for doc_id, chunks in self.chunks.items()
            }
            with open(self.chunks_file, 'w') as f:
                json.dump(chunks_data, f, indent=2)
            
            logger.info("Knowledge base saved to disk")
        except Exception as e:
            logger.error(f"Error saving knowledge base: {e}")
    
    def add_document(self, document: Document) -> None:
        """Add document to knowledge base.
        
        Args:
            document: Document to add
        """
        self.documents[document.id] = document
        logger.info(f"Added document: {document.title} ({document.id})")
    
    def remove_document(self, doc_id: str) -> bool:
        """Remove document from knowledge base.
        
        Args:
            doc_id: ID of document to remove
            
        Returns:
            True if document was removed, False if not found
        """
        if doc_id in self.documents:
            del self.documents[doc_id]
            if doc_id in self.chunks:
                del self.chunks[doc_id]
            logger.info(f"Removed document: {doc_id}")
            return True
        return False
    
    def add_chunks(self, doc_id: str, chunks: List[Chunk]) -> None:
        """Add chunks for a document.
        
        Args:
            doc_id: Document ID
            chunks: List of chunks to add
        """
        self.chunks[doc_id] = chunks
        logger.info(f"Added {len(chunks)} chunks for document {doc_id}")
    
    def get_document(self, doc_id: str) -> Optional[Document]:
        """Get document by ID.
        
        Args:
            doc_id: Document ID
            
        Returns:
            Document or None if not found
        """
        return self.documents.get(doc_id)
    
    def get_chunks(self, doc_id: str) -> List[Chunk]:
        """Get all chunks for a document.
        
        Args:
            doc_id: Document ID
            
        Returns:
            List of chunks
        """
        return self.chunks.get(doc_id, [])
    
    def get_all_documents(self) -> List[Document]:
        """Get all documents in knowledge base.
        
        Returns:
            List of documents
        """
        return list(self.documents.values())
    
    def get_all_chunks(self) -> List[Chunk]:
        """Get all chunks in knowledge base.
        
        Returns:
            List of all chunks
        """
        all_chunks = []
        for chunks in self.chunks.values():
            all_chunks.extend(chunks)
        return all_chunks
    
    def search_by_title(self, title_query: str) -> List[Document]:
        """Search documents by title.
        
        Args:
            title_query: Query string
            
        Returns:
            List of matching documents
        """
        query_lower = title_query.lower()
        return [
            doc for doc in self.documents.values()
            if query_lower in doc.title.lower()
        ]
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get knowledge base statistics.
        
        Returns:
            Statistics dictionary
        """
        total_docs = len(self.documents)
        total_chunks = sum(len(chunks) for chunks in self.chunks.values())
        total_chars = sum(
            len(doc.content) for doc in self.documents.values()
        )
        
        return {
            "total_documents": total_docs,
            "total_chunks": total_chunks,
            "total_characters": total_chars,
            "avg_doc_size": total_chars // total_docs if total_docs > 0 else 0,
        }
