'''This program contains a function that computes the cube-sum of all 
    the numbers less than the specified value.
    '''

def cube_sum(m):
    '''This function returns the cubic sum of numbers until the entered value.'''
    if m < 0 or type(m)==float:  # Since, negative and non-integral values are invalid.
        return print("Please enter a positive integral value :)")
    elif m > 0 and type(m)== int:  # Only positive integral values will have the cubic sum computed.
        a = 0
        for i in range(0,m):
            a = a + i*i*i
        return print(str(a), "is the sum of all the cubes until", str(m-1))