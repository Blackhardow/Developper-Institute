# list1 = [5, 10, 15, 20, 25, 50, 20]
# for i in list1 :
#     if i == 20 :
#         list1.index[i] == 200

# print(list1)
# a_tuple = (10, 20, 30, 40)
# a, b, c, d = a_tuple
# print(a)
# print(b)
# print(c)
# print(d)
# this_set = {"banana", "apple", "cherry", "apple"}
# print(this_set)
# mul = ''
# while True :
#     num = input("Enter a number")
#     if type(num) != int :
#         num = input("Enter a number not a caractere")
#     else:
#         for i in range(1, 13):
#             mul = mul + i
#             print(mul)
# integer_1 = 100
# integer_2 = 50

# # various operations on integers
# print (integer_1*integer_2)
# print (integer_1+integer_2)
# print (integer_1-integer_2)
# print (integer_1/integer_2)

# fruits = ["Apple", "Banana", "Kiwi", "Mango"]

# # various len functions
# print (len(fruits))
# fruits.append("Melon")
# fruits.remove("Apple")
# print (fruits)

# my_car =    {
#   "brand": "Suzuki",
#   "model": "Mehran",
#   "year": 2001
# }

# # indexing the dict
# print("The brand of my car is ", my_car["brand"]) 

# Dayly challenge

# liste1 = [2,3,4,3,10,3,5,6,3]
# elm_count = liste1.count(3)
# print('Le nombre de l’élément : 3 est ', elm_count)


# def trouver_dups(liste1):
#     dups = set()

# for el in liste1:
#     if liste1.count(el)>1:
#         dups.add(el)  
#         return dups

# print(trouver_dups([1, 1, 1, 2, 2, 3]))
# print(trouver_dups(["Alice", "Bob", "Alice"]))
# print(trouver_dups([1, 2, 3]))
# xp ninja 4

# text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

# text_lis = text.split(" ")  
# print(text_lis)   

# for i in text_lis :
#     coun = text_lis.count(i)
#     print("l'occurence de l'element ",i , "est de ", coun," fois")
#     continue

# dayly challenge 1

us = int(input(' entrer un nombre '))
len = int(input(' entrer une longueur '))

user_fin = [i*us for i in range(1,len+1)]
print (user_fin)
   
     



    

