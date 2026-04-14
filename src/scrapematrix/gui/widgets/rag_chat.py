"""RAG Chat Widget for PyQt6 GUI."""
import logging
from pathlib import Path
from typing import Optional

from PyQt6.QtCore import Qt, QThread, pyqtSignal, QSize
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel,
    QFileDialog, QMessageBox, QScrollArea, QFrame, QProgressBar,
    QListWidget, QListWidgetItem, QSplitter, QTabWidget
)

from scrapematrix.rag.knowledge_base import KnowledgeBase
from scrapematrix.rag.document_processor import DocumentProcessor
from scrapematrix.rag.retriever import RetrieverSystem
from scrapematrix.rag.chat_engine import RAGChatEngine

logger = logging.getLogger(__name__)


class QueryWorkerThread(QThread):
    """Worker thread for processing queries."""
    
    query_processed = pyqtSignal(dict)  # Result from answer_query
    error_occurred = pyqtSignal(str)
    
    def __init__(self, engine: RAGChatEngine, query: str):
        """Initialize worker thread.
        
        Args:
            engine: RAG chat engine
            query: User query
        """
        super().__init__()
        self.engine = engine
        self.query = query
    
    def run(self):
        """Run query processing."""
        try:
            result = self.engine.answer_query(self.query)
            self.query_processed.emit(result)
        except Exception as e:
            logger.exception("Error processing query")
            self.error_occurred.emit(str(e))


class DocumentUploadWorkerThread(QThread):
    """Worker thread for uploading documents."""
    
    progress_updated = pyqtSignal(str)
    upload_complete = pyqtSignal(str)  # Document title
    error_occurred = pyqtSignal(str)
    
    def __init__(self, kb: KnowledgeBase, retriever: RetrieverSystem, 
                 file_path: Path, title: Optional[str] = None):
        """Initialize upload worker thread.
        
        Args:
            kb: Knowledge base
            retriever: Retriever system
            file_path: Path to file to upload
            title: Optional document title
        """
        super().__init__()
        self.kb = kb
        self.retriever = retriever
        self.file_path = file_path
        self.title = title
    
    def run(self):
        """Run document upload."""
        try:
            self.progress_updated.emit(f"Processing {self.file_path.name}...")
            
            # Process document
            processor = DocumentProcessor()
            doc, chunks = processor.process_file(self.file_path, self.title)
            
            self.progress_updated.emit(f"Adding {len(chunks)} chunks to knowledge base...")
            
            # Add to knowledge base
            self.kb.add_document(doc)
            self.kb.add_chunks(doc.id, chunks)
            self.kb.save_to_disk()
            
            self.progress_updated.emit(f"Indexing chunks...")
            
            # Index chunks
            self.retriever.index_chunks(chunks)
            
            self.progress_updated.emit(f"Done!")
            self.upload_complete.emit(doc.title)
            
        except Exception as e:
            logger.exception(f"Error uploading document {self.file_path}")
            self.error_occurred.emit(f"Error uploading document: {str(e)}")


