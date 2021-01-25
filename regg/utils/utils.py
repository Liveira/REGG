class utils:
    def __init__(self):
        self.one_or_more = "+"
        self.zero_or_more = "*"
        self.any_word = "\w"
        self.everything_without_spaces = "\w\d\D\W/"
        self.everything = "\w\d\D\W\s"
        self.space = "\s"
    def _range(self,start,end):
        return "{"+start+","+end+"}"
    
