# DocPrint

## Overview
DocPrint is a runtime documentation generation tool that creates live markdown output. All content is written to `DOC.PRINT.md` in the current directory.

## Basic Usage

```python
from docprint import docPrint, flush_cache, docPrintFile

# Single file
docPrintFile("file_name.md")

# Folder structure
docPrintFile("path/file_name.log")
docPrintFile("path/to/file_name.txt")
docPrintFile("path/to/folder/file_name.md")

# Generate content
docPrint(section_type, header, content, line=True, **kwargs)

# Force write to file
flush_cache()
```

---

#### Header
```python
docPrint('header', 'Section Title', 'Optional description')
```

## Section Title

Optional description


---

#### Text
```python
docPrint('text', 'Status', 'System operational', line=True)
```

## Status

System operational

---


---

#### Table
```python
docPrint('table', 'Performance Data', [
    {'metric': 'CPU', 'value': '45%'},
    {'metric': 'Memory', 'value': '2.1GB'}
])
```

## Performance Data

| metric | value |
|---|---|
| CPU | 45% |
| Memory | 2.1GB |

---

#### Bullets
```python
docPrint('bullets', 'Key Points', ['First point', 'Second point', 'Third point'])
```

## Key Points

- First point
- Second point
- Third point

---

#### Horizontal Rule
```python
docPrint('horizontal_rule', 'Section Break', 'Content above the line')
```

## Section Break

Content above the line

---

---

#### Code Block
```python
docPrint('code_block', 'Python Example', 'print("Hello World")', language='python')
```

## Python Example

```python
print("Hello World")
```

---

#### Blockquote

```python
docPrint('blockquote', 'Quote', 'This is important text')
```

## Quote

> This is important text

---

#### Ordered List
```python
docPrint('ordered_list', 'Steps', ['Step 1', 'Step 2', 'Step 3'])
```

## Steps

1. Step 1
2. Step 2
3. Step 3

---

#### Unordered List
```python
docPrint('unordered_list', 'Items', ['Item A', 'Item B', 'Item C'])
```

## Items

- Item A
- Item B
- Item C

---

### Visual Elements

#### Badge
```python
docPrint('badge', 'Build Status', {
    'label': 'build',
    'message': 'passing',
    'color': 'green',
    'style': 'flat',
    'url': 'https://github.com/repo'
})
```

## Build Status

[![build](https://img.shields.io/badge/build-passing-green?style=flat)](https://github.com/repo)

---

#### HTML Block
```python
docPrint('html_block', 'Custom HTML', {
    'tag': 'div',
    'attributes': {'class': 'highlight', 'id': 'test-div'},
    'content': 'This is custom HTML content'
})
```

## Custom HTML

<div class="highlight" id="test-div">
This is custom HTML content
</div>

---

#### CSS Block
```python
docPrint('css_block', 'Styling', {
    'selector': '.highlight',
    'styles': {
        'background-color': 'yellow',
        'padding': '10px',
        'border-radius': '5px'
    }
})
```

## Styling

```css
.highlight {
  background-color: yellow;
  padding: 10px;
  border-radius: 5px;
}
```

---

#### SVG Animation
```python
docPrint('svg_animation', 'Loading Spinner', {
    'width': 50,
    'height': 50,
    'elements': [{
        'tag': 'circle',
        'attributes': {'cx': 25, 'cy': 25, 'r': 10, 'fill': 'blue'},
        'animations': [{
            'attributeName': 'r',
            'values': '5;15;5',
            'dur': '1s',
            'repeatCount': 'indefinite'
        }]
    }]
})
```

## Loading Spinner

<svg width="50" height="50" xmlns="http://www.w3.org/2000/svg">
  <circle cx="25" cy="25" r="10" fill="blue">
    <animate attributeName="r" values="5;15;5" dur="1s" repeatCount="indefinite" />
  </circle>
</svg>

---

### Rich Content

#### Alert
```python
docPrint('alert', 'Warning', 'This is important', alert_type='warning')
docPrint('alert', 'Error List', ['Error 1', 'Error 2'], alert_type='error')
```

Alert types: `info`, `warning`, `error`, `success`, `note`

## Warning

> **[WARNING]**
>
> This is important

## Error List

> **[ERROR]**
>
> Error 1
> Error 2


---

#### Collapsible Section
```python
docPrint('collapsible', 'Details', 'Hidden content', summary='Click to expand')
```

## Details

<details>
<summary>Click to expand</summary>

Hidden content

</details>

---

#### Image
```python
docPrint('image', 'Logo', {
    'url': 'https://example.com/logo.png',
    'alt': 'Company Logo',
    'title': 'Our Logo',
    'width': '200',
    'height': '100'
})

# Simple version
docPrint('image', 'Simple Image', 'https://example.com/image.jpg')
```

## Logo

<img src="https://example.com/logo.png" alt="Company Logo" width="200" height="100" title="Our Logo" />

## Simple Image

![Image](https://example.com/image.jpg)


---

#### Link Collection
```python
docPrint('link_collection', 'Resources', [
    {'url': 'https://github.com', 'text': 'GitHub', 'description': 'Code repository'},
    {'url': 'https://docs.python.org', 'text': 'Python Docs'}
])
```

## Resources

- [GitHub](https://github.com) - Code repository
- [Python Docs](https://docs.python.org)


---

## Parameters

### Common Parameters
- `section_type`: The formatter to use
- `header`: Section header text
- `content`: Main content (string, list, or dict depending on type)
- `line`: Add separator line after content (default: True)

### Type-specific Parameters
- `language`: Code block syntax highlighting
- `alert_type`: Alert style (info, warning, error, success, note)
- `summary`: Collapsible section summary text

## Content Updates
Sections with the same header are automatically updated in place:

```python
docPrint('text', 'Status', 'Starting up')
flush_cache()

docPrint('text', 'Status', 'Running')  # Updates existing section
flush_cache()
```

## Cache Management
- Content is cached in memory and periodically flushed to file
- Manual flush: `flush_cache()`
- Auto-flush: Every 30 seconds or 100 calls (configurable)

## Configuration
Located in `docprint.config.constants`:

```python
CACHE_FLUSH_INTERVAL = 30      # seconds
CACHE_FLUSH_COUNT = 100        # calls
DOC_FILE_PREFIX = "DOC_"       # file prefix
DOC_FILE_EXTENSION = ".md"     # file extension
DEFAULT_OUTPUT_DIR = "."       # output directory
```