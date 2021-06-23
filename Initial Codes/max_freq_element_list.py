''' A Python program to find the most common element of a given list'''

def frequency_of_list_members(list): # Overall Time Complexity :- O(len(list)) or O(n)
    '''
    This function returns the tuple with information of highest frequency word.
    '''
    count = dict()

    for word in list:    # Time complexity of the loop :- O(len(list)) or O(number of words in the list) or O(n)
      count[word] = 0

    for word in list:   # Time complexity of the loop :- O(len(list)) or O(number of words in the list) or O(n)
      if count[word] == 0:
        count[word] =1
      else:
        count[word] += 1

    largest = 0
    most_freq = None
    for key,value in count.items():  # Time complexity of the loop :- O(number of elements in the dictionary)
        if value>largest:
            largest = value
            most_freq = key
        else:
            pass

     a = (largest, most_freq)

     return '{} is the tuple with information of the highest frequency word.'.format(a)

# Above function is a Linear Time Procedure for finding the maximum frequency word in a list.
