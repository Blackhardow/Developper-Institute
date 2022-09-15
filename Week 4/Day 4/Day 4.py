def say_hello():  # """A function that says hello"""
    print("Hello!")
say_hello()

def say_hello1(username):
    print("Hello "+username)

say_hello1("Rick") # "Rick" is an argument
# output "Hello Rick"

say_hello1("Morty") # "Morty" is an argument
# output "Hello Morty
# 
def say_hello(username, language):
    if language == "EN":
        print("Hello "+username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)
say_hello("Rick", "FR")

def say_hello3(username, language="EN"):
    if language == "EN":
        print("Hello "+username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)

say_hello3("Rick")
# OR
say_hello3(username="Rick")

def number_by_three(name, day):
  sentence = 'Hello {}! Today is {}.'.format(name, day)
  print(sentence)

print(day)

name = 'Avner'

def say_hi():
  print(name)

say_hi()

