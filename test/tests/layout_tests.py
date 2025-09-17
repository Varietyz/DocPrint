from pathlib import Path
from docprint import docPrint, flush_cache

class LayoutTest:
    def run(self):
        self._test_layout_functionality()
    
    def _test_layout_functionality(self):
        print("Testing layout functionality...")
        
        layout_content = [
            {
                'type': 'table',
                'header': 'Performance Metrics',
                'content': [
                    {'metric': 'response_time', 'value': '48ms'},
                    {'metric': 'throughput', 'value': '1350rps'}
                ]
            },
            {
                'type': 'alert',
                'header': 'Status',
                'content': 'System not operational',
                'kwargs': {'alert_type': 'warning'}
            }
        ]
        
        docPrint('flex_layout', 'Dashboard', layout_content, 
                container_style='display: flex; gap: 30px; align-items: flex-start;')
        
        flex_content = [
            {
                'type': 'table',
                'header': 'Server Stats',
                'content': [
                    {'metric': 'CPU', 'value': '45%'},
                    {'metric': 'Memory', 'value': '2.1GB'},
                    {'metric': 'Disk', 'value': '68%'}
                ]
            },
            {
                'type': 'alert',
                'header': 'System Status',
                'content': 'All systems operational',
                'kwargs': {'alert_type': 'success'}
            }
        ]
        
        docPrint('flex_layout', 'Server Dashboard', flex_content)
        
        table_content = [
            {
                'type': 'code_block',
                'header': 'Python Code',
                'content': 'def hello():\n    return "world"',
                'kwargs': {'language': 'python'}
            },
            {
                'type': 'bullets',
                'header': 'Features',
                'content': ['Fast execution', 'Low memory', 'Type safe']
            },
            {
                'type': 'text',
                'header': 'Notes',
                'content': 'Production ready implementation'
            }
        ]
        
        docPrint('table_layout', 'Code Review', table_content)
        
        grid_content = [
            {
                'type': 'badge',
                'header': 'Build Status',
                'content': {
                    'label': 'build',
                    'message': 'passing',
                    'color': 'green'
                }
            },
            {
                'type': 'image',
                'header': 'Architecture',
                'content': {
                    'url': 'https://via.placeholder.com/200x100',
                    'alt': 'System Architecture',
                    'width': '200'
                }
            },
            {
                'type': 'ordered_list',
                'header': 'Deployment Steps',
                'content': ['Build docker image', 'Run tests', 'Deploy to staging', 'Deploy to production']
            },
            {
                'type': 'collapsible',
                'header': 'Debug Info',
                'content': 'Detailed logging information here',
                'kwargs': {'summary': 'View Debug Details'}
            }
        ]
        
        docPrint('grid_layout', 'Project Overview', grid_content, columns=2, gap='15px')
        
        mixed_content = [
            {
                'type': 'advanced_table',
                'header': 'Performance Metrics',
                'content': {
                    'headers': ['Endpoint', 'Response Time', 'Status'],
                    'rows': [
                        ['/api/users', '45ms', '200'],
                        ['/api/orders', '78ms', '200'],
                        ['/api/products', '23ms', '200']
                    ],
                    'alignment': ['left', 'center', 'center']
                }
            },
            {
                'type': 'html_block',
                'header': 'Custom Widget',
                'content': {
                    'tag': 'div',
                    'attributes': {'class': 'widget', 'id': 'stats-widget'},
                    'content': '<p>Custom HTML content here</p><button>Action</button>'
                }
            }
        ]
        
        docPrint('flex_layout', 'API Dashboard', mixed_content, 
                container_style='display: flex; gap: 25px; align-items: flex-start;')
        
        three_col_content = [
            {
                'type': 'alert',
                'header': 'Warnings',
                'content': ['High memory usage', 'Disk space low'],
                'kwargs': {'alert_type': 'warning'}
            },
            {
                'type': 'task_list',
                'header': 'Todo Items',
                'content': [
                    {'task': 'Update dependencies', 'completed': True},
                    {'task': 'Write unit tests', 'completed': False},
                    {'task': 'Deploy to staging', 'completed': False}
                ]
            },
            {
                'type': 'link_collection',
                'header': 'Resources',
                'content': [
                    {'url': 'https://docs.python.org', 'text': 'Python Docs', 'description': 'Official documentation'},
                    {'url': 'https://github.com/project', 'text': 'GitHub Repo', 'description': 'Source code'}
                ]
            }
        ]
        
        docPrint('grid_layout', 'Development Status', three_col_content, columns=3, gap='20px')
        
        styled_content = [
            {
                'type': 'blockquote',
                'header': 'Quote of the Day',
                'content': 'Code is like humor. When you have to explain it, it\'s bad.'
            },
            {
                'type': 'definition_list',
                'header': 'Terms',
                'content': {
                    'API': 'Application Programming Interface',
                    'REST': 'Representational State Transfer',
                    'JSON': 'JavaScript Object Notation'
                }
            }
        ]
        
        docPrint('table_layout', 'Daily Brief', styled_content,
                table_style='width: 100%; border: 2px solid #ccc; border-radius: 8px;')
        
        flush_cache()
        
        content = Path('DOC.PRINT.md').read_text(encoding='utf-8')
        layout_indicators = [
            '<div style="display: flex',
            '<table style=',
            '<div style="display: grid'
        ]
        
        for indicator in layout_indicators:
            if indicator not in content:
                raise AssertionError(f"Missing layout element: {indicator}")
        
        print("  Layout functionality works")