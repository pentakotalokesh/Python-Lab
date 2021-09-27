"""
Write a program that asks the user to enter three numbers (use three separate input
statements). Create variables called total and average that hold the sum and average of
the three numbers and print out the values of total and average.

"""
num1=int(input("Enter 1st Number:"))
num2=int(input("Enter 2nd Number:"))
num3=int(input("Enter 3rd Number:"))
total=num1+num2+num3
average=total/3
print("The total of Three Numbers is {0}and average is {1}".format(total,average))