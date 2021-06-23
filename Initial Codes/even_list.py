'''
The file contains a function which would generate a new list with only
even elements in it and print it.
'''
import sys

def even_num_list(List):
    '''
    This function generates a new list with
    even elements in it from the given list.
    '''
    new_list = list()    # An empty new list for appending even no.

    for i in List:

        try:
            if i%2 ==0:
                # If the element is even, then it will be appended.
                new_list.append(i)

        except TypeError as e:
            print('Please ensure that all the elements are integers in the list.')
            sys.exit()

        except Exception as e:
            print(e)
            sys.exit()

    print(new_list)


# Testing of the above function :-

even_num_list([1,2,3,4,5,'kskdk'])
