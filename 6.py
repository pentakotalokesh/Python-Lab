"""
Generate a random number between 1 and 10. Ask the user to guess the number and
print a message based on whether they get it right or not.

"""
import random as r
num=r.randint(1,10)
usernum=int(input("Enter any number:"))
if num==usernum:
    print("Your Guess is Correct")
else:
    print("Your Guess is Wrong")