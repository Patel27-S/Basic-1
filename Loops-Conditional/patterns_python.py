'''
This file contains functions to form different types of star('*')
patterns.
'''


def boxed_stars_pattern():
  '''
  This function prints the boxed star pattern as per 
  number of stars a user enters.
  '''
  try:
    user_input = int(input('Please enter the number of stars in the box : '))
  except:
    print('Please enter a valid entry(i.e. an integral value)')
    exit()
  for i in range(user_input): # i -> 0 to 4
    if i==0 or i ==user_input-1:   # First and Last Iteration.(i.e. * * * * *, i -> 0,4)
      for j in range(user_input):
        print('*', end = ' ')
      print()
    else:              # Middle Iterations. (i.e. *          *, i-> 1,2,3)
      for a in range(user_input): # i -> 0 to 4
        if a == 0 or a==user_input-1:
          print('*', end = ' ')
        else:
          print(' ', end = ' ')
      print()
 


def decreasing_star_pattern():
  '''
  This function prints the decreasing star pattern as per the number of rows input by the user.
  '''
  try:
    user_input = int(input('Please enter the number of rows for decreasing star pattern : '))
  except:
    print('Please enter a valid entry(i.e. an integral value.)')
    exit()
  for j in range(user_input): # j -> from 0 to user_input-1
    a = user_input - j  
    for i in range(a):
      print('*', end = ' ')
    print()

    
    
def increasing_star_pattern():
  '''
  This function prints the increasing star patterns as per the number of rows input by the user.
  '''
  try:
    user_input = int(input('Please enter the number of rows for increasing star pattern : '))
  except:
    print('Please Enter a valid entry(i.e. an integral value)')
    exit()

  for j in range(user_input): # j -> 0 to user_input-1
    a = j + 1  # a -> 1 to user_input
    for i in range(a): 
      print('*', end = ' ')
    print()
    

    
def constant_stars_pattern():
  '''
  This function prints the constant star pattern as per the number of rows input by the user.
  '''
  try:
    user_input = int(input('Please enter the number of rows for constant star pattern : '))
  except:
    print('Please enter a valid entry(i.e. an integral value).')
    exit()
  for j in range(user_input):
    for i in range(5):
      print('*', end = ' ')
    print()    

   
 
