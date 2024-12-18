class Database:
    # the database implemetation
    def __init__(self):
        pass

    def connect(self):
        print("Connecting to DB")

    
class Formatter:
    def format_string(self, string):
        """Format a string using using the fomatter object, which
        is expected to have a format() method that accepts a string"""
        formatter = None
        class DefaultFomatter:
            def format(self, string):
                return str(string).title()
        
        if not formatter:
            formatter = DefaultFomatter()

        return formatter.format(string)
    