# 🚀 Phase 1 Quick Start Guide

## Running Tests

### Run All Tests
```powershell
cd D:\projects\ScrapeMatrix
python -m pytest tests/ -v
```

### Run Framework Verification (Iteration 1)
```powershell
python -m pytest tests/test_framework.py -v
```

### Run with Coverage
```powershell
python -m pytest tests/ -v --cov=src/scrapematrix --cov-report=html
```

### Run Specific Test Type
```powershell
# Unit tests only
python -m pytest -m unit -v

# Integration tests only
python -m pytest -m integration -v

# RAG tests only
python -m pytest -m rag -v
```

---

## Building the Application

### Clean Build
```powershell
cd D:\projects\ScrapeMatrix
python packaging/build_executable.py --clean
```

### Build Status Check
```powershell
# Check if executable was created
Get-ChildItem -Path dist\ScrapeMatrix\ScrapeMatrix.exe
```

### Run Application
```powershell
.\dist\ScrapeMatrix\ScrapeMatrix.exe
```

---

## Phase 1 Iteration Workflow

### For Each Iteration:

#### 1. **Implement** (60-120 min)
```powershell
# Create/modify test files in tests/
# Update fixtures in tests/conftest.py if needed
# Document your changes
```

#### 2. **Test** (20-30 min)
```powershell
# Run your new tests
python -m pytest tests/test_new_feature.py -v

# Check overall test status
python -m pytest tests/ -v

# Verify coverage
python -m pytest tests/ --cov=src/scrapematrix --cov-report=term-missing
```

#### 3. **Build** (10-15 min)
```powershell
# Verify build still works
python packaging/build_executable.py --clean

# Check executable exists
Test-Path dist\ScrapeMatrix\ScrapeMatrix.exe
```

#### 4. **Document** (15-20 min)
```powershell
# Create iteration summary
# Update PROGRESS_DASHBOARD.md
# Commit changes to git
```

#### 5. **Verify** (10-15 min)
```powershell
# Check for regressions
python -m pytest tests/ --tb=short

# Verify no breaking changes
.\dist\ScrapeMatrix\ScrapeMatrix.exe
```

---

## Iteration 1 Status

✅ **COMPLETE**

- [x] pytest.ini created
- [x] tests/conftest.py created with 5 fixtures
- [x] tests/test_framework.py created with 7 tests
- [x] All 7 tests passing (100%)
- [x] Build system fixed (6 encoding issues)
- [x] Application runnable

### Files Created:
- `pytest.ini` - pytest configuration
- `tests/conftest.py` - fixtures and configuration
- `tests/test_framework.py` - framework verification tests
- `PHASE_1_ITERATION_1_COMPLETE.md` - detailed completion report
- `PROGRESS_DASHBOARD.md` - progress tracking
- `PHASE_1_QUICK_REFERENCE.md` - this file

### Build Status:
```
✅ All Python files compile
✅ Framework tests pass (7/7)
✅ Executable builds successfully
✅ Application launches
```

---

## Iteration 2 Preview

### Tasks for Iteration 2: Test Fixtures & Mocking
- Create RAG-specific fixtures
- Create mocking utilities
- Create test data generators
- Setup mock databases
- Create mock API responses

**Start:** Next iteration  
**Duration:** ~2 hours  
**Blocking:** None (can start immediately)

---

## Key Commands Reference

```powershell
# Navigation
cd D:\projects\ScrapeMatrix

# Testing
python -m pytest tests/ -v                    # All tests
python -m pytest tests/test_framework.py -v   # Iteration 1
python -m pytest -m unit -v                   # Unit tests only
python -m pytest --cov=src/scrapematrix       # With coverage

# Building
python packaging/build_executable.py --clean  # Build
Test-Path dist\ScrapeMatrix\ScrapeMatrix.exe # Check executable
.\dist\ScrapeMatrix\ScrapeMatrix.exe         # Run app

# Verification
python -m py_compile src/**/*.py              # Check syntax
Get-ChildItem tests/ -Recurse -Filter *.py   # List test files
```

---

## Git Workflow for Each Iteration

```powershell
# Before starting
git checkout main
git pull origin main

# After completing iteration
git add -A
git commit -m "Phase 1 Iteration X: [description]"
git push origin main

# Example:
git commit -m "Phase 1 Iteration 1: Test Framework Setup - All tests passing"
```

---

## Troubleshooting

### Tests not found
```powershell
# Verify pytest.ini exists
Test-Path pytest.ini

# Check test discovery
python -m pytest --collect-only tests/
```

### Build fails
```powershell
# Clean everything
rm -Force -Recurse build, dist

# Rebuild
python packaging/build_executable.py --clean

# Check for errors
python -c "from scrapematrix.gui.main_window import MainWindow"
```

### Encoding errors
```powershell
# Already fixed in Iteration 1!
# All write_text() calls now use encoding='utf-8'
```

---

## Performance Baseline (Iteration 1)

| Metric | Value |
|--------|-------|
| Test Execution Time | 20.70s |
| Build Time | ~8 minutes |
| Executable Size | ~113 MB |
| Framework Tests | 7 |
| Fixtures Available | 5 |

---

## Progress Tracking

### Phase 1 Progress
- Iteration 1: ✅ COMPLETE (0/50 baseline)
- Iteration 2-50: ⏳ PENDING

### Overall Progress
- Phase 1 (1-50): 🟡 2% (1/50)
- Phase 2 (51-100): ⏳ 0%
- Phase 3 (101-150): ⏳ 0%
- Phase 4 (151-175): ⏳ 0%
- Phase 5 (176-200): ⏳ 0%
- **Total: 0.5% (1/200)**

---

## Resources

- **Master Roadmap:** `ITERATIVE_ROADMAP_200.md`
- **Iteration Details:** `PHASE_1_ITERATION_1_COMPLETE.md`
- **Progress Dashboard:** `PROGRESS_DASHBOARD.md`
- **pytest Documentation:** https://docs.pytest.org/
- **Coverage.py Documentation:** https://coverage.readthedocs.io/

---

## Checklist for Next Iteration

Before starting Iteration 2:
- [ ] Review `PHASE_1_ITERATION_1_COMPLETE.md`
- [ ] Verify Iteration 1 tasks all complete
- [ ] Review `ITERATIVE_ROADMAP_200.md` for Iteration 2 details
- [ ] Create `tests/unit/` and `tests/integration/` subdirectories if needed
- [ ] Plan fixtures for RAG module testing

---

**Quick Reference Created:** 2024-01-01  
**For Phase:** 1 of 5  
**Status:** ✅ READY FOR ITERATION 2
