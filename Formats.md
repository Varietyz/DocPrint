# DocPrint Formatters

Complete reference with examples for all available formatters.

## Basic Content

### header
```python
docPrint('header', 'Section Title', 'Optional description')
```

**Output:**
```markdown
## Section Title

Optional description

---
```
## Section Title

Optional description

---

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### text
```python
docPrint('text', 'Status', 'System operational')
```

**Output:**
```markdown
## Status

System operational
```
## Status

System operational

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### table
```python
docPrint('table', 'Performance Data', [
    {'metric': 'CPU', 'value': '45%'},
    {'metric': 'Memory', 'value': '2.1GB'}
])
```

**Output:**
```markdown
## Performance Data

| metric | value |
|---|---|
| CPU | 45% |
| Memory | 2.1GB |
```
## Performance Data

| metric | value |
|---|---|
| CPU | 45% |
| Memory | 2.1GB |

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### advanced_table
```python
docPrint('advanced_table', 'User Data', {
    'headers': ['Name', 'Age', 'Score'],
    'alignment': ['left', 'center', 'right'],
    'rows': [
        ['Alice', 25, 95.5],
        ['Bob', 30, 88.2]
    ]
})
```

**Output:**
```markdown
## User Data

| Name | Age | Score |
|---|:---:|---:|
| Alice | 25 | 95.5 |
| Bob | 30 | 88.2 |
```
## User Data

| Name | Age | Score |
|---|:---:|---:|
| Alice | 25 | 95.5 |
| Bob | 30 | 88.2 |

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### bullets
```python
docPrint('bullets', 'Key Points', ['First point', 'Second point', 'Third point'])
```

**Output:**
```markdown
## Key Points

- First point
- Second point
- Third point
```
## Key Points

- First point
- Second point
- Third point

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### code_block
```python
docPrint('code_block', 'Python Example', 'print("Hello World")', language='python')
```

**Output:**
## Python Example

```python
print("Hello World")
```


<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

## Structural Elements

### divider
Create custom visual dividers with various styles.

```python
# Simple colored line
docPrint('divider', 'Section Break', color='#e74c3c', thickness=2)

# Headerless divider
docPrint('divider', '', divider_type='gradient', no_header=True)

# Thick divider with custom styling
docPrint('divider', 'Important Section', divider_type='thick', color='#3498db', thickness=5)
```

**Available divider types:**
- `simple` - Basic colored line
- `thick` - Thick line with rounded corners
- `solid` - Solid color block
- `gradient` - Multi-color gradient
- `dotted` - Dotted pattern
- `shadow` - Line with drop shadow
- `fade` - Fading gradient
- `rainbow` - Multi-color rainbow
- `dashed` - Dashed pattern
- `double` - Double line style

**Output examples:**
```html
## Section Break

<hr style="border: none; height: 2px; background-color: #e74c3c;">

<div style="height: 4px; background: linear-gradient(90deg, #ff6b6b 0%, #4ecdc4 50%, #45b7d1 100%); border-radius: 2px; margin: 20px 0;"></div>

## Important Section

<hr style="border: none; height: 5px; background-color: #3498db; border-radius: 3px;">
```
## Section Break

<hr style="border: none; height: 2px; background-color: #e74c3c;">

<div style="height: 4px; background: linear-gradient(90deg, #ff6b6b 0%, #4ecdc4 50%, #45b7d1 100%); border-radius: 2px; margin: 20px 0;"></div>

## Important Section

<hr style="border: none; height: 5px; background-color: #3498db; border-radius: 3px;">

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### horizontal_rule
```python
docPrint('horizontal_rule', 'Section Break', 'Content above the line')
```

**Output:**
```markdown
## Section Break

Content above the line

---
```
## Section Break

Content above the line

---

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### blockquote
```python
# Single line
docPrint('blockquote', 'Quote', 'This is important text')

# Multi-line
docPrint('blockquote', 'Multi-line Quote', ['Line 1', 'Line 2', 'Line 3'])
```

**Output:**
```markdown
## Quote

> This is important text

## Multi-line Quote

> Line 1
> Line 2
> Line 3
```
## Quote

> This is important text

## Multi-line Quote

> Line 1
> Line 2
> Line 3

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### ordered_list
```python
docPrint('ordered_list', 'Steps', ['Step 1', 'Step 2', 'Step 3'])
```

**Output:**
```markdown
## Steps

1. Step 1
2. Step 2
3. Step 3
```
## Steps

1. Step 1
2. Step 2
3. Step 3

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### unordered_list
```python
docPrint('unordered_list', 'Items', ['Item A', 'Item B', 'Item C'])
```

**Output:**
```markdown
## Items

- Item A
- Item B
- Item C
```
## Items

- Item A
- Item B
- Item C

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### footnotes
```python
docPrint('footnotes', 'Research Paper', 
         ("This study builds on previous work", 
          {1: "Source: Smith et al. 2020", 2: "Additional data from Johnson study"}))
```

**Output:**
```markdown
## Research Paper

This study builds on previous work[^1][^2]

[^1]: Source: Smith et al. 2020
[^2]: Additional data from Johnson study
```
## Research Paper

This study builds on previous work[^1][^2]

[^1]: Source: Smith et al. 2020
[^2]: Additional data from Johnson study

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### definition_list
```python
docPrint('definition_list', 'Glossary', {
    "API": "Application Programming Interface",
    "JSON": "JavaScript Object Notation"
}, line=True)
```

**Output:**
```markdown
## Glossary

API
: Application Programming Interface

JSON
: JavaScript Object Notation

---
```
## Glossary

API
: Application Programming Interface

JSON
: JavaScript Object Notation

---

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### task_list
```python
docPrint('task_list', 'Checklist', [
    {"task": "Write documentation", "completed": True},
    {"task": "Test features", "completed": False}
], line=True)
```

**Output:**
```markdown
## Checklist

- [x] Write documentation
- [ ] Test features

---
```
## Checklist

- [x] Write documentation
- [ ] Test features

---

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

## Layout Elements

### flex_layout
```python
docPrint('flex_layout', 'Dashboard', [
    {
        'type': 'text',
        'header': 'CPU Usage',
        'content': '45%',
        'style': 'background: #ff0000ff; padding: 10px;'
    },
    {
        'type': 'table', 
        'header': 'Memory',
        'content': [{'used': '2.1GB', 'free': '1.9GB'}],
        'style': 'background: #ff0000ff; padding: 10px;'
    }
], container_style='display: flex; gap: 20px; margin: 10px;')
```

**Output:**
```html
## Dashboard

<div style="display: flex; gap: 20px; margin: 10px;">

<div style="flex: 1; background: #ff0000ff; padding: 10px;">

### CPU Usage

45%

</div>

<div style="flex: 1; background: #ff0000ff; padding: 10px;">

### Memory

| used | free |
|---|---|
| 2.1GB | 1.9GB |

</div>

</div>
```
## Dashboard

<div style="display: flex; gap: 20px; margin: 10px;">

<div style="flex: 1; background: #ff0000ff; padding: 10px;">

### CPU Usage

45%

</div>

<div style="flex: 1; background: #ff0000ff; padding: 10px;">

### Memory

| used | free |
|---|---|
| 2.1GB | 1.9GB |

</div>

</div>

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### table_layout
```python
docPrint('table_layout', 'Comparison View', [
    {
        'type': 'bullets',
        'header': 'Features',
        'content': ['Fast', 'Reliable', 'Scalable'],
        'style': 'border: 1px solid #ccc; padding: 15px;'
    },
    {
        'type': 'alert',
        'header': 'Status',
        'content': 'All systems operational',
        'kwargs': {'alert_type': 'success'},
        'style': 'border: 1px solid #ccc; padding: 15px;'
    }
], table_style='width: 100%; border-collapse: collapse; margin: 10px 0;')
```

**Output:**
```html
## Comparison View

<table style="width: 100%; border-collapse: collapse; margin: 10px 0;">
<tr>
<td style="vertical-align: top; padding: 10px; border: 1px solid #ccc; padding: 15px;">

### Features

- Fast
- Reliable
- Scalable

</td>
<td style="vertical-align: top; padding: 10px; border: 1px solid #ccc; padding: 15px;">

### Status

> **[SUCCESS]**
>
> All systems operational

</td>
</tr>
</table>
```
## Comparison View

<table style="width: 100%; border-collapse: collapse; margin: 10px 0;">
<tr>
<td style="vertical-align: top; padding: 10px; border: 1px solid #ccc; padding: 15px;">

### Features

- Fast
- Reliable
- Scalable

</td>
<td style="vertical-align: top; padding: 10px; border: 1px solid #ccc; padding: 15px;">

### Status

> **[SUCCESS]**
>
> All systems operational

</td>
</tr>
</table>

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### grid_layout
```python
docPrint('grid_layout', 'Services Overview', [
    {'type': 'text', 'header': 'Web Server', 'content': 'Running'},
    {'type': 'text', 'header': 'Database', 'content': 'Connected'},
    {'type': 'text', 'header': 'Cache', 'content': 'Active'},
    {'type': 'text', 'header': 'Queue', 'content': 'Processing'}
], columns=2, gap='15px')
```

**Output:**
```html
## Services Overview

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;">

<div style="">

### Web Server

Running

</div>

<div style="">

### Database

Connected

</div>

<div style="">

### Cache

Active

</div>

<div style="">

### Queue

Processing

</div>

</div>
```
## Services Overview

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;">

<div style="">

### Web Server

Running

</div>

<div style="">

### Database

Connected

</div>

<div style="">

### Cache

Active

</div>

<div style="">

### Queue

Processing

</div>

</div>

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

## Visual Elements

### badge
```python
# Simple badge
docPrint('badge', 'Build Status', {
    'label': 'build',
    'message': 'passing',
    'color': 'green'
})

# Badge with logo and URL
docPrint('badge', 'Python Version', {
    'label': 'Python',
    'message': '3.9+',
    'color': 'blue',
    'logo': 'python',
    'logo_color': 'white',
    'url': 'https://python.org'
})
```

**Output:**
```markdown
## Build Status

![build](https://img.shields.io/badge/build-passing-green)

## Python Version

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)](https://python.org)
```
## Build Status

