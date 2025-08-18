import argparse

def func(username,password,age):

    if int(age)>18:
        print("logged to the server")
        age_sq=int(age)*2
        print(f"{username} is username")
        print(f"{password} is password")
        print(f"{age} is age")
        return username,password,age_sq
    else:
        return "check the age above 18"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='User validation')
    
    parser.add_argument('-u','--username',help='username')
    parser.add_argument('-p','--password',help='password')
    parser.add_argument('-a','--age',help='age')
    args = parser.parse_args()
    print(func(args.username,args.password,args.age))
