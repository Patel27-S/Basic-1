'''The function below would generate new list with only 
even elements in it and print it.'''

def even_num_list(List):
    '''This function generates a new list with 
    even elements in it from the given list.'''
    new_list = list()    # This generates a new_list
    for i in List:
        if i%2 == 0:
            new_list.append(i)    # new_list is appended with even no.
    print(new_list)

