'''The function below would print if the value passed is positive 
    ,negative or zero.'''

def posi_nega(m):
    
    #A negative number multiplied by -1 would return a positive value.
    if m * -1 > 0:                   
        print("The number is negative")
    
    #A positive number multiplied by -1 would return a negative value.
    elif m * -1 < 0:
        print('The number is positive')
    
    #If the number is neither positive or negative, then it is zero.
    else:
        print("The number is zero")