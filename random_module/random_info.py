import random

'''
In this particular application of random module, we will 
use it to generate bogus data/info of some number of people.
'random' as a module has functions such as 'uniform()',
'randint()', 'choice()', 'choices()', 'sample()'.
'''

first_name = ['John','Kaman','Hardikbhai', 'Mark', 'Yuvi', 'Ricky', 'Brett', 'Colin', 'Mihirbhai', 'Digantbhai', 'Sahilbhai']

last_name = ['Patel', 'Bush', 'Lee', 'Ponting', 'Johnson', 'Goradia', 'Warne', 'Zhu']

street_names = ['Brooke Park Drive', 'Bellwood Rd', 'Canterburry Drive', 'Sherwood Circle', 'Main St.', 'Shreeji Rd', \
    'Purshottam Drive', 'State Park Rd']

city_name = ['Canton', 'Romulus', 'Livonia', 'Plymouth', 'Novi', 'Dearborn', 'Ann Arbor', 'Westland']

state_name = ['NJ', 'IL', 'MI', 'CA', 'AZ', 'PA', 'OH', 'IN', 'NC', 'SC']



for i in range(10):

    f_name = random.choice(first_name)
    print(f_name, end = ' ')

    l_name = random.choice(last_name)
    print(l_name+',')

    print(random.randint(4562,8965), end = ' ')

    print(random.choice(street_names)+',')

    print(random.choice(city_name), end = ' ')

    print(random.choice(state_name), end = '-')

    print(random.randint(41632, 95632))

    print()
