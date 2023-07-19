#creating a Dictionary

my_dict = {'key1':'value1',
           'key2':'value2',
           'key3':'value3'}

my_other_dict = dict()

print(my_dict['key1'])

print(len(my_dict))

my_dict_person={'name':'John',
                'age': 25,
                'courses':['Math','CompSci'],
                'phone': {'home': {'area_code': 123,},
                            'work': 7654321}
}

print(my_dict_person['courses'])
print(my_dict_person['courses'][0])
print(my_dict_person['phone']['home']['area_code'])


#adding a new key

my_dict_person['address'] = '123 Main St'

print(my_dict_person)

#updating a key

my_dict_person['courses'].append('Art')

print(my_dict_person)

#deleting a key

del my_dict_person['age']

print(my_dict_person)

#pop a key

my_dict_person.pop('address')

print(my_dict_person)

#pop an item

my_dict_person.popitem()

print(my_dict_person)

#check if a key exists

print('name' in my_dict_person)

#looping through a dictionary

for key in my_dict_person:
    print(key)

for key in my_dict_person.keys():
    print(key)

for value in my_dict_person.values():
    print(value)

for key, value in my_dict_person.items():
    print(key, value)


#copying a dictionary

my_dict_person_copy = my_dict_person.copy()

print(my_dict_person_copy)


#merging two dictionaries

my_dict_person_copy.update(my_dict)

print(my_dict_person_copy)

#clearing a dictionary

my_dict_person_copy.clear()

print(my_dict_person_copy)

#creating a dictionary with a list comprehension

my_dict_person_copy = {key:value for key, value in my_dict_person.items() if key != 'phone'}

print(my_dict_person_copy)




