'''This program contains a function that computes the cube-sum of all
    the numbers less than the specified value.
    '''

def cube_sum(m):
    '''
    This function returns the cubic sum of numbers until the entered value.
    '''
    # Since, negative and non-integral values are invalid.
    if m < 0 or isinstance(m, float):
        return print("Please enter a positive integral value :)")
    # Only positive integral values will have the cubic sum computed.
    elif m > 0 and isinstance(m, int):
        a = 0
        for i in range(0,m+1):
            a = a + i*i*i
        return print(a, "is the sum of all the cubes until", m)

    # The Asymptotic Time Complexity of the above function is O(m). 

# Testing of the above function :-

cube_sum(3.4)
cube_sum(-2)
cube_sum(5)
