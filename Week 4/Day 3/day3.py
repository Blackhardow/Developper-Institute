# # a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

# # print(a_dict.items())

# # # The items() method returns a view object that displays 
# # # a list of dictionary's (key, value) tuple pairs.


# # for key, value in a_dict.items():
# #     print(key, '->', value)
# #     break

# import random


# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# # print(sample_dict['class']['student']['marks']['history'])
# # sample_dict['class']['student']['marks']['history'] = 'SANCHEZ'
# # print(sample_dict['class']['student']['marks']['history'])
# # del sample_dict['class']['student']['name']
# # print(sample_dict)
# # Acceder à un dictionnaire
# # print(sample_dict['class'].keys())
# # print(sample_dict.values())
# #  print(sample_dict.items())

# sample_dict1 = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }

# del sample_dict1['name']
# del sample_dict1['salary']

# print(sample_dict1)

# #  SUPRESSION DES ELEMENTS DU DIC
# # sample_dict.clear()
# # print(sample_dict, 'kbjbjbjbjb')
# # BOUCLES AVANCE
# print(list(range(1, 10, 2)))

# for item in enumerate('abcd'):
#     print(item)

# for (letter, index_count) in enumerate('abcd'):
#     print('At index {} the letter is {}'.format(letter, index_count))

# list1 = [1,2,3]
# list2 = ['a','b','c']
# list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

# for it in zip(list1, list2, list3): # only go as far it is possible
    
#     print(it)

#     tip = list(it)

#     random.shuffle(tip)

#     print('valeur aleatoir',tip)

#     for letter in 'Leonardo':
#         if letter == 'a':
#             break
#         print(letter, end='') # end='' renders each letter next to the other
rick_dict = {
    'first_name':'Rick',
    'last_name':'Sanchez'
}
print(rick_dict.keys())