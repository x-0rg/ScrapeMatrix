# How to Add Images to README.md

## Quick Answer

```markdown
![Alt text for image](./path/to/image.png)
```

---

## Three Ways to Add Images

### Method 1: Local Image File (Recommended for GitHub)
```markdown
![Stock Viewer Interface](./docs/screenshots/stock_viewer.png)
```

**Pros:**
- ✅ Images stay in repository
- ✅ No external dependencies
- ✅ Works when cloned
- ✅ Best for version control

**Setup:**
```bash
mkdir -p docs/screenshots
# Copy your image to docs/screenshots/
```

### Method 2: Online Image URL
```markdown
![Alt text](https://example.com/image.png)
```

**Pros:**
- ✅ No repository size increase
- ✅ Easy to update

**Cons:**
- ❌ Link may break
- ❌ Requires internet
- ❌ Speed depends on host

### Method 3: HTML with Size Control
```markdown
<img src="./docs/screenshots/image.png" alt="Stock Viewer" width="600">
```

**Pros:**
- ✅ Full HTML control
- ✅ Responsive sizing
- ✅ Custom styling

---

## ScrapeMatrix Example

### Setup Directory
```bash
mkdir -p docs/screenshots
```

### Add to README.md
```markdown
# ScrapeMatrix

Industrial-Grade Stock Analysis Desktop Application

## Features

### Stock Viewer
![Stock Viewer Interface](./docs/screenshots/stock_viewer.png)

Real-time stock data visualization with:
- Interactive price charts
- Company information
- 50-day historical data
- Professional styling

### Dynamic Ticker Suggestions
![Ticker Autocomplete](./docs/screenshots/autocomplete.png)

Smart suggestions while you type with 70+ popular stocks.

## Getting Started

```bash
pip install -e .
python -m scrapematrix
```
```

---

## Image Best Practices

### File Format
| Format | Use Case | Notes |
|--------|----------|-------|
| **PNG** | Screenshots | Lossless, good for UI |
| **JPG/JPEG** | Photos | Smaller files |
| **GIF** | Animations | Supported by markdown |
| **SVG** | Icons | Vector, scalable |
| **WebP** | Modern | Check browser support |

### File Size
- **Target:** < 500 KB per image
- **Ideal:** 200-300 KB
- Use image compression tools if needed

### Dimensions
- **Dashboard:** 800x600 or 1024x768
- **Full page:** 1200x800
- **Mobile:** 375x667
- Use `width="600"` in HTML for consistency

### File Names
```
✅ Good:
  stock_viewer.png
  ticker_autocomplete.png
  dashboard_overview.png

❌ Avoid:
  image1.png
  screenshot_2024-01-15_at_12.34.56.png
  IMG_0001.JPG
```

---

## Complete README Example

```markdown
# ScrapeMatrix

> Industrial-Grade Stock Analysis Desktop Application

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📸 Screenshots

### Stock Viewer with Real-Time Charts
![Stock Viewer Interface showing AAPL data with candlestick chart](./docs/screenshots/stock_viewer.png)

### Intelligent Ticker Suggestions
![Autocomplete dropdown showing matching stock symbols](./docs/screenshots/ticker_suggestions.png)

## ✨ Features

- 📈 Real-time stock data visualization
- 🎯 Smart ticker suggestions with autocomplete
- 📊 Interactive charts and analytics
- ⚡ Non-blocking UI with background threading
- 🎨 Professional PyQt6 interface

## 🚀 Quick Start

### Installation
```bash
pip install -e .
```

### Run
```bash
python -m scrapematrix
```

## 📚 Documentation

- [Quick Reference](./docs/QUICK_REFERENCE.md)
- [Code Cleanup Guide](./docs/CLEANUP_SUMMARY.md)
- [Complete Documentation Index](./docs/INDEX.md)

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details

## 👥 Contributing

Contributions welcome! See our [development guide](./docs/CLEANUP_CHECKLIST.md).
```

---

## Troubleshooting Images

### Image Not Showing?

**Check 1: File Path**
```
✅ Correct:   ./docs/screenshots/image.png
✅ Correct:   docs/screenshots/image.png
❌ Wrong:     /docs/screenshots/image.png  (absolute)
❌ Wrong:     C:/path/to/image.png  (full path)
```

