class ValidationUtils:
    INVALID_FILENAME_CHARS = {'<', '>', ':', '"', '|', '?', '*'}
    
    @staticmethod
    def validate_filename(filepath):
        if not filepath or filepath in (".", ".."):
            return False, "Invalid or empty filepath"
        
        invalid_chars = ValidationUtils.INVALID_FILENAME_CHARS.intersection(set(filepath))
        if invalid_chars:
            return False, f"Invalid filename characters: {', '.join(invalid_chars)}"
        
        return True, None
    
    @staticmethod
    def validate_required_params(**params):
        missing = [name for name, value in params.items() if not value]
        if missing:
            return False, f"Missing required parameters: {', '.join(missing)}"
        return True, None