class RAGChatWidget(QWidget):
    """RAG Chat Widget for the application."""
    
    def __init__(self):
        """Initialize RAG chat widget."""
        super().__init__()
        
        # Initialize RAG system
        self.kb = KnowledgeBase()
        self.retriever = RetrieverSystem()
        self.engine = RAGChatEngine(self.kb, self.retriever)
        
        # Index existing documents
        self._index_existing_documents()
        
        # UI setup
        self.init_ui()
        
        self.query_thread: Optional[QueryWorkerThread] = None
        self.upload_thread: Optional[DocumentUploadWorkerThread] = None
    
    def _index_existing_documents(self) -> None:
        """Index existing documents in knowledge base."""
        try:
            all_chunks = self.kb.get_all_chunks()
            if all_chunks:
                self.retriever.index_chunks(all_chunks)
                logger.info(f"Indexed {len(all_chunks)} existing chunks")
        except Exception as e:
            logger.error(f"Error indexing existing documents: {e}")
    
    def init_ui(self) -> None:
        """Initialize user interface."""
        main_layout = QVBoxLayout()
        
        # Create tabs
        self.tabs = QTabWidget()
        
        # Chat tab
        self.tabs.addTab(self._create_chat_tab(), "Chat")
        
        # Documents tab
        self.tabs.addTab(self._create_documents_tab(), "Documents")
        
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)
    
    def _create_chat_tab(self) -> QWidget:
        """Create chat tab."""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Knowledge Base Chat")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Chat display area with scroll
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("Courier", 9))
        scroll_area.setWidget(self.chat_display)
        
        layout.addWidget(QLabel("Chat History:"))
        layout.addWidget(scroll_area, 1)
        
        # Query input area
        query_label = QLabel("Your Question:")
        layout.addWidget(query_label)
        
        self.query_input = QTextEdit()
        self.query_input.setMaximumHeight(80)
        self.query_input.setPlaceholderText("Ask a question about the documents...")
        layout.addWidget(self.query_input)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        self.submit_button = QPushButton("Ask Question")
        self.submit_button.clicked.connect(self.submit_query)
        self.submit_button.setStyleSheet(
            "QPushButton { background-color: #10B981; color: white; "
            "padding: 8px; border-radius: 4px; font-weight: bold; }"
        )
        button_layout.addWidget(self.submit_button)
        
        self.clear_button = QPushButton("Clear Chat")
        self.clear_button.clicked.connect(self.clear_chat)
        button_layout.addWidget(self.clear_button)
        
        layout.addLayout(button_layout)
        
        # Status
        self.status_label = QLabel("Ready")
        self.status_label.setStyleSheet("color: #666; font-size: 11px;")
        layout.addWidget(self.status_label)
        
        widget.setLayout(layout)
        return widget
    
    def _create_documents_tab(self) -> QWidget:
        """Create documents management tab."""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Document Management")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Upload button
        upload_layout = QHBoxLayout()
        
        self.upload_button = QPushButton("Upload Document")
        self.upload_button.clicked.connect(self.upload_document)
        self.upload_button.setStyleSheet(
            "QPushButton { background-color: #3B82F6; color: white; "
            "padding: 8px; border-radius: 4px; font-weight: bold; }"
        )
        upload_layout.addWidget(self.upload_button)
        
        upload_layout.addStretch()
        layout.addLayout(upload_layout)
        
        # Progress bar
        self.upload_progress = QProgressBar()
        self.upload_progress.setVisible(False)
        layout.addWidget(self.upload_progress)
        
        self.upload_status = QLabel("")
        self.upload_status.setStyleSheet("color: #666; font-size: 11px;")
        layout.addWidget(self.upload_status)
        
        # Documents list
        layout.addWidget(QLabel("Documents in Knowledge Base:"))
        
        self.documents_list = QListWidget()
        self._refresh_documents_list()
        layout.addWidget(self.documents_list, 1)
        
        # Document actions
        actions_layout = QHBoxLayout()
        
        self.remove_button = QPushButton("Remove Selected")
        self.remove_button.clicked.connect(self.remove_document)
        self.remove_button.setStyleSheet(
            "QPushButton { background-color: #EF4444; color: white; "
            "padding: 6px; border-radius: 4px; }"
        )
        actions_layout.addWidget(self.remove_button)
        
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self._refresh_documents_list)
        actions_layout.addWidget(self.refresh_button)
        
        layout.addLayout(actions_layout)
        
        # Statistics
        layout.addWidget(QLabel("Knowledge Base Statistics:"))
        
        self.stats_display = QTextEdit()
        self.stats_display.setReadOnly(True)
        self.stats_display.setMaximumHeight(100)
        self._update_statistics()
        layout.addWidget(self.stats_display)
        
        widget.setLayout(layout)
        return widget
    
    def submit_query(self) -> None:
        """Submit a query to the RAG engine."""
        query = self.query_input.toPlainText().strip()
        
        if not query:
            QMessageBox.warning(self, "Input Error", "Please enter a question")
            return
        
        if not self.kb.get_all_documents():
            QMessageBox.warning(
                self,
                "Empty Knowledge Base",
                "Please upload documents first before asking questions."
            )
            return
        
        # Disable input during processing
        self.submit_button.setEnabled(False)
        self.query_input.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.status_label.setText("Processing query...")
        
        # Run query in worker thread
        self.query_thread = QueryWorkerThread(self.engine, query)
        self.query_thread.query_processed.connect(self.on_query_processed)
        self.query_thread.error_occurred.connect(self.on_query_error)
        self.query_thread.start()
    
    def on_query_processed(self, result: dict) -> None:
        """Handle processed query result.
        
        Args:
            result: Result dictionary from answer_query
        """
        # Display result
        self._append_to_chat(f"Q: {result['query']}\n")
        self._append_to_chat(f"A: {result['answer']}\n")
        
        if result['sources']:
            sources_text = ", ".join([
                self.kb.get_document(doc_id).title
                for doc_id in result['sources']
                if self.kb.get_document(doc_id)
            ])
            self._append_to_chat(f"Sources: {sources_text}\n")
        
        self._append_to_chat("\n" + "="*60 + "\n\n")
        
        # Re-enable input
        self.submit_button.setEnabled(True)
        self.query_input.setEnabled(True)
        self.progress_bar.setVisible(False)
        self.query_input.clear()
        self.status_label.setText("Ready")
    
    def on_query_error(self, error: str) -> None:
        """Handle query error.
        
        Args:
            error: Error message
        """
        QMessageBox.critical(self, "Query Error", f"Error: {error}")
        
        self.submit_button.setEnabled(True)
        self.query_input.setEnabled(True)
        self.progress_bar.setVisible(False)
        self.status_label.setText("Error occurred")
    
    def upload_document(self) -> None:
        """Upload a document."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Document",
            "",
            "All Files (*);;Text Files (*.txt);;PDF Files (*.pdf);;Word Files (*.docx);;Markdown Files (*.md)"
        )
        
        if not file_path:
            return
        
        file_path = Path(file_path)
        
        # Optional: get title from user
        title = file_path.stem
        
        # Disable button during upload
        self.upload_button.setEnabled(False)
        self.upload_progress.setVisible(True)
        
        # Run upload in worker thread
        self.upload_thread = DocumentUploadWorkerThread(
            self.kb, self.retriever, file_path, title
        )
        self.upload_thread.progress_updated.connect(self._on_upload_progress)
        self.upload_thread.upload_complete.connect(self._on_upload_complete)
        self.upload_thread.error_occurred.connect(self._on_upload_error)
        self.upload_thread.start()
    
    def _on_upload_progress(self, message: str) -> None:
        """Handle upload progress update.
        
        Args:
            message: Progress message
        """
        self.upload_status.setText(message)
    
    def _on_upload_complete(self, title: str) -> None:
        """Handle upload completion.
        
        Args:
            title: Document title
        """
        QMessageBox.information(
            self,
            "Upload Complete",
            f"Document '{title}' has been uploaded and indexed."
        )
        
        self.upload_button.setEnabled(True)
        self.upload_progress.setVisible(False)
        self.upload_status.setText("Ready")
        
        self._refresh_documents_list()
        self._update_statistics()
    
    def _on_upload_error(self, error: str) -> None:
        """Handle upload error.
        
        Args:
            error: Error message
        """
        QMessageBox.critical(self, "Upload Error", error)
        
        self.upload_button.setEnabled(True)
        self.upload_progress.setVisible(False)
        self.upload_status.setText("Error occurred")
    
    def remove_document(self) -> None:
        """Remove selected document."""
        current_item = self.documents_list.currentItem()
        
        if not current_item:
            QMessageBox.warning(self, "No Selection", "Please select a document to remove")
            return
        
        doc_id = current_item.data(Qt.ItemDataRole.UserRole)
        doc = self.kb.get_document(doc_id)
        
        if not doc:
            return
        
        confirm = QMessageBox.question(
            self,
            "Confirm Removal",
            f"Remove document '{doc.title}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.kb.remove_document(doc_id)
            self.kb.save_to_disk()
            self.retriever.clear()  # Clear and re-index
            self._index_existing_documents()
            self._refresh_documents_list()
            self._update_statistics()
            QMessageBox.information(self, "Success", "Document removed")
    
    def _refresh_documents_list(self) -> None:
        """Refresh the documents list display."""
        self.documents_list.clear()
        
        documents = self.kb.get_all_documents()
        
        if not documents:
            self.documents_list.addItem("No documents uploaded yet")
            return
        
        for doc in documents:
            item = QListWidgetItem(f"{doc.title} ({doc.file_type})")
            item.setData(Qt.ItemDataRole.UserRole, doc.id)
            self.documents_list.addItem(item)
    
    def _update_statistics(self) -> None:
        """Update statistics display."""
        stats = self.engine.get_kb_stats()
        
        stats_text = (
            f"Documents: {stats['total_documents']}\n"
            f"Chunks: {stats['total_chunks']}\n"
            f"Total Characters: {stats['total_characters']:,}\n"
            f"Avg Doc Size: {stats['avg_doc_size']:,} chars"
        )
        
        self.stats_display.setText(stats_text)
    
    def _append_to_chat(self, text: str) -> None:
        """Append text to chat display.
        
        Args:
            text: Text to append
        """
        self.chat_display.append(text)
        # Scroll to bottom
        self.chat_display.verticalScrollBar().setValue(
            self.chat_display.verticalScrollBar().maximum()
        )
    
    def clear_chat(self) -> None:
        """Clear chat history."""
        confirm = QMessageBox.question(
            self,
            "Clear Chat",
            "Clear chat history?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if confirm == QMessageBox.StandardButton.Yes:
            self.chat_display.clear()
            self.engine.clear_history()
