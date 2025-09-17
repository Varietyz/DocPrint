from pathlib import Path
from docprint import docPrint, docFlush

class FormatterTest:
    def run(self):
        self._test_structural_formatters()
        self._test_visual_formatters()
        self._test_rich_content_formatters()
        self._test_edge_cases()
        self._test_all_formatter_combinations()
    
    def _test_structural_formatters(self):
        print("Testing structural formatters...")
        
        docPrint('bullets', 'Key Points', ['First point', 'Second point', 'Third point'])
        docPrint('horizontal_rule', 'Section Break', 'Content above the line')
        docPrint('code_block', 'Python Code', 'print("Hello World")', language='python')
        docPrint('blockquote', 'Quote', 'This is a quoted text')
        docPrint('ordered_list', 'Steps', ['Step 1', 'Step 2', 'Step 3'])
        docPrint('unordered_list', 'Items', ['Item A', 'Item B', 'Item C'])
        
        docFlush()
        
        content = Path('DOC.PRINT.md').read_text(encoding='utf-8')
        required_elements = [
            '- First point',
            '---',
            '```python',
            '> This is a quoted text',
            '1. Step 1',
            '- Item A'
        ]
        
        for element in required_elements:
            if element not in content:
                raise AssertionError(f"Missing structural element: {element}")
        
        print("  Structural formatters work")
    
    def _test_visual_formatters(self):
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
        
        docFlush()
        
        content = Path('DOC.PRINT.md').read_text(encoding='utf-8')
        required_elements = [
            'shields.io',
            '<div class="highlight"',
            '.highlight {',
            '<svg width="50"'
        ]
        
        for element in required_elements:
            if element not in content:
                raise AssertionError(f"Missing visual element: {element}")
        
        print("  Visual formatters work")
    
    def _test_rich_content_formatters(self):
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
        
        docFlush()
        
        content = Path('DOC.PRINT.md').read_text(encoding='utf-8')
        required_elements = [
            '[WARNING]',
            '[ERROR]',
            '<details>',
            '<summary>Click to expand</summary>',
            '<img src="https://example.com/logo.png"',
            '[GitHub](https://github.com)'
        ]
        
        for element in required_elements:
            if element not in content:
                raise AssertionError(f"Missing rich content element: {element}")
        
        print("  Rich content formatters work")
    
    def _test_edge_cases(self):
        print("Testing edge cases...")
        
        docPrint('badge', 'Simple Badge', 'Just text content')
        docPrint('image', 'Simple Image', 'https://example.com/simple.jpg')
        docPrint('link_collection', 'Simple Links', ['https://example.com', 'https://test.com'])
        docPrint('bullets', 'Single Bullet', 'Just one item')
        
        docFlush()
        
        content = Path('DOC.PRINT.md').read_text(encoding='utf-8')
        required_elements = [
            'Just text content',
            '![Image](https://example.com/simple.jpg)',
            '- Just one item'
        ]
        
        for element in required_elements:
            if element not in content:
                raise AssertionError(f"Missing edge case element: {element}")
        
        print("  Edge cases work")
    
    def _test_all_formatter_combinations(self):
        print("Testing all formatter combinations...")
        
        for alert_type in ['info', 'warning', 'error', 'success', 'note']:
            docPrint('alert', f'{alert_type.title()} Alert', f'This is a {alert_type} alert', alert_type=alert_type)
        
        docPrint('badge', 'Badge Test', {
            'label': 'test',
            'message': 'complete',
            'color': 'brightgreen'
        })
        
        docPrint('badge', 'Python Badge', {
            'label': 'Python',
            'message': '3.9+',
            'color': 'blue',
            'logo': 'python',
            'logo_color': 'white'
        })
        
        docPrint('image', 'Image Test', 'https://via.placeholder.com/150')
        
        docPrint('task_list', 'Mixed Tasks', [
            {"task": "Completed task", "completed": True},
            {"task": "Pending task", "completed": False},
            "Simple task item"
        ])
        
        for lang in ['python', 'javascript', 'bash', '']:
            docPrint('code_block', f'{lang or "Plain"} Code', f'// {lang or "plain"} code example', language=lang)
        
        docFlush()
        print("  All formatter combinations work")