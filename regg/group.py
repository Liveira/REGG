# -*- coding utf-8 -*-
"""
MIT License

Copyright (c) 2021 Liveira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from regg.utils import utils
data = ['*','+','^','.','[',']','(',')','-','|']
class Group:
    def __init__(self,regex: str):
        self.regex = regex
    def one_word(self,word:str,multiply: str=None) -> None:
        '''
        One World
        ------------
        Add a one world to group
        
        Arguments:
        `word` -> Word
        `multiply` -> Filter, example: multiply = regg.utils.one_or_more | '+', for more info, read the docs!

        
        returns `None`
        '''
        self.regex += '[' + word + ']' + multiply if multiply != None else ""
    def many_words(self,words:str,multiply:str=None) -> None:
        '''Many Worlds
        ------------
        Add a many worlds to group
        
        Arguments:
        `words` -> Words
        `multiply` -> Filter, example: multiply = regg.utils.one_or_more | '+', for more info, read the docs!

        returns `None`'''
        string = ""
        for i in words:
            if i in data:
                string += '\\'+ i
            else:
                string += i
        self.regex += string + multiply if multiply != None else ""
    