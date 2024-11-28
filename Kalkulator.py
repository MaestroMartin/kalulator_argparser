import math
import argparse


choice1 = float(input("Enter your number: "))

operations = input("enter your operations => /, *, -, + = :")

choice2 = float(input("Enter your second number: "))

def result():
    if "+" in operations:
        print(choice1 + choice2)
        next
    else:
        if "-" in operations:
            print(choice1 - choice2)
            next 
        else:
            if "*" in operations:
                print(choice1 * choice2)
                next
            else:
                if "/" in operations:
                    choice1 and choice2 != 0
                    breakpoint
                    print("you dont division by 0")
                else:
                    print(choice1 / choice2)

result()

