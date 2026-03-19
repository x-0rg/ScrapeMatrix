"""RAG Chat Engine for question answering."""
import logging
from typing import List, Optional, Dict, Any
from dataclasses import dataclass, field
from datetime import datetime

from .retriever import RetrieverSystem, RetrievalResult
from .knowledge_base import KnowledgeBase

logger = logging.getLogger(__name__)


@dataclass
class Message:
    """Chat message."""
    
    role: str  # "user" or "assistant"
    content: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    sources: List[str] = field(default_factory=list)  # Document IDs used
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            'role': self.role,
            'content': self.content,
            'timestamp': self.timestamp,
            'sources': self.sources,
        }


class RAGChatEngine:
    """RAG-based chat engine for question answering."""
    
    def __init__(self, knowledge_base: KnowledgeBase, retriever: RetrieverSystem):
        """Initialize RAG chat engine.
        
        Args:
            knowledge_base: Knowledge base instance
            retriever: Retriever system instance
        """
        self.kb = knowledge_base
        self.retriever = retriever
        self.conversation_history: List[Message] = []
    
    def answer_query(self, query: str, top_k: int = 5, use_history: bool = True) -> Dict[str, Any]:
        """Answer a user query using RAG.
        
        Args:
            query: User query
            top_k: Number of relevant chunks to retrieve
            use_history: Whether to use conversation history
            
        Returns:
            Dictionary with answer and metadata
        """
        # Add user message to history
        user_msg = Message(role="user", content=query)
        self.conversation_history.append(user_msg)
        
        # Retrieve relevant chunks
        retrieved = self.retriever.retrieve(query, top_k=top_k)
        
        if not retrieved:
            answer = (
                "I couldn't find relevant information in the knowledge base "
                "to answer your question. Please upload documents related to your query."
            )
            sources = []
        else:
            # Build context from retrieved chunks
            context = self._build_context(retrieved)
            
            # Generate answer
            answer = self._generate_answer(query, context, retrieved)
            
            # Collect sources
            sources = list(set(r.document_id for r in retrieved))
        
        # Add assistant message to history
        assistant_msg = Message(
            role="assistant",
            content=answer,
            sources=sources,
        )
        self.conversation_history.append(assistant_msg)
        
        return {
            'query': query,
            'answer': answer,
            'sources': sources,
            'retrieved_chunks': [
                {
                    'content': r.content[:200] + '...' if len(r.content) > 200 else r.content,
                    'similarity': r.similarity_score,
                    'document_id': r.document_id,
                }
                for r in retrieved
            ],
        }
    
    def _build_context(self, retrieved: List[RetrievalResult]) -> str:
        """Build context from retrieved chunks.
        
        Args:
            retrieved: List of retrieved chunks
            
        Returns:
            Context string
        """
        context_parts = []
        
        for i, result in enumerate(retrieved, 1):
            doc = self.kb.get_document(result.document_id)
            doc_title = doc.title if doc else "Unknown"
            
            context_parts.append(
                f"[Source {i}: {doc_title}]\n{result.content}"
            )
        
        return "\n\n---\n\n".join(context_parts)
    
    def _generate_answer(self, query: str, context: str, retrieved: List[RetrievalResult]) -> str:
        """Generate answer based on query and context.
        
        Args:
            query: User query
            context: Retrieved context
            retrieved: Retrieved chunks
            
        Returns:
            Generated answer
        """
        # In a production system, you would use an LLM here (OpenAI, Cohere, etc.)
        # For now, we'll use a simple template-based approach
        
        if not retrieved:
            return "No relevant information found."
        
        # Simple answer generation based on retrieved content
        answer_template = (
            "Based on the provided documents:\n\n"
            "{context}\n\n"
            "---\n\n"
            "Key findings:\n"
            "- The most relevant information comes from {top_sources}\n"
            "- Relevance score: {relevance:.0%}\n\n"
            "Note: This answer is generated based on document retrieval. "
            "For complex queries, please review the source documents directly."
        )
        
        # Get top sources
        top_sources = ", ".join([
            self.kb.get_document(r.document_id).title
            for r in retrieved[:3]
            if self.kb.get_document(r.document_id)
        ])
        
        avg_relevance = sum(r.similarity_score for r in retrieved) / len(retrieved)
        
        answer = answer_template.format(
            context=context[:1000] + "..." if len(context) > 1000 else context,
            top_sources=top_sources or "retrieved documents",
            relevance=avg_relevance,
        )
        
        return answer
    
    def get_conversation_history(self) -> List[Message]:
        """Get conversation history.
        
        Returns:
            List of messages
        """
        return self.conversation_history
    
    def clear_history(self) -> None:
        """Clear conversation history."""
        self.conversation_history.clear()
        logger.info("Cleared conversation history")
    
    def export_conversation(self) -> List[Dict[str, Any]]:
        """Export conversation as list of dictionaries.
        
        Returns:
            List of message dictionaries
        """
        return [msg.to_dict() for msg in self.conversation_history]
    
    def get_kb_stats(self) -> Dict[str, Any]:
        """Get knowledge base statistics.
        
        Returns:
            Statistics dictionary
        """
        stats = self.kb.get_statistics()
        stats['conversation_length'] = len(self.conversation_history)
        return stats
