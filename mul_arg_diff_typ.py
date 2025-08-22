import argparse

parser = argparse.ArgumentParser(description="different types of arguments")

parser.add_argument("--name",help="Enter a name")
parser.add_argument("--village",help="Enter a village name")
parser.add_argument("--city",help="Enter a city name")
parser.add_argument("--age",type=int,help="Enter your age")
parser.add_argument("--marks",type=float,help="Enter your Marks")

args = parser.parse_args()
print(f"name: {args.name}")
print(f"village: {args.village}")
print(f"city: {args.city}")
if args.age >= 18:
    print(f"age: {args.age}")
else:
    print("age can't be less than 18")
if args.marks >= 85:
    print("first class")
elif args.marks >= 75:
    print("second class")
elif args.marks >= 60:
    print("third class")
elif args.marks >= 50:
    print("fourth class")
else:
    print("fail")


