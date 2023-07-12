"""
This module is designed for iterators practice
"""
class ClassIterator:
    """
    Iterater practice using __iter__ and __next__ magic methods

    Attributes
    ----------
    num: int
        number for increment

    Methods
    -------
    None
    """
    #Class Constructor
    def __init__(self, num):
        self.num=num

    # Iterator over the class
    def __iter__(self):
        return self
    #next method perform next to next iteartion over class object
    def __next__(self):
        iterator_output=self.num+1
        return iterator_output
