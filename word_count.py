import argparse

def word_count(sentence):
    words =sentence.split()
    for word in words:
        print("word:",word)

    print("total words:",len(words))

if __name__ == "__main__":

      parser = argparse.ArgumentParser(description="count of words in sentence")
      parser.add_argument("--sentence",help="Enter a sentence")

      args = parser.parse_args()

word_count(args.sentence)

