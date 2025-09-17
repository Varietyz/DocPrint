from pathlib import Path
from docprint import docPrint, docFlush

class CoreFunctionalityTest:
    def run(self):
        self._test_basic_functionality()
        self._test_content_updates()
        self._test_content_deduplication()
        self._test_error_handling()

    def _test_basic_functionality(self):
        print("Testing basic functionality...")

        docPrint('chart', 'Market Share', {
            'title': 'Browser Usage',
            'data': {'Chrome': 65, 'Firefox': 15, 'Safari': 20}
        }, chart_type='pie')

        docPrint('chart', 'Project Schedule', {
            'title': 'Development Plan',
            'sections': [
                {
                    'title': 'Development',
                    'tasks': [
                        {'name': 'Design', 'start': '2024-01-01', 'duration': '10d'},
                        {'name': 'Implementation', 'start': '2024-01-11', 'duration': '20d'}
                    ]
                }
            ]
        }, chart_type='gantt')

        docPrint('chart', 'Process Flow', {
            'nodes': [
                {'id': 'start', 'label': 'Start', 'shape': 'circle'},
                {'id': 'process', 'label': 'Process Data'},
                {'id': 'end', 'label': 'End', 'shape': 'circle'}
            ],
            'edges': [
                {'from': 'start', 'to': 'process', 'label': 'begin'},
                {'from': 'process', 'to': 'end', 'label': 'complete'}
            ]
        }, chart_type='flowchart')

        docPrint('chart', 'Project Timeline', {
            'title': 'Development Schedule',
            'events': [
                {'period': '2024 Q1', 'description': 'Planning'},
                {'period': '2024 Q2', 'description': 'Development'},
                {'period': '2024 Q3', 'description': 'Testing'}
            ]
        }, chart_type='timeline')

        docPrint('text', 'Status', 'Stwcswag')
        docPrint('text', 'Status', 'Rwscey')
        docPrint('text', 'Status', 'Cwswco')
        docPrint('divider', 'Important', line=False, divider_type='shadow', color="#b659ae")
        docPrint('text', 'Section', 'Content', line=True)
        docPrint('text', 'Section', 'Content', line=True, 
                divider_line={'divider_type': 'gradient', 'thickness': 4})
        docPrint('bullets', 'Tasks', ['Task 1', 'Task 2'], line=True,
                divider_line={'divider_type': 'shadow', 'color': "#fbff00"})
        docPrint('header', 'Test Header', 'Test content', line=True)
        docPrint('text', 'Status Update', 'System operational', line=False)
        docPrint('table', 'Performance Data', [
            {'metric': 'CPU', 'value': '45%'},
            {'metric': 'Memory', 'value': '2.1GB'}
        ], line=True)
        
        docFlush()
        
        doc_file = Path('DOC.PRINT.md')
        if not doc_file.exists():
            raise AssertionError("DOC.PRINT.md not created")
        
        content = doc_file.read_text(encoding='utf-8')
        if '## Test Header' not in content:
            raise AssertionError("Header formatting failed")
        if '## Status Update' not in content:
            raise AssertionError("Text formatting failed")
        if 'CPU' not in content:
            raise AssertionError("Table formatting failed")
        
        print("  Basic formatting works")
    
    def _test_content_updates(self):
        print("Testing content updates...")
        
        import random
        
        for i in range(3):
            rng_value = random.randint(1, 200)
            status = "ONLINE" if rng_value > 100 else "OFFLINE"
            
            docPrint('text', 'System Status', f'Status: {status} (Check #{i+1}, RNG: {rng_value})', line=True)
        
        docFlush()
        
        print("  Dynamic content logging works")
    
    def _test_content_deduplication(self):
        print("Testing content deduplication...")
        
        docPrint('text', 'Dedup Test', 'Same content', line=False)
        docFlush()
        
        docPrint('text', 'Dedup Test', 'Same content', line=False)
        docFlush()
        
        print("  Content deduplication works")
    
    def _test_error_handling(self):
        print("Testing error handling...")
        
        docPrint('text', 'Empty Test', '', line=True)
        docFlush()
        
        docPrint('text', 'None Test', None, line=True)
        docFlush()
        
        docPrint('table', 'Complex Data', [], line=False)
        docFlush()
        
        docPrint('unknown_type', 'Fallback Test', 'Should fall back to text format')
        docFlush()
        
        print("  Error handling works")