class Validator:
    
    # Return True if the value is an integer
    def isInt(val) -> bool:
        try:
            int(val)
            return True
        
        except ValueError:
            return False
    
    # Return True if the value is an empty string
    def isEmpty(val) -> bool:
        return val == ""