class Validator:
    def isInt(val) -> bool:
        try:
            int(val)
            return True
        
        except ValueError:
            return False
        
    def isEmpty(val) -> bool:
        return val == ""