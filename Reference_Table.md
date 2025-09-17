# DocPrint Reference Table

## Function Signatures

### docPrint(section_type, header, content="", line=False, **kwargs)

Generate and cache formatted content.

| Parameter | Type | Description | Default |
|---|---|---|---|
| section_type | str | Formatter name | Required |
| header | str | Section header text | Required |
| content | str/list/dict | Main content | "" |
| line | bool | Add separator line | False |
| **kwargs | dict | Type-specific parameters | {} |

**Returns:** None

### docPrintFile(filepath)

Set output file for subsequent docPrint calls.

| Parameter | Type | Description | Default |
|---|---|---|---|
| filepath | str | Target file path | Required |

**Special values:**
- Empty string `""` → DOC.PRINT.md
- `"."` → DOC.PRINT.md  
- `".."` → DOC.PRINT.md

**Behavior:**
- Creates directories automatically
- Flushes current cache before switching
- Thread-safe operation

**Raises:** ValueError for invalid characters (< > : " | ? *)

### docFlush()

Force write cached content to file immediately.

**Parameters:** None
**Returns:** None
**Behavior:** No-op if cache is empty

### enableGitCommits(enabled, **kwargs)

Enable or disable automatic GitHub synchronization.

| Parameter | Type | Description | Default |
|---|---|---|---|
| enabled | bool | Enable/disable sync | Required |
| token | str | GitHub personal access token | Required when enabled |
| repo | str | Repository "username/repository" | Required when enabled |
| interval_minutes | int | Sync interval (minimum 1) | 1 |

**Raises:**
- ValueError: Invalid token, repository access denied, missing parameters
- ImportError: GitHub integration unavailable

## Type-Specific Parameters

### Divider Types (divider)

| Parameter | Type | Description | Default |
|---|---|---|---|
| divider_type | str | Divider style | "simple" |
| color | str | Divider color | "#e74c3c" |
| thickness | int | Divider thickness | 2 |
| margin | str | CSS margin | "20px 0" |
| no_header | bool | Skip header display | False |

**Valid divider_type values:** simple, thick, solid, gradient, dotted, shadow, fade, rainbow, dashed, double

### All Layout Types (flex_layout, table_layout, grid_layout)

| Parameter | Type | Description | Default |
|---|---|---|---|
| container_style | str | CSS styles for container | "" |

### flex_layout

| Parameter | Type | Description | Default |
|---|---|---|---|
| container_style | str | Flex container CSS | "display: flex; gap: 20px;" |

### table_layout

| Parameter | Type | Description | Default |
|---|---|---|---|
| table_style | str | Table element CSS | "width: 100%; border-collapse: collapse;" |

### grid_layout

| Parameter | Type | Description | Default |
|---|---|---|---|
| columns | int | Number of grid columns | 2 |
| gap | str | Grid gap size | "10px" |

### code_block

| Parameter | Type | Description | Default |
|---|---|---|---|
| language | str | Syntax highlighting language | None |

### alert

| Parameter | Type | Description | Default |
|---|---|---|---|
| alert_type | str | Alert style | "info" |

**Valid alert_type values:** info, warning, error, success, note

### collapsible

| Parameter | Type | Description | Default |
|---|---|---|---|
| summary | str | Collapsible summary text | "Details" |

### advanced_table

| Parameter | Type | Description | Default |
|---|---|---|---|
| alignment | list | Column alignment per header | ['left', ...] |

**Valid alignment values:** left, center, right

### badge

| Parameter | Type | Description | Default |
|---|---|---|---|
| (content dict) | dict | Badge configuration | {} |

**Badge content structure:**
```python
{
    'label': str,        # Badge label
    'message': str,      # Badge message  
    'color': str,        # Badge color
    'style': str,        # Badge style (optional)
    'url': str,          # Click URL (optional)
    'logo': str,         # Logo name (optional)
    'logo_color': str,   # Logo color (optional)
    'logo_width': str    # Logo width (optional)
}
```

### image

| Parameter | Type | Description | Default |
|---|---|---|---|
| (content) | str/dict | URL string or config dict | Required |

**Image content structure:**
```python
{
    'url': str,          # Image URL
    'alt': str,          # Alt text (optional)
    'title': str,        # Title attribute (optional)
    'width': str,        # Width attribute (optional)
    'height': str        # Height attribute (optional)
}
```

### html_block

| Parameter | Type | Description | Default |
|---|---|---|---|
| (content dict) | dict | HTML configuration | {} |

**HTML content structure:**
```python
{
    'tag': str,          # HTML tag name
    'attributes': dict,  # HTML attributes (optional)
    'content': str       # Inner content
}
```

### css_block

| Parameter | Type | Description | Default |
|---|---|---|---|
| (content dict) | dict | CSS configuration | {} |

**CSS content structure:**
```python
{
    'selector': str,     # CSS selector
    'styles': dict       # Style properties
}
```

### svg_animation

| Parameter | Type | Description | Default |
|---|---|---|---|
| (content dict) | dict | SVG configuration | {} |

**SVG content structure:**
```python
{
    'width': int,        # SVG width
    'height': int,       # SVG height
    'elements': list     # SVG elements with animations
}
```

## Content Type Requirements

| Formatter | Content Type | Required Structure |
|---|---|---|
| text | str | Plain text |
| header | str | Plain text |
| table | list[dict] | List of row dictionaries |
| advanced_table | dict | {'headers': list, 'rows': list, 'alignment': list} |
| bullets | list[str] | List of bullet points |
| ordered_list | list[str] | List of items |
| unordered_list | list[str] | List of items |
| code_block | str | Code content |
| blockquote | str/list[str] | Quote content |
| alert | str/list[str] | Alert message(s) |
| collapsible | list[str] | Collapsible content items |
| footnotes | tuple | (text, {id: footnote}) |
| definition_list | dict | {term: definition} |
| task_list | list[dict] | [{'task': str, 'completed': bool}] |
| link_collection | list | Mixed URLs and link objects |
| image | str/dict | URL or configuration dict |
| badge | dict | Badge configuration |
| html_block | dict | HTML configuration |
| css_block | dict | CSS configuration |
| svg_animation | dict | SVG configuration |
| flex_layout | list[dict] | Layout block configurations |
| table_layout | list[dict] | Layout block configurations |
| grid_layout | list[dict] | Layout block configurations |
| horizontal_rule | any | Content above the rule |
| divider | str | Optional content (optional) |

## Layout Block Structure

For flex_layout, table_layout, grid_layout:

```python
{
    'type': str,         # Formatter type
    'header': str,       # Block header
    'content': any,      # Content for the formatter
    'style': str,        # CSS styles for block (optional)
    'kwargs': dict       # Formatter-specific kwargs (optional)
}
```

## Configuration Constants

| Constant | Value | Description |
|---|---|---|
| CACHE_FLUSH_INTERVAL | 30 | Auto-flush interval (seconds) |
| CACHE_FLUSH_COUNT | 1000 | Auto-flush threshold (calls) |
| DOC_FILE_PREFIX | "DOC.PRINT" | Default file prefix |
| DOC_FILE_EXTENSION | ".md" | Default file extension |
| DEFAULT_OUTPUT_DIR | "." | Default output directory |

## Dependencies

### Core Dependencies
- `regex>=2025.9.1` (fallback: standard `re`)
- `xxhash>=3.5.0` (fallback: `hashlib.md5`)

### Performance Dependencies
- `ujson>=5.11.0` (GitHub API operations)
- `orjson>=3.11.3` (fastest JSON when available)

### GitHub Integration
- Uses urllib from standard library
- Zero overhead when disabled
- Fallback JSON handling maintains compatibility

## Error Handling

| Function | Exception | Condition |
|---|---|---|
| docPrintFile | ValueError | Invalid filename characters |
| enableGitCommits | ValueError | Invalid token or repo access |
| enableGitCommits | ImportError | GitHub integration unavailable |

## Thread Safety

All functions are protected by RLock for concurrent access:
- Cache operations
- File handling
- Content matching
- GitHub sync operations
- File switching

- [README.md](https://github.com/Varietyz/DocPrint/blob/main/README.md)
- [Formats.md](https://github.com/Varietyz/DocPrint/blob/main/Formats.md) - Complete formatter documentation with examples