**Check 2: File Exists**
```bash
# Verify file exists
ls -la docs/screenshots/
# or on Windows
dir docs\screenshots\
```

**Check 3: Syntax**
```markdown
✅ Correct:   ![Alt text](./path/to/image.png)
❌ Wrong:     ![Alt text] (./path/to/image.png)  # space before paren
❌ Wrong:     ! [Alt text](./path/to/image.png)  # space after !
```

**Check 4: Special Characters**
```markdown
✅ Good:      image_name.png
✅ Good:      image-name.png
❌ Bad:       image name.png  (space)
❌ Bad:       image@name.png  (special char)
```

---

## GitHub-Specific Tips

### Relative Paths Work Best
```markdown
<!-- These work on GitHub: -->
![Image](./docs/screenshots/image.png)
![Image](docs/screenshots/image.png)

<!-- These don't work everywhere: -->
![Image](/docs/screenshots/image.png)  ❌ Absolute path
![Image](https://raw.githubusercontent.com/...) ⚠️ Fragile
```

### Raw GitHub URLs
If you need the direct URL:
```
https://raw.githubusercontent.com/YOUR_REPO/main/docs/screenshots/image.png
```

### Image Alignment (HTML)
```html
<div align="center">
  <img src="./docs/screenshots/image.png" alt="Centered image" width="600">
</div>
```

---

## Image Optimization

### Using ImageMagick
```bash
convert original.png -resize 1024x768 -quality 85 optimized.png
```

### Using Python
```python
from PIL import Image

img = Image.open('original.png')
img.thumbnail((1024, 768))
img.save('optimized.png', quality=85)
```

### Online Tools
- **TinyPNG:** https://tinypng.com/
- **Compressor.io:** https://compressor.io/
- **ImageOptim:** https://imageoptim.com/

---

## Responsive Images

### Simple CSS
```markdown
<img src="./docs/screenshots/image.png" 
     alt="Stock Viewer Interface" 
     style="max-width: 100%; height: auto;">
```

### Picture Element
```markdown
<picture>
  <source media="(max-width: 768px)" srcset="./docs/screenshots/image_mobile.png">
  <img src="./docs/screenshots/image.png" alt="Stock Viewer">
</picture>
```

---

## Git and Images

### .gitignore
```
# Temporary image files
docs/screenshots/*.tmp
docs/screenshots/*.bak

# OS generated files
.DS_Store
Thumbs.db
```

### Large Image Files (Git LFS)
```bash
# Install Git LFS
git lfs install

# Track PNG files
git lfs track "*.png"
git add .gitattributes

# Commit as normal
git add docs/screenshots/
git commit -m "Add screenshots"
```

---

## SEO and Accessibility

### Always Include Alt Text
```markdown
✅ Good:
![Stock Viewer showing AAPL data with price chart and company info](./image.png)

❌ Bad:
![image](./image.png)
![screenshot](./image.png)
```

### With Captions
```markdown
![Stock Viewer Interface](./docs/screenshots/stock_viewer.png)
*The stock viewer widget showing real-time price data and historical charts*
```

---

## For ScrapeMatrix Specifically

### Recommended Screenshots
1. **Main Window** - Overall application layout
2. **Stock Viewer** - With sample stock (AAPL)
3. **Autocomplete** - Showing ticker suggestions
4. **Chart** - Example price chart
5. **Data Table** - Historical data display

### Setup Steps
```bash
# Create directory
mkdir -p docs/screenshots

# Add your screenshots
# Take screenshots and save to docs/screenshots/
# Name them: stock_viewer.png, ticker_suggestions.png, etc.

# Update README.md with images
# See example above
```

---

## Quick Checklist

- [ ] Create `docs/screenshots/` directory
- [ ] Copy images to directory
- [ ] Image files < 500 KB each
- [ ] Image dimensions 800x600 or larger
- [ ] Use relative paths (./docs/screenshots/...)
- [ ] Add descriptive alt text
- [ ] Test on GitHub (view README online)
- [ ] Check link formatting in preview

---

## Questions?

See the main documentation:
- **docs/QUICK_REFERENCE.md** - Common commands
- **docs/INDEX.md** - Full documentation index
- **README.md** - Project overview

---

**Happy documenting! 📸**