![build](https://img.shields.io/badge/build-passing-green)

## Python Version

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)](https://python.org)

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### html_block
```python
docPrint('html_block', 'Custom HTML', {
    'tag': 'div',
    'attributes': {
        'class': 'highlight', 
        'id': 'test-div', 
        'style': 'background: green; padding: 10px;'
    },
    'content': 'This is custom HTML content with styling'
})
```

**Output:**
```html
## Custom HTML

<div class="highlight" id="test-div" style="background: green; padding: 10px;">
This is custom HTML content with styling
</div>
```
## Custom HTML

<div class="highlight" id="test-div" style="background: green; padding: 10px;">
This is custom HTML content with styling
</div>

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### css_block
```python
docPrint('css_block', 'Component Styling', {
    'selector': '.dashboard-card',
    'styles': {
        'background-color': '#f8f9fa',
        'border': '1px solid #dee2e6',
        'border-radius': '8px',
        'padding': '1rem',
        'margin': '0.5rem'
    }
})
```

**Output:**
## Component Styling
```css
.dashboard-card {
  background-color: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 1rem;
  margin: 0.5rem;
}
```

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### svg_animation
```python
docPrint('svg_animation', 'Loading Spinner', {
    'width': 60,
    'height': 60,
    'elements': [{
        'tag': 'circle',
        'attributes': {
            'cx': 30, 'cy': 30, 'r': 20, 
            'fill': 'none', 'stroke': 'blue', 'stroke-width': 3
        },
        'animations': [{
            'attributeName': 'stroke-dasharray',
            'values': '0 126;63 63;0 126',
            'dur': '2s',
            'repeatCount': 'indefinite'
        }]
    }]
})
```

**Output:**
```html
## Loading Spinner

<svg width="60" height="60" xmlns="http://www.w3.org/2000/svg">
  <circle cx="30" cy="30" r="20" fill="none" stroke="blue" stroke-width="3">
    <animate attributeName="stroke-dasharray" values="0 126;63 63;0 126" dur="2s" repeatCount="indefinite" />
  </circle>
</svg>
```
## Loading Spinner

<svg width="60" height="60" xmlns="http://www.w3.org/2000/svg">
  <circle cx="30" cy="30" r="20" fill="none" stroke="blue" stroke-width="3">
    <animate attributeName="stroke-dasharray" values="0 126;63 63;0 126" dur="2s" repeatCount="indefinite" />
  </circle>
</svg>

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

## Rich Content

### alert
```python
# Different alert types
docPrint('alert', 'Information', 'System maintenance scheduled', alert_type='info')
docPrint('alert', 'Warning', 'Disk space running low', alert_type='warning')
docPrint('alert', 'Error', 'Database connection failed', alert_type='error')
docPrint('alert', 'Success', 'Deployment completed', alert_type='success')
docPrint('alert', 'Note', 'Remember to backup before upgrading', alert_type='note')

# Multi-line alert
docPrint('alert', 'Error Summary', [
    'Database connection failed', 
    'Retry attempts exhausted'
], alert_type='error')
```

**Output:**
```markdown
## Information

> **[INFO]**
>
> System maintenance scheduled

## Warning

> **[WARNING]**
>
> Disk space running low

## Error

> **[ERROR]**
>
> Database connection failed

## Success

> **[SUCCESS]**
>
> Deployment completed

## Note

> **[NOTE]**
>
> Remember to backup before upgrading

## Error Summary

> **[ERROR]**
>
> Database connection failed
> Retry attempts exhausted
```
## Information

> **[INFO]**
>
> System maintenance scheduled

## Warning

> **[WARNING]**
>
> Disk space running low

## Error

> **[ERROR]**
>
> Database connection failed

## Success

> **[SUCCESS]**
>
> Deployment completed

## Note

> **[NOTE]**
>
> Remember to backup before upgrading

## Error Summary

> **[ERROR]**
>
> Database connection failed
> Retry attempts exhausted

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### collapsible
```python
docPrint('collapsible', 'Debug Information', [
    'Stack trace: line 42 in main.py',
    'Memory usage: 1.2GB',
    'CPU time: 2.1s'
], summary='Click to show debug details')
```

**Output:**
```html
## Debug Information

<details>
<summary>Click to show debug details</summary>

Stack trace: line 42 in main.py

Memory usage: 1.2GB

CPU time: 2.1s

</details>
```
## Debug Information

<details>
<summary>Click to show debug details</summary>

Stack trace: line 42 in main.py

Memory usage: 1.2GB

CPU time: 2.1s

</details>

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### image
```python
# Simple image
docPrint('image', 'Screenshot', 'https://example.com/screenshot.jpg')

# Detailed image configuration
docPrint('image', 'Architecture Diagram', {
    'url': 'https://example.com/architecture.png',
    'alt': 'System Architecture',
    'title': 'Complete system overview',
    'width': '800',
    'height': '400'
})
```

**Output:**
```html
## Screenshot

![Image](https://example.com/screenshot.jpg)

## Architecture Diagram

<img src="https://example.com/architecture.png" alt="System Architecture" width="800" height="400" title="Complete system overview" />
```
## Screenshot

![Image](https://example.com/screenshot.jpg)

## Architecture Diagram

<img src="https://example.com/architecture.png" alt="System Architecture" width="800" height="400" title="Complete system overview" />

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### link_collection
```python
docPrint('link_collection', 'Development Resources', [
    {
        'url': 'https://github.com/company/project', 
        'text': 'Source Code', 
        'description': 'Main repository'
    },
    {
        'url': 'https://docs.company.com', 
        'text': 'Documentation', 
        'description': 'API reference'
    },
    {
        'url': 'https://company.slack.com', 
        'text': 'Team Chat'
    },
    'https://example.com/simple-link'
])
```

**Output:**
```markdown
## Development Resources

- [Source Code](https://github.com/company/project) - Main repository
- [Documentation](https://docs.company.com) - API reference
- [Team Chat](https://company.slack.com)
- https://example.com/simple-link
```
## Development Resources

- [Source Code](https://github.com/company/project) - Main repository
- [Documentation](https://docs.company.com) - API reference
- [Team Chat](https://company.slack.com)
- https://example.com/simple-link

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

## Layout Block Configuration

For `flex_layout`, `table_layout`, and `grid_layout`, each block uses this structure:

```python
{
    'type': 'formatter_name',    # Any valid formatter
    'header': 'Block Title',     # Header for this block
    'content': content_data,     # Content appropriate for the formatter
    'style': 'css_styles',       # Optional CSS for the block container
    'kwargs': {                  # Optional formatter-specific parameters
        'alert_type': 'warning',
        'language': 'python',
        'divider_type': 'gradient'  # For divider blocks
    }
}
```

**Example with kwargs:**
```python
docPrint('flex_layout', 'Code and Alert', [
    {
        'type': 'code_block',
        'header': 'Python Code',
        'content': 'def hello(): return "world"',
        'kwargs': {'language': 'python'}
    },
    {
        'type': 'divider',
        'header': '',
        'content': '',
        'kwargs': {
            'divider_type': 'rainbow',
            'thickness': 4,
            'no_header': True
        }
    },
    {
        'type': 'alert',
        'header': 'Warning',
        'content': 'Code not tested',
        'kwargs': {'alert_type': 'warning'}
    }
])
```

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

## Divider Examples

### Basic Dividers
```python
# Simple divider with color
docPrint('divider', 'Basic', color='#3498db', thickness=3)

# Thick divider with rounded corners
docPrint('divider', 'Thick Section', divider_type='thick', color='#e74c3c', thickness=5)

# Headerless gradient divider
docPrint('divider', '', divider_type='gradient', no_header=True, thickness=4)
```

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### Styled Dividers
```python
# Solid color block
docPrint('divider', 'Solid Block', divider_type='solid', color='#2ecc71', thickness=3, margin='30px 0')

# Dotted pattern
docPrint('divider', 'Dotted Line', divider_type='dotted', color='#f39c12', thickness=2)

# Shadow effect
docPrint('divider', 'With Shadow', divider_type='shadow', color='#9b59b6', thickness=3)
```

<div style="height: 3px; background-color: #12726dff; margin: 30px 0;"></div>

### Special Effects
```python
# Fading gradient
docPrint('divider', 'Fade Effect', divider_type='fade', color='#34495e')

# Rainbow gradient
docPrint('divider', 'Rainbow', divider_type='rainbow', thickness=6, margin='25px 0')

# Dashed pattern
docPrint('divider', 'Dashed', divider_type='dashed', color='#16a085', thickness=3)

# Double line
docPrint('divider', 'Double Line', divider_type='double', color='#c0392b', thickness=6)
```

**Output examples:**
```html
## Basic

<hr style="border: none; height: 3px; background-color: #3498db;">

## Thick Section

<hr style="border: none; height: 5px; background-color: #e74c3c; border-radius: 3px;">

<div style="height: 4px; background: linear-gradient(90deg, #ff6b6b 0%, #4ecdc4 50%, #45b7d1 100%); border-radius: 2px; margin: 20px 0;"></div>

## Solid Block

<div style="height: 3px; background-color: #2ecc71; margin: 30px 0;"></div>
```

## Basic

<hr style="border: none; height: 3px; background-color: #3498db;">

## Thick Section

<hr style="border: none; height: 5px; background-color: #e74c3c; border-radius: 3px;">

<div style="height: 4px; background: linear-gradient(90deg, #ff6b6b 0%, #4ecdc4 50%, #45b7d1 100%); border-radius: 2px; margin: 20px 0;"></div>

## Solid Block

<div style="height: 3px; background-color: #2ecc71; margin: 30px 0;"></div>

## Documents

- [README.md](https://github.com/Varietyz/DocPrint/blob/main/README.md)
- [Reference_Table.md](https://github.com/Varietyz/DocPrint/blob/main/Reference_Table.md) - Function signatures and parameters
