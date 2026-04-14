"""
ScrapeMatrix Test Configuration - Iteration 1

This file provides pytest fixtures and configuration for all tests.
- Phase 1: Testing & Stability
- Created: Iteration 1

Usage:
    pytest                          # Run all tests
    pytest tests/unit              # Run unit tests only
    pytest --cov=src               # Run with coverage
    pytest -m unit                 # Run tests marked as unit
"""

import sys
import os
import pytest
from pathlib import Path
from unittest.mock import Mock, MagicMock, patch
import logging

# Add src to path for imports
PROJECT_ROOT = Path(__file__).parent
SRC_PATH = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_PATH))

# Configure logging for tests
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)8s] %(name)s: %(message)s'
)


# ============================================================================
# FIXTURES - Available to all tests
# ============================================================================

@pytest.fixture(scope="session")
def test_data_dir():
    """Provide path to test data directory."""
    data_dir = PROJECT_ROOT / "tests" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


@pytest.fixture
def temp_dir(tmp_path):
    """Provide temporary directory for test files."""
    return tmp_path


@pytest.fixture
def sample_text_data():
    """Sample text data for testing document processing."""
    return """
    The Python programming language is known for its simplicity and readability.
    Python is widely used in data science, web development, and artificial intelligence.
    The language emphasizes code readability with its significant whitespace.
    Python has a large standard library and active community.
    """


@pytest.fixture
def sample_documents():
    """Sample documents for RAG testing."""
    return [
        {
            "id": "doc1",
            "content": "Python is a high-level programming language.",
            "source": "test_doc1.txt",
            "metadata": {"type": "text"}
        },
        {
            "id": "doc2",
            "content": "Machine learning is a subset of artificial intelligence.",
            "source": "test_doc2.txt",
            "metadata": {"type": "text"}
        },
        {
            "id": "doc3",
            "content": "Data science combines statistics, programming, and domain knowledge.",
            "source": "test_doc3.txt",
            "metadata": {"type": "text"}
        }
    ]


@pytest.fixture
def mock_yfinance():
    """Mock yfinance API for stock testing."""
    with patch('yfinance.Ticker') as mock_ticker:
        # Setup mock data
        mock_ticker_instance = MagicMock()
        mock_ticker_instance.history.return_value = MagicMock()
        mock_ticker_instance.info = {
            'symbol': 'AAPL',
            'regularMarketPrice': 150.0,
            'regularMarketChange': 2.5,
            'regularMarketChangePercent': 1.7
        }
        mock_ticker.return_value = mock_ticker_instance
        yield mock_ticker


@pytest.fixture
def mock_qt_app():
    """Mock PyQt6 application for GUI testing."""
    # This prevents actual QApplication creation during tests
    with patch('PyQt6.QtWidgets.QApplication'):
        with patch('PyQt6.QtCore.QTimer'):
            yield MagicMock()


# ============================================================================
# MARKERS - For test categorization
# ============================================================================

def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line("markers", "unit: Unit tests (fast, isolated)")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "performance: Performance benchmarks")
    config.addinivalue_line("markers", "gui: GUI component tests")
    config.addinivalue_line("markers", "rag: RAG system tests")
    config.addinivalue_line("markers", "stock: Stock Viewer tests")
    config.addinivalue_line("markers", "slow: Slow tests")
    config.addinivalue_line("markers", "serial: Tests requiring serial execution")


# ============================================================================
# HOOKS - pytest lifecycle hooks
# ============================================================================

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Provide test outcome reporting."""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call":
        # Add test markers to report
        markers = [marker.name for marker in item.iter_markers()]
        rep.markers = markers


def pytest_collection_modifyitems(config, items):
    """Modify test collection."""
    for item in items:
        # Mark tests by location
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif "performance" in str(item.fspath):
            item.add_marker(pytest.mark.performance)
        elif "gui" in str(item.fspath):
            item.add_marker(pytest.mark.gui)


# ============================================================================
# HELPER FUNCTIONS - Available throughout tests
# ============================================================================

def assert_valid_response(response: dict):
    """Assert response has valid structure."""
    assert isinstance(response, dict)
    assert "status" in response
    assert response["status"] in ["success", "error", "warning"]
    return True


def create_test_document(content: str, doc_id: str = "test_doc", source: str = "test.txt"):
    """Create a test document."""
    return {
        "id": doc_id,
        "content": content,
        "source": source,
        "metadata": {"type": "text", "created": "2024-01-01"}
    }


# ============================================================================
# CLEANUP & TEARDOWN
# ============================================================================

@pytest.fixture(autouse=True)
def cleanup_after_test():
    """Cleanup after each test."""
    yield
    # Cleanup code here if needed


# ============================================================================
# ITERATION 1 CHECKLIST
# ============================================================================
"""
✓ pytest.ini created with configuration
✓ conftest.py created with fixtures
✓ Test markers registered
✓ Fixtures available for:
  - Document processing
  - RAG system
  - Stock viewer (mocked yfinance)
  - GUI testing (mocked Qt)
✓ Ready for Iteration 2: Test fixtures expansion

Next: Iteration 2 - Create specific test fixtures for RAG modules
"""
