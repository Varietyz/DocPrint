import sys

class ErrorReporter:
    @staticmethod
    def report_error(context, error, fallback_action=None):
        error_msg = f"{context}: {error}"
        print(error_msg, file=sys.stderr)
        
        if fallback_action:
            try:
                return fallback_action()
            except Exception as fallback_error:
                fallback_msg = f"{context} fallback failed: {fallback_error}"
                print(fallback_msg, file=sys.stderr)
        
        return None

    @staticmethod
    def report_file_error(operation, path, error, fallback_action=None):
        context = f"File {operation} error ({path})"
        return ErrorReporter.report_error(context, error, fallback_action)

    @staticmethod
    def report_network_error(operation, url, error, fallback_action=None):
        context = f"Network {operation} error ({url})"
        return ErrorReporter.report_error(context, error, fallback_action)