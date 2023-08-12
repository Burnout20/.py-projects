

import random

print("How are you Welcome to a Simple Beta Test of a Python app")
name = input("Please Input Your Name : ")
age = int(input("Please Input Your Age : "))

a = random.randint(1,200)

if age <= 16:
    print("Too young to Beta Test ")
elif age > 100:
    print("Dude ???")
else:
    print("You are eligible For a Beta Test")
    print("Here is your User Number ", a )



