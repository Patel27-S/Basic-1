'''
File contains a function that checks whether a passed string is in lowercase/
uppercase or otherwise.
'''

def check_low_up(string):
    '''
    This function returns 'True' if the passed string is in lowercase
    or uppercase, all letters including. And, 'False' otherwise.
    '''
    # The Boolean value 'True' or 'False' is returned.
    return string == string.lower() or string == string.upper()
