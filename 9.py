"""
Write a program that asks the user to enter two strings of the same length. The
program should then check to see if the strings are of the same length. If they are not,
the program should print an appropriate message and exit. If they are of the same length, the program should alternate the characters of the two strings. For example, if
the user enters abcde and ABCDE the program should print out AaBbCcDdEe
"""
print("Both Strings Could be Equal")
str1=input("Enter String 1:")
str2=input("Enter String 2:")
if len(str1)!=len(str2):
    print("Two Strings Not Equal")
else:
    for i in range(len(str1)):
        print(str1[i],str2[i],end="")
