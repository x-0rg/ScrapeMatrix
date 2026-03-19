"""Embeddings and retrieval for RAG system."""
import logging
import json
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class RetrievalResult:
    """Result from retrieval system."""
    
    chunk_id: str
    document_id: str
    content: str
    similarity_score: float
    document_title: Optional[str] = None


class SimpleEmbedder:
    """Simple embedding system using TF-IDF-like scoring.
    
    This is a lightweight alternative to transformer-based embeddings.
    For production, consider using sentence-transformers or OpenAI embeddings.
    """
    
    def __init__(self):
        """Initialize simple embedder."""
        self.vocabulary: Dict[str, int] = {}
        self.vocab_size = 0
    
    def build_vocabulary(self, texts: List[str], max_vocab: int = 5000) -> None:
        """Build vocabulary from texts.
        
        Args:
            texts: List of text documents
            max_vocab: Maximum vocabulary size
        """
        word_freq = {}
        
        for text in texts:
            words = self._tokenize(text)
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
        
        # Sort by frequency and limit vocabulary
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        sorted_words = sorted_words[:max_vocab]
        
        self.vocabulary = {word: idx for idx, (word, _) in enumerate(sorted_words)}
        self.vocab_size = len(self.vocabulary)
        
        logger.info(f"Built vocabulary with {self.vocab_size} words")
    
    def embed(self, text: str) -> List[float]:
        """Create embedding for text.
        
        Args:
            text: Text to embed
            
        Returns:
            Embedding vector
        """
        if not self.vocabulary:
            raise ValueError("Vocabulary not built. Call build_vocabulary first.")
        
        # Create TF vector
        words = self._tokenize(text)
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        # Build embedding
        embedding = [0.0] * self.vocab_size
        total_words = len(words)
        
        for word, count in word_count.items():
            if word in self.vocabulary:
                idx = self.vocabulary[word]
                # TF (term frequency)
                embedding[idx] = count / (total_words + 1e-6)
        
        # Normalize
        norm = np.sqrt(sum(x**2 for x in embedding) + 1e-6)
        embedding = [x / norm for x in embedding]
        
        return embedding
    
    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization.
        
        Args:
            text: Text to tokenize
            
        Returns:
            List of tokens
        """
        # Convert to lowercase and split
        words = text.lower().split()
        
        # Remove punctuation and filter
        cleaned = []
        for word in words:
            # Remove common punctuation
            word = word.strip('.,!?;:()[]{}"\'-')
            if len(word) > 2 and word.isalnum():  # Keep alphanumeric, len > 2
                cleaned.append(word)
        
        return cleaned
    
    def similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """Calculate cosine similarity between two vectors.
        
        Args:
            vec1: First vector
            vec2: Second vector
            
        Returns:
            Similarity score between 0 and 1
        """
        if len(vec1) != len(vec2):
            return 0.0
        
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        # Vectors are already normalized, so similarity is just dot product
        return max(0.0, min(1.0, dot_product))


class RetrieverSystem:
    """System for retrieving relevant chunks based on queries."""
    
    def __init__(self, embedder: Optional[SimpleEmbedder] = None):
        """Initialize retriever system.
        
        Args:
            embedder: Embedder to use (default: SimpleEmbedder)
        """
        self.embedder = embedder or SimpleEmbedder()
        self.chunk_embeddings: Dict[str, List[float]] = {}
        self.chunks: Dict[str, Dict] = {}  # chunk_id -> chunk data
    
    def index_chunks(self, chunks: List) -> None:
        """Index chunks for retrieval.
        
        Args:
            chunks: List of Chunk objects to index
        """
        # First, build vocabulary from all chunks
        texts = [chunk.content for chunk in chunks]
        self.embedder.build_vocabulary(texts)
        
        # Then embed each chunk
        for chunk in chunks:
            embedding = self.embedder.embed(chunk.content)
            self.chunk_embeddings[chunk.id] = embedding
            self.chunks[chunk.id] = {
                'id': chunk.id,
                'document_id': chunk.document_id,
                'content': chunk.content,
                'chunk_index': chunk.chunk_index,
            }
        
        logger.info(f"Indexed {len(chunks)} chunks")
    
    def retrieve(self, query: str, top_k: int = 5, min_score: float = 0.1) -> List[RetrievalResult]:
        """Retrieve relevant chunks for query.
        
        Args:
            query: Query string
            top_k: Number of top results to return
            min_score: Minimum similarity score threshold
            
        Returns:
            List of RetrievalResult objects
        """
        if not self.chunks:
            logger.warning("No chunks indexed for retrieval")
            return []
        
        # Embed query
        query_embedding = self.embedder.embed(query)
        
        # Score all chunks
        scores = []
        for chunk_id, chunk_embedding in self.chunk_embeddings.items():
            similarity = self.embedder.similarity(query_embedding, chunk_embedding)
            if similarity >= min_score:
                chunk_data = self.chunks[chunk_id]
                scores.append((similarity, chunk_id, chunk_data))
        
        # Sort by score and return top-k
        scores.sort(key=lambda x: x[0], reverse=True)
        results = []
        
        for similarity, chunk_id, chunk_data in scores[:top_k]:
            result = RetrievalResult(
                chunk_id=chunk_id,
                document_id=chunk_data['document_id'],
                content=chunk_data['content'],
                similarity_score=similarity,
            )
            results.append(result)
        
        return results
    
    def save_embeddings(self, path: Path) -> None:
        """Save embeddings to file.
        
        Args:
            path: Path to save embeddings
        """
        try:
            data = {
                'chunk_embeddings': {
                    k: v for k, v in self.chunk_embeddings.items()
                },
                'chunks': self.chunks,
            }
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w') as f:
                json.dump(data, f)
            logger.info(f"Saved embeddings to {path}")
        except Exception as e:
            logger.error(f"Error saving embeddings: {e}")
    
    def load_embeddings(self, path: Path) -> None:
        """Load embeddings from file.
        
        Args:
            path: Path to load embeddings from
        """
        try:
            if not path.exists():
                logger.warning(f"Embeddings file not found: {path}")
                return
            
            with open(path, 'r') as f:
                data = json.load(f)
            
            self.chunk_embeddings = data.get('chunk_embeddings', {})
            self.chunks = data.get('chunks', {})
            
            logger.info(f"Loaded {len(self.chunks)} chunk embeddings from {path}")
        except Exception as e:
            logger.error(f"Error loading embeddings: {e}")
    
    def clear(self) -> None:
        """Clear all indexed chunks."""
        self.chunk_embeddings.clear()
        self.chunks.clear()
        logger.info("Cleared all indexed chunks")
