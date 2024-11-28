
import argparse

def kalkulator(args):

    if args.operation == "addition" :
        result = args.number1 + args.number2
        print(f"result = {args.number1} + {args.number2} = {result}")

    elif args.operation == "substraction":
        result = args.number1 - args.number2
        print(f"result = {args.number1} - {args.number2} = {result}")

    elif args.operation == "multiplication":
        result = args.number1 * args.number2 
        print(f"result = {args.number1} * {args.number2} = {result}")

    elif args.operation == "division":
        if args.number2 == 0:
            return ValueError
        else:
            result = args.number1 / args.number2
            print(f"result = {args.number1} / {args.number2} = {result}")
    else:
        print("Wrong operation" )

if __name__ == "__main__":

    parser =  argparse.ArgumentParser(description= "Welcome in Kalkulator")

    parser.add_argument("Operation", type=str, choices=["addition", "substraction", "multiplication", "division"], 
        help="Operation witch you prefer to use (addition, substraction, multiplication, division)")

    parser.add_argument("number1", type=float, help= "frist number")
    parser.add_argument("number2", type=float, help= "second number")

    args = parser.parse_args()

    kalkulator(args)

