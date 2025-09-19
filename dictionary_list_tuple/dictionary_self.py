my_dict = dict()
print(my_dict)
my_dict2 = {}
print(my_dict2)

eng_sp = dict(one='uno', two='dos', three = 'tres')  #the datatype of the key doesn't have to be specified when using the dict() method
print(eng_sp)

eng_sp2 = {'one':'uno', 'two':'dos', 'three':'tres'} #datatype to be specified, hence '' around one, two and three, since string
print(eng_sp2)

eng_sp_list = [('one','uno'), ('two','dos'), ('three','tres')]
eng_sp3 = dict(eng_sp_list)
print(eng_sp3)


my_dict = {'name':'Mia', 'age': 12}
my_dict['age'] = 15
my_dict['address'] = 'Bangalore'
print(my_dict)

def traverse_dict(dict):
    for key in dict:
        print(key, dict[key])

traverse_dict(my_dict)

def search_dict(dict, val):
    for key in dict:
        if val == dict[key]:
            return key, val
    return ('Not found in dictionary')

ele=search_dict(my_dict, 17)
print(ele)

# del my_dict['age']
# print(my_dict)

# ele_removed = my_dict.pop('name', None) #None is the default value which will be used in case the specified key can't be found in the dictionary
# print(ele_removed)
# print(my_dict)

# ele_removed = my_dict.popitem()   #removes the last key value pair added to the dictionary
# print(ele_removed)
# print(my_dict)

# my_dict.clear()  #Removes all key value pairs from the dictionary and leaves an empty dictionary
# print(my_dict)
# up_dict = {0:2, 3:4}
# my_dict.update(up_dict)
# print(my_dict)
# Dictionary methods

copy_dict = my_dict.copy()
print(my_dict)
print(copy_dict)

# new_dict = {}.fromkeys([1,2,3],4)
# print(new_dict)

# print(my_dict.get('city',30))

print(my_dict.items())
print(my_dict.keys())

print(my_dict.setdefault('name', 'Juhi'))
print(my_dict)

print(my_dict.setdefault('name1', 'Juhi'))
print(my_dict)

print(my_dict.values())

present = "Juhi" in my_dict.values()
print(present)

print(len(my_dict))
print(all(my_dict))

print(any(my_dict))
print(sorted(my_dict))


# Dictionary Comprehension

import random
city_names = ['Paris', 'London', 'Rome', 'Delhi','Madrid']
new_dict = {city : random.randint(20,30) for city in city_names}
print(new_dict)

ref_dict = {'Paris': 'France', 'Delhi':'India', 'Madrid':'Spain'}

ref_dict2 = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}

country_capital = {city : capital for (city, capital) in ref_dict.items() }
if_dict = {num : letter for (num, letter) in ref_dict2.items() if num>2}
print(country_capital)
print(if_dict)







