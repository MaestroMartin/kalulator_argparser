
import argparse

def kalkulator(args):

    if args.operation == "+" :
        result = args.number1 + args.number2
        print(f"result = {args.number1} + {args.number2} = {result}")

    elif args.operation == "-":
        result = args.number1 - args.number2
        print(f"result = {args.number1} - {args.number2} = {result}")

    elif args.operation == "*":
        result = args.number1 * args.number2 
        print(f"result = {args.number1} * {args.number2} = {result}")

    elif args.operation == "/":
        if args.number2 == 0:
            return ValueError
        else:
            result = args.number1 / args.number2
            print(f"result = {args.number1} / {args.number2} = {result}")
    else:
        print("Wrong operation" )

if __name__ == "__main__":

    parser =  argparse.ArgumentParser(description= "Welcome in Kalkulator")

    parser.add_argument(-'n1','--number1',"number1", type=float, help= "frist number")
    
    parser.add_argument('-o','--operation',"Operation", type=str, choices=["+", "-", "*", "/"], 
        help="Operation witch you prefer to use ( + , - , * , / )")
    
    parser.add_argument('-n2','--number2',"number2", type=float, help= "second number")

    args = parser.parse_args()

    kalkulator(args)

