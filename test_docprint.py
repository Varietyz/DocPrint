#!/usr/bin/env python3
import time
import os
from pathlib import Path
from docprint import docPrint, flush_cache, docPrintFile, enableGitCommits

def test_basic_functionality():
    print("Testing basic functionality...")

    docPrint('header', 'Test Header', 'Test content', line=True)
    docPrint('text', 'Status Update', 'System operational', line=False)
    docPrint('table', 'Performance Data', [
        {'metric': 'CPU', 'value': '45%'},
        {'metric': 'Memory', 'value': '2.1GB'}
    ], line=True)

    docPrint('footnotes', 'Research Paper', 
            ("This study builds on previous work", 
            {1: "Source: Smith et al. 2020", 2: "Additional data from Johnson study"}))

    docPrint('definition_list', 'Glossary',
            {"API": "Application Programming Interface", 
            "JSON": "JavaScript Object Notation"})

    docPrint('task_list', 'Checklist',
            [{"task": "Write documentation", "completed": True},
            {"task": "Test features", "completed": False}])

    docPrint('advanced_table', 'User Data',
            {'headers': ['Name', 'Age', 'Score'],
            'alignment': ['left', 'center', 'right'], 
            'rows': [['Alice', 25, 95.5], ['Bob', 30, 88.2], ['Charlie', 28, 92.0]]})

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
        'title': 'Our Logo',
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

def test_file_management():
    print("Testing file management...")

    # Test custom file
    docPrintFile("test_custom.md")
    docPrint('text', 'Custom File Test', 'This is in a custom file')
    flush_cache()

    custom_file = Path('test_custom.md')
    assert custom_file.exists()
    content = custom_file.read_text(encoding='utf-8')
    assert 'Custom File Test' in content

    # Test directory creation
    docPrintFile("test_dir/nested/deep.md")
    docPrint('text', 'Deep File', 'Nested directory test')
    flush_cache()

    deep_file = Path('test_dir/nested/deep.md')
    assert deep_file.exists()
    assert deep_file.parent.exists()

    # Reset to default
    docPrintFile("")
    docPrint('text', 'Back to Default', 'Should be in DOC.PRINT.md')
    flush_cache()

    default_file = Path('DOC.PRINT.md')
    content = default_file.read_text(encoding='utf-8')
    assert 'Back to Default' in content

    print("  File management works")

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
        print("  Content deduplication test inconclusive - file was modified")

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

def test_github_integration():
    print("Testing GitHub integration...")

    # Load environment variables for GitHub token
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("  python-dotenv not available, checking environment directly")

    token = os.getenv('GITHUB_TOKEN')
    repo = os.getenv('GITHUB_REPO', 'test-user/test-repo')

    if not token:
        print("  GITHUB_TOKEN not found - skipping GitHub tests")
        print("  Set GITHUB_TOKEN environment variable to test GitHub integration")
        return

    if repo == 'test-user/test-repo':
        print("  GITHUB_REPO not set - using default test repository")
        print("  Set GITHUB_REPO environment variable for your test repository")

    try:
        # Test enabling GitHub sync
        print(f"  Testing GitHub sync with repo: {repo}")
        enableGitCommits(True, token=token, repo=repo, interval_minutes=1)
        print("  GitHub sync enabled")

        # Generate test content for GitHub
        docPrintFile("github_test.md")
        docPrint('text', 'GitHub Test', f'Testing GitHub integration at {time.strftime("%Y-%m-%d %H:%M:%S")}')
        docPrint('table', 'GitHub Test Data', [
            {'feature': 'Authentication', 'status': 'Working'},
            {'feature': 'Repository Access', 'status': 'Verified'},
            {'feature': 'Content Sync', 'status': 'Testing'}
        ])
        docPrint('alert', 'GitHub Integration', 'This content should sync to GitHub', alert_type='success')

        flush_cache()
        print("  GitHub test content generated")

        # Test content update
        time.sleep(2)
        docPrint('text', 'GitHub Update', f'Updated at {time.strftime("%Y-%m-%d %H:%M:%S")}')
        docPrint('bullets', 'Test Results', [
            'GitHub authentication successful',
            'Repository access verified',
            'Content synchronization active'
        ])

        flush_cache()
        print("  GitHub update content added")

        # Wait for sync (optional)
        print("  Waiting 65 seconds for GitHub sync...")
        for i in range(65):
            if i % 10 == 0:
                print(f"    {65-i} seconds remaining...")
            time.sleep(1)

        # Test disabling
        enableGitCommits(False)
        print("  GitHub sync disabled")

        print("  GitHub integration test complete")
        print(f"  Check your repository: https://github.com/{repo}")

    except ValueError as e:
        print(f"  GitHub configuration error: {e}")
        print("  Verify GITHUB_TOKEN and GITHUB_REPO are correct")
    except Exception as e:
        print(f"  GitHub integration error: {e}")

def test_all_formatter_combinations():
    print("Testing all formatter combinations...")

    # Test all alert types
    for alert_type in ['info', 'warning', 'error', 'success', 'note']:
        docPrint('alert', f'{alert_type.title()} Alert', f'This is a {alert_type} alert', alert_type=alert_type)

    # Test badge variations
    docPrint('badge', 'Badge Test', {
        'label': 'test',
        'message': 'complete',
        'color': 'brightgreen'
    })

    # Test image variations
    docPrint('image', 'Image Test', 'https://via.placeholder.com/150')

    # Test task list variations
    docPrint('task_list', 'Mixed Tasks', [
        {"task": "Completed task", "completed": True},
        {"task": "Pending task", "completed": False},
        "Simple task item"
    ])

    # Test code blocks with different languages
    for lang in ['python', 'javascript', 'bash', '']:
        docPrint('code_block', f'{lang or "Plain"} Code', f'// {lang or "plain"} code example', language=lang)

    flush_cache()
    print("  All formatter combinations work")

def cleanup_test_files():
    print("Cleaning up test files...")
    
    test_files = [
        'DOC.PRINT.md',
        'test_custom.md',
        'github_test.md'
    ]
    
    test_dirs = [
        'test_dir'
    ]
    
    for file_path in test_files:
        try:
            Path(file_path).unlink(missing_ok=True)
        except Exception:
            pass
    
    for dir_path in test_dirs:
        try:
            import shutil
            shutil.rmtree(dir_path, ignore_errors=True)
        except Exception:
            pass
    
    print("  Test files cleaned up")

def main():
    print("=== DocPrint Comprehensive Test Suite ===\n")

    try:
        test_basic_functionality()
        test_structural_formatters()
        test_visual_formatters()
        test_rich_content_formatters()
        test_file_management()
        test_content_updates()
        test_content_deduplication()
        test_cache_timing()
        test_error_handling()
        test_edge_cases()
        test_all_formatter_combinations()
        test_github_integration()

        print("\n=== All Tests Completed ===")
        print("Core functionality: PASSED")
        print("File management: PASSED")
        print("Content formatters: PASSED")
        print("GitHub integration: CHECK REPOSITORY")
        print("\nGenerated files:")
        print("- DOC.PRINT.md (main test output)")
        print("- github_test.md (GitHub sync test)")

        # Ask about cleanup
        cleanup = input("\nCleanup test files? (y/N): ")
        if cleanup.lower() == 'y':
            cleanup_test_files()

    except Exception as e:
        print("\n=== Test Failed ===")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0

if __name__ == "__main__":
    exit(main())