import math
import argparse


def addition(number1,number2):
    return number1 + number2

def substraction(number1,number2):
    return number1 - number2 

def multiplication(number1,number2):
    return number1 * number2

def division(number1,number2):
    if number2 != 0:
        return number1 /number2
    else:
        return ValueError

def kalkulator():
    print("Velcome in Kalkulator, please choose number: ")
    print("1 = addition ")
    print("2 = substraction")
    print("3 = multiplication")
    print("4 = division")

    try: 
        number1 = float(input("enter your first number: "))
        choose = int(input())
        number2 = float(input("enter your second number: "))

        if choose == 1:
            print( f"result is {addition(number1,number2)}")

        if choose == 2:
            print( f"result is {substraction(number1,number2)}")

        if choose == 3:
            print( f"result is {multiplication(number1,number2)}")  

        if choose == 4:
             print( f"result is {division(number1,number2)}")

    except  ValueError:
        print("EROR: entered values not right numbers")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

kalkulator()
