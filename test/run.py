#!/usr/bin/env python3
import sys
import time

from tests.core_tests import CoreFunctionalityTest
from tests.formatter_tests import FormatterTest
from tests.file_tests import FileManagementTest
from tests.github_tests import GitHubIntegrationTest
from tests.cache_tests import CacheTest
from tests.layout_tests import LayoutTest
from tests.cleanup import TestCleanup

class TestRunner:
    def __init__(self):
        self.tests = [
            CoreFunctionalityTest(),
            FormatterTest(),
            FileManagementTest(),
            CacheTest(),
            LayoutTest(),
            GitHubIntegrationTest()
        ]
        self.cleanup = TestCleanup()
        self.results = {}
    
    def run_all_tests(self):
        print("=== DocPrint Comprehensive Test Suite ===\n")
        
        start_time = time.time()
        passed_tests = 0
        total_tests = len(self.tests)
        
        for test in self.tests:
            try:
                test.run()
                self.results[test.__class__.__name__] = "PASSED"
                passed_tests += 1
                print(f"{test.__class__.__name__}: PASSED")
            except Exception as e:
                self.results[test.__class__.__name__] = f"FAILED: {e}"
                print(f"{test.__class__.__name__}: FAILED - {e}")
        
        end_time = time.time()
        
        self._print_summary(passed_tests, total_tests, end_time - start_time)
        return passed_tests == total_tests
    
    def _print_summary(self, passed, total, duration):
        print("\n=== Test Summary ===")
        print(f"Tests run: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {total - passed}")
        print(f"Duration: {duration:.2f}s")
        
        if passed == total:
            print("\nAll tests completed successfully!")
        else:
            print("\nSome tests failed. Check output above for details.")
        
        print("\nGenerated test files:")
        print("- DOC.PRINT.md (main test output)")
        print("- github_test.md (GitHub sync test)")
        
        self._handle_cleanup()
    
    def _handle_cleanup(self):
        try:
            cleanup = input("\nCleanup test files? (y/N): ")
            if cleanup.lower() == 'y':
                self.cleanup.cleanup_all()
        except KeyboardInterrupt:
            print("\nTest complete.")

def main():
    runner = TestRunner()
    success = runner.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())