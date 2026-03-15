# Adding Images to README.md - Quick Guide

## Basic Markdown Syntax

### Local Image File
```markdown
![Alt text for image](./docs/screenshots/image.png)
```

**Example:**
```markdown
![Stock Viewer Interface](./docs/screenshots/stock_viewer.png)
```

### Online Image URL
```markdown
![Alt text for image](https://example.com/image.png)
```

### Image with Size Control (HTML)
```markdown
<img src="./docs/screenshots/image.png" alt="Description" width="600">
```

## Setting Up Image Directory

### Step 1: Create Screenshots Directory
```bash
mkdir docs/screenshots
```

### Step 2: Add Your Images
Copy PNG/JPG images to the `docs/screenshots/` directory

### Step 3: Update README.md
Reference them in your markdown:

```markdown
## Features

### Stock Viewer
![Stock Viewer Interface](./docs/screenshots/stock_viewer.png)

Real-time stock data visualization with:
- Interactive charts
- Company information
- Historical data tables

### Dynamic Ticker Suggestions
![Ticker Autocomplete](./docs/screenshots/autocomplete.png)

Smart suggestions as you type...
```

## Recommended Image Format

| Aspect | Recommendation |
|--------|-----------------|
| **Format** | PNG (lossless) or JPG (smaller file size) |
| **Dimensions** | 800x600 or 1024x768 (for dashboard shots) |
| **File Size** | < 500 KB per image |
| **Resolution** | 72-96 DPI is fine for web |

## Responsive Images

For better responsiveness, use HTML with CSS:

```markdown
<img src="./docs/screenshots/stock_viewer.png" alt="Stock Viewer" style="max-width: 100%; height: auto;">
```

Or create a GitHub-compatible responsive image:

```markdown
<picture>
  <img src="./docs/screenshots/stock_viewer.png" alt="Stock Viewer Interface" style="max-width: 100%;">
</picture>
```

## Best Practices

✅ **DO:**
- Use descriptive alt text for accessibility
- Keep images organized in `docs/screenshots/`
- Use relative paths starting with `./`
- Include image captions/descriptions in markdown
- Keep images under 500 KB

❌ **DON'T:**
- Use absolute paths (breaks on forks)
- Use external image hosting (links may break)
- Include huge high-resolution images
- Forget alt text (bad for SEO and accessibility)

## Complete README Example

```markdown
# ScrapeMatrix

Industrial-Grade Stock Analysis Desktop Application

## Features

### Stock Viewer
![Stock Viewer Interface](./docs/screenshots/stock_viewer.png)

Real-time stock data with interactive charts and analytics.

### Dynamic Ticker Suggestions
![Ticker Suggestions](./docs/screenshots/autocomplete.png)

Smart autocomplete with 70+ popular stock tickers.

## Getting Started

```bash
pip install -e .
python -m scrapematrix
```

## Project Structure

See [project structure documentation](./docs/PROJECT_STRUCTURE.md)
```

## Supported Image Formats in Markdown

| Format | Support | Notes |
|--------|---------|-------|
| PNG | ✅ Full | Best for screenshots, icons |
| JPG/JPEG | ✅ Full | Good for photos, smaller files |
| GIF | ✅ Full | Animations supported |
| SVG | ✅ Full | Vector graphics, scalable |
| WebP | ⚠️ Partial | Modern format, check browser support |

## Git and Images

### Adding Large Images
If images are > 100 MB, consider using Git LFS:

```bash
git lfs install
git lfs track "*.png"
git add .gitattributes
git add docs/screenshots/
```

### .gitignore for Temporary Files
```
docs/screenshots/*.tmp
docs/screenshots/*.bak
__pycache__/
*.pyc
```

## Troubleshooting

### Image not showing in GitHub?
- Check the path is relative (e.g., `./docs/screenshots/image.png`)
- Verify file exists in repository
- Check filename matches exactly (case-sensitive)

### Images too large?
- Use image compression tools
- Resize to 1024x768 max
- Convert to PNG with optimization

### Alt text shows instead of image?
- File path is incorrect
- File doesn't exist
- Syntax is malformed

---

**TIP:** Test your README locally using Markdown preview before pushing!
