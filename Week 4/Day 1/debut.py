#dayly challenge
from ntpath import join
import random




# strin = input(" Entrez un mot de 10 caractère ")
# if len(strin) < 10 :
#     print('string not long enough ')
# elif len(strin) > 10 :
#     print('string too long')
# else :
#     print(strin[0], strin[len(strin)-1])

# altern = ""
    
# for i in strin :
   
#     altern = altern + i
#     print(altern)

# alice = list(strin)
# print(alice)
# random.shuffle(alice)
# print(alice)
# mm = ''.join(alice)
# print(mm)




# from webbrowser import Konqueror


# number = int(input('Entrez un nombre entre 1 et 100 '))
# if number >= 1 and number <= 100 :
#     if number % 3 == 0 :
#         if (number % 5 == 0) :
#              print('FIZZ-BUZZ')
#         else :
#             print('FIZZ')
#     elif number % 5 == 0:
#         print('BUZZ')
#     else:
#         print("Votre nombre n'est pas modulable ")
    

    

# else:
#     print("Votre nombre n'est pas dans l'interval requis")



# Example 1
#if 3 > 4:  print('something is fishy...')
#elif 3 <= 4:
#  print('3 is not equal to 4, but it is lower than 4')
#else:
#  print('4 is actually greater than 3')

# Example 2
#name = input('Please state your name: ')

#if name == 'Frank':
 # print('You are Frank Sinatra')
#elif name == 'Miles':
 # print('You are Miles Davis')
#elif name == 'Tony':
 # print('You are Tony Benett')
#else:
 # print('I do not know who you are!')
  

#XP NINJA 5 
# while True:
#     sentence = input('Enter the longest sentence whitout A !!! ')
#     if 'A' in sentence:
#         print(sentence) 
#         continue             
#     else:
#         print("Congrat pericka")
#     break
#XP NINJA 5

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit? sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,  sunt in culpa qui officia deserunt mollit anim id est laborum."
alo = "p a"
print(len(alo))
alo_list = list(alo)
newalo = "" + join(alo_list)
print(newalo)