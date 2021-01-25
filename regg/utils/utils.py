one_or_more = "+"
zero_or_more = "*"
any_word = "\w"
everything_without_spaces = "\w\d\D\W/"
everything = "\w\d\D\W\s"
space = "\s"
ng = "\w\d\D\W\s"
def _range(self,start,end):
    return "{"+start+","+end+"}"
__data__=[
    "+","*","\w","\w\d\D\W/","w\d\D\W\s","\s","\w\d\D\W\s"
]