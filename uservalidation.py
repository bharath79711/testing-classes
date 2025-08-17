import argparse
def func(username,password,age):
    print(f"{username} is username")
    print(f"{password} is password")
    print(f"{age} is age")
    age_sq=int(age)*2
    return username,password,age_sq


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='User validation')
    parser.add_argument('-u','--username',help='username')
    parser.add_argument('-p','--password',help='password')
    parser.add_argument('-a','--age',help='age')
    args = parser.parse_args()
    print(func(args.username,args.password,args.age))
