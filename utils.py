import numpy as np

def dollar_formatter(num):
    return '$' + comma(num)


def comma(num):
    '''Add comma to every 3rd digit. Takes int or float and
    returns string.
    @Source: dnaman7, https://stackoverflow.com/questions/5180365/
    python-add-comma-into-number-string'''
    if type(num) == int:
        num = float(num)
    if type(num) == float:
        return '{:,.2f}'.format(num) # Rounds to 2 decimal places
    else:
        raise ValueError("Need int or float as input to function!")
