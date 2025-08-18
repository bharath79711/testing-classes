import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple command-line calculator")

    # Positional arguments
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")

    # Optional argument for operation
    parser.add_argument(
        "--operation",
        choices=["add", "subtract", "multiply", "divide"],
        default="add",
        help="Operation to perform (default: add)"
    )

    args = parser.parse_args()

    # Perform calculation
    if args.operation == "add":
        result = args.num1 + args.num2
    elif args.operation == "subtract":
        result = args.num1 - args.num2
    elif args.operation == "multiply":
        result = args.num1 * args.num2
    elif args.operation == "divide":
        if args.num2 == 0:
            print("Error: Division by zero")
            return
        result = args.num1 / args.num2

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
