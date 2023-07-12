"""
This module will perform the basic functionalities of typing library
"""
from typing import Optional, Union
   #return income tax amount if the user income is larger then 100000
def return_optional_value(user_income: int)-> Optional[float]:
    """
    This function take  a user_income as int  and return 
    (10%) income tax amount if the user income is larger then 100000
    ----------
    user_income: int 
        user income
    Return
    
        return a value if the user income is greater then 100000 
        otherwise return None
    """
    if user_income < 100000:
        return None
    return user_income*0.2

    #Take the two values as input and rturn its quotient
def division(numerator: Union[int, float], denominator: Union[int, float] )-> Union[int, float]:
    """
    This finction will take the two values as input and rturn its quotient 
    as int or float value
    ----------
    numerator: Union[int, float] 
        numerator value
    denominator: Union[int. float]
        denominator value
    Return
    
        return a value of quotienta s int or float
    """
    try:
        return numerator/denominator
    except ZeroDivisionError as exc:
        raise exc
