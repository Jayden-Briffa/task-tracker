class Validator:
    def isInt(val):
        try:
            int(val)
            return True
        
        except ValueError:
            return False
        
    def isEmpty(val):
        return val == ""