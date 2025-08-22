import argparse

parser = argparse.ArgumentParser(description="count the characters in a sentence")

parser.add_argument("--sentence",help="Enter a sentence")

args = parser.parse_args()

count_chars ={}

for char in args.sentence:
    if char !=" ":
     if char in count_chars:
        count_chars[char] += 1
     else:
        count_chars[char] = 1


if __name__ == "__main__":
    for key,value in count_chars.items():
        print(f"char {key} : {value}")

