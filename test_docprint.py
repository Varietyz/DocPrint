#!/usr/bin/env python3
import time
from pathlib import Path
from docprint import docPrint, flush_cache

def test_basic_functionality():
    print("Testing basic functionality...")

    docPrint('header', 'Test Header', 'Test content', line=True)
    docPrint('text', 'Status Update', 'System operational', line=False)
    docPrint('table', 'Performance Data', [
        {'metric': 'CPU', 'value': '45%'},
        {'metric': 'Memory', 'value': '2.1GB'}
    ], line=True)

    flush_cache()

    doc_file = Path('DOC.PRINT.md')
    if doc_file.exists():
        content = doc_file.read_text(encoding='utf-8')
        assert '## Test Header' in content
        assert '## Status Update' in content
        assert '## Performance Data' in content
        assert 'CPU' in content
        print("  Basic formatting works")
    else:
        raise AssertionError("DOC.PRINT.md not created")

def test_structural_formatters():
    print("Testing structural formatters...")

    docPrint('bullets', 'Key Points', ['First point', 'Second point', 'Third point'])
    docPrint('horizontal_rule', 'Section Break', 'Content above the line')
    docPrint('code_block', 'Python Code', 'print("Hello World")', language='python')
    docPrint('blockquote', 'Quote', 'This is a quoted text')
    docPrint('ordered_list', 'Steps', ['Step 1', 'Step 2', 'Step 3'])
    docPrint('unordered_list', 'Items', ['Item A', 'Item B', 'Item C'])

    flush_cache()

    content = Path('DOC.PRINT.md').read_text(encoding='utf-8')
    assert '- First point' in content
    assert '---' in content
    assert '```python' in content
    assert '> This is a quoted text' in content
    assert '1. Step 1' in content
    assert '- Item A' in content
    print("  Structural formatters work")

def test_visual_formatters():
    print("Testing visual formatters...")

    docPrint('badge', 'Build Status', {
        'label': 'build',
        'message': 'passing',
        'color': 'green',
        'style': 'flat',
        'url': 'https://github.com/test'
    })

    docPrint('html_block', 'Custom HTML', {
        'tag': 'div',
        'attributes': {'class': 'highlight', 'id': 'test-div'},
        'content': 'This is custom HTML content'
    })

    docPrint('css_block', 'Styling', {
        'selector': '.highlight',
        'styles': {
            'background-color': 'yellow',
            'padding': '10px',
            'border-radius': '5px'
        }
    })

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

    flush_cache()

    content = Path('DOC.PRINT.md').read_text(encoding='utf-8')
    assert 'shields.io' in content
    assert '<div class="highlight"' in content
    assert '.highlight {' in content
    assert '<svg width="50"' in content
    print("  Visual formatters work")

def test_rich_content_formatters():
    print("Testing rich content formatters...")

    docPrint('alert', 'Warning Message', 'This is a warning alert', alert_type='warning')
    docPrint('alert', 'Error Details', ['Error code: 404', 'File not found', 'Check path'], alert_type='error')

    docPrint('collapsible', 'Detailed Info', 'This content is collapsible', summary='Click to expand')

    docPrint('image', 'Project Logo', {
        'url': 'https://example.com/logo.png',
        'alt': 'Project Logo',
        'title': 'Our Amazing Logo',
        'width': '200',
        'height': '100'
    })

    docPrint('link_collection', 'Useful Links', [
        {'url': 'https://github.com', 'text': 'GitHub', 'description': 'Code repository'},
        {'url': 'https://docs.python.org', 'text': 'Python Docs', 'description': 'Official documentation'}
    ])

    flush_cache()

    content = Path('DOC.PRINT.md').read_text(encoding='utf-8')
    assert '[WARNING]' in content
    assert '[ERROR]' in content
    assert '<details>' in content
    assert '<summary>Click to expand</summary>' in content
    assert '<img src="https://example.com/logo.png"' in content
    assert '[GitHub](https://github.com)' in content
    print("  Rich content formatters work")

def test_content_updates():
    print("Testing content updates...")

    docPrint('header', 'Update Test', 'Initial content', line=True)
    flush_cache()

    docPrint('header', 'Update Test', 'Updated content', line=True)
    flush_cache()

    content = Path('DOC.PRINT.md').read_text(encoding='utf-8')
    assert 'Updated content' in content
    assert 'Initial content' not in content
    print("  Content updates work")

def test_content_deduplication():
    print("Testing content deduplication...")

    docPrint('text', 'Dedup Test', 'Same content', line=False)
    flush_cache()

    doc_file = Path('DOC.PRINT.md')
    initial_mtime = doc_file.stat().st_mtime

    time.sleep(0.1)

    docPrint('text', 'Dedup Test', 'Same content', line=False)
    flush_cache()

    new_mtime = doc_file.stat().st_mtime
    if initial_mtime == new_mtime:
        print("  Content deduplication works")
    else:
        print("  Content deduplication test failed - file was modified")

def test_cache_timing():
    print("Testing cache timing...")

    from docprint.config import constants
    original_interval = constants.CACHE_FLUSH_INTERVAL
    original_count = constants.CACHE_FLUSH_COUNT
    constants.CACHE_FLUSH_INTERVAL = 2
    constants.CACHE_FLUSH_COUNT = 999

    flush_cache()
    docPrint('text', 'Timed Entry', 'Should auto-flush after 2 seconds', line=True)
    time.sleep(4)

    constants.CACHE_FLUSH_INTERVAL = original_interval
    constants.CACHE_FLUSH_COUNT = original_count

    doc_file = Path('DOC.PRINT.md')
    if doc_file.exists():
        content = doc_file.read_text(encoding='utf-8')
        if 'Timed Entry' in content:
            print("  Auto-flush timing works")
        else:
            print("  Auto-flush timing test failed")
    else:
        print("  Auto-flush timing test failed - no file created")

def test_error_handling():
    print("Testing error handling...")

    docPrint('text', 'Empty Test', '', line=True)
    flush_cache()

    docPrint('text', 'None Test', None, line=True)
    flush_cache()

    docPrint('table', 'Complex Data', [], line=False)
    flush_cache()

    docPrint('unknown_type', 'Fallback Test', 'Should fall back to text format')
    flush_cache()

    print("  Error handling works")

def test_edge_cases():
    print("Testing edge cases...")

    docPrint('badge', 'Simple Badge', 'Just text content')
    docPrint('image', 'Simple Image', 'https://example.com/simple.jpg')
    docPrint('link_collection', 'Simple Links', ['https://example.com', 'https://test.com'])
    docPrint('bullets', 'Single Bullet', 'Just one item')

    flush_cache()

    content = Path('DOC.PRINT.md').read_text(encoding='utf-8')
    assert 'Just text content' in content
    assert '![Image](https://example.com/simple.jpg)' in content
    assert '- Just one item' in content
    print("  Edge cases work")

def cleanup_files():
    print("Cleaning up test files...")
    doc_file = Path('DOC.PRINT.md')
    if doc_file.exists():
        doc_file.unlink()
        print("  Removed DOC.PRINT.md")

def main():
    print("=== DocPrint Optimized Test Suite ===\n")

    cleanup_files()

    try:
        test_basic_functionality()
        test_structural_formatters()
        test_visual_formatters()
        test_rich_content_formatters()
        test_content_updates()
        test_content_deduplication()
        test_cache_timing()
        test_error_handling()
        test_edge_cases()

        print("\n=== All Tests Completed ===")
        print("Check DOC.PRINT.md file for generated content")

    except Exception as e:
        print("\n=== Test Failed ===")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0

if __name__ == "__main__":
    exit(main())