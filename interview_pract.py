#-------Reverse String------
"""
text=input("Enter the text: ")
# rev_str=text[::-1]
# print("rev_str:",rev_str)
# z=text.split()
# rev_str=" ".join(z[::-1])
# print(rev_str)
reversed_string="".join(reversed(text))

print(reversed_string)
"""

"""
#-------Max num in a list-------
my_list =input("Enter the numbers space separated: ")
nums=[int(x) for x in my_list.split() ]  
print(max(nums))
print(min(nums))
"""
"""
num= int(input("Enter a number: "))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
          print(f"{num}: is not a prime number")
          break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

"""
"""
sentence=input("Enter the sentence: ")
count=0
for char in sentence:
    if char in "aeiouAEIOU":
        count=count+1
print("vowel_count:",count)
"""
"""

numbers=input("Enter the numbers: ")
x=[int(i)for i in numbers.split()]
print(x)
n=len(x)+1
exp_sum=n*(n+1)//2
actual_sum=sum(x)
missing_num=exp_sum-actual_sum
print(missing_num)

"""
"""

input=[1,2,3,4,4,5]
unique_list=[]
for i in input:
    if i not in unique_list:
        unique_list.append(i)

print("unique_list:",unique_list)        
"""
"""
text="banana"
frequency_char={}
for char in text:
    if char in frequency_char:
        frequency_char[char]=frequency_char[char]+1
    else:
        frequency_char[char]=1

print("frequency_char:",frequency_char)

"""
"""
str1="listen"
str2="silent"
if sorted(str1) == sorted(str2):
    print(True)
else:
    print(False)

"""
"""
x=[10,5,8,20,3]
x.sort()
print("second largest num:",x[-2])
"""
"""
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"{n}:factorial is {fact}")
"""

"""
n=6
for i in range(1,11):
    print(f"{n}X{i}={n*i}")
"""
"""
text="aabbcdeff"
freq={}
for char in text:
    if char in freq:
        freq[char]=freq[char]+1
    else:
        freq[char]=1

for char in text:
    if freq[char]==1:
        print(char)
"""
"""
x=[1,2,3,4,5]
y=x[-1:-3:-1]
print(y)
for num in x:
    if num < 4:
        y.append(num)
print(y)
"""
"""
x=[1,2,3,4,]
y=[3,4,5,6]
set1=set(x)
set2=set(y)
resu=set1.intersection(set2)
print(list(resu))

"""
"""
nums=[1,2,3,2,4,5,1,6,1]
x=[]
y=[]
for num in nums:
    if num not in x:
        x.append(num)
    else:
        y.append(num)
print("Duplicates of lis :",set(y))  
"""

"""
s = "Bharath Kumar Talari"

vowel_replace={'a':'1','A':'1','e':'2','E':'2','i':'3','I':'3','o':'4','O':'4','u':'5','U':'5'}

replace =""

for char in s:
    if char in vowel_replace:
        replace=replace+vowel_replace[char]

    else:
        replace=replace+char

print("replaced vowels is:",replace)

"""
"""
N =123456
result=0
while N>0:
    digit = N%10
    result=result*10+digit
    N=N//10
print(result)
"""
"""
x=[1,2,3,7,8,9,4,5]
x.sort()
print(x)
x.sort(reverse=True)
print(x)
y=sorted(x)
print(y)
"""
"""
x=10
def fun(x,y):
    global x

    return x+y
y=fun(x,10)
print(y)

"""
"""
x=[1,2,3,4,5,[6,7,8,9],10,11]
flat=[]
for num in x:
    if type(num)==list:
        flat.extend(num)

    else:
        flat.append(num)
print(flat)
"""
"""
s="abc@tu$xyz"
chars=list(s)

letters=[char for char in chars if char.isalpha()]
letters.reverse()
#letters.insert(3,"@"),letters.insert(6,"$")
print(letters)
j=0
for i in range(len(chars)):
    if chars[i].isalpha():
        chars[i]=letters[j]
        j=j+1
    result="".join(chars)
print(result)

 #rev=letters[::-1]
#print(rev)

"""

"""


x="Engineering"
def vowel_count(strr):
    result=""
    count=0
    vowels="aeiouAEIOU"
    for char in strr:
        if char in vowels:
            count=count+1
            result=result+char*count
        else:
            result=result+char
    return result
print(vowel_count(x))

"""
"""
x="MY NAME IS BHARATH KUMAR TALARI"

def freq_char(strr):
    freq={}
    for char in strr:
        if char ==" ":
            continue
        if char in freq:
            freq[char]=freq[char]+1
        else:
            freq[char]=1
    return freq
print(freq_char(x))
"""
"""
x="Engineering"
def vowel_count(strr):
    result=""
    count=0
    vowels="aeiouAEIOU"
    for char in strr:
        if char in vowels:
            count=count+1
            result=result+char*count
        else:
            result=result+char
    return result
print(vowel_count(x))

"""
"""
list_num=[5,3,8,3,1,5,9,1]

uniq_num =[]#[5,3,8,1,9]   1,3,8,5,9  1 3 5 8 9

for num in list_num:
    if num not in uniq_num:
        uniq_num.append(num)

print("uniq_nums:",uniq_num)
# x=len(uniq_num)
# print(x)


for i in range (len(uniq_num)):
    for j in range (i+1,len(uniq_num)):
        if uniq_num[i] > uniq_num[j]:
            uniq_num[i],uniq_num[j] = uniq_num[j],uniq_num[i]
print(uniq_num)

"""
"""
s="abc@tu$xyz"

chars=list(s)

letters=[char for char in chars if char.isalpha()]
letters.reverse()
print(letters)

j=0
for i in range(len(chars)):
    if chars[i].isalpha():
        chars[i]=letters[j]
        j=j+1
        result="".join(chars)
print(result)
"""
"""
N=370
#-------- 1 method-------------------

x=[int(i)for i in str(N)]
power=len(x)
results=0

for i in x:
    results=results+i**power
if results==N:
    print("This is Armstrong Number")
else:
    print("This is Not Armstrong Number")
"""
# 2.method-------------------------
"""
N=(int
   (input("Enter a number:")))
temp=N
N2=str(N)
power=len(N2)

sum =0
while temp>0:
    digit=temp%10
    sum=sum+digit**power
    temp=temp//10
if sum==N:                                           
    print("This is Armstrong Number")
else:
    print("This is Not Armstrong Number")
"""
"""
N=123456

result=0

while N>0:
    digit=N%10
    result=result*10+digit
    N=N//10
print(result)

"""

"""
def two_num_sum(nums,target):
    for i in range (len(nums)):
        for j in range (i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

nums= [5,6,7,8,2,1,4]
target=3
print("index of two numbers:",two_num_sum(nums,target))

"""
"""
# ==============2.prime number find out ?==============
N = int(input("Enter a number:"))

if N > 1:
    for i in range(2, N):
        if N % i == 0:
            print(f"{N}:is not a prime number")
            break
    else:
        print(f"{N}:is a prime number")


else:
    print(f"{N}:is  not a prime number")
 """
"""
sentence="Hcl Tech in Bangalore"
#x=sentence.split()
#print(x)
rev =""
for word in sentence.split():
    rev=word+" "+rev
print(rev)
"""
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]

"""
arr=[16,17,4,3,5,2]
leaders=[]

max_val=arr[-1]
leaders.append(max_val)

for i in range(len(arr)-2,-1,-1):
    if arr[i] > max_val:
        leaders.append(arr[i])
        max_val=arr[i]
        leaders.reverse()
print(leaders)
print(leaders[::-1])

"""
"""
def find_leaders(arr):
    leaders = []
    
    for i in range(len(arr)):
        is_leader = True
        
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                is_leader = False
                break
        
        if is_leader:
            leaders.append(arr[i])
     
    return leaders


arr = [16,17,4,3,5,2]
print(find_leaders(arr))
"""
"""
num=int(input("Enter a number:"))
count=0

if num>1:

    for i in range(1,num+1):
        if num % i == 0:
            count = count + 1
    if count==2:
        print(f"{num} is prime")

    else:
        print(f"{num} is not prime")

"""
"""
#num=int(input("Enter a number:"))
def fact(num):
    fact=1
    if num<0:
        return "factorial does not exist for negative numbers"
    elif num==0:
        return 1
    else:
        for i in range(1,num+1):
            fact = fact * i
    return f"{num} factorial is: {fact}"
print(fact(5))

"""
"""
arr=[2,15,6,8,12,22,1]

max=arr[0]
min=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]>max:
        max=arr[i]

    elif arr[i]<min:
        min=arr[i]

print(max)
print(min)

"""
"""
my_list=[23,65,19,90]

print(my_list)
pos1,pos2=1,3
my_list[pos1],my_list[pos2]=my_list[pos2],my_list[pos1]

print(my_list)
"""
"""
my_list=[2,15,65,19,90]
print(my_list)
my_list[1],my_list[3]=my_list[3],my_list[1]

print(my_list)
"""

"""

add=(lambda x,y:(x**2,y**2))(2,4)
print(add)

"""
"""
def my_Decrator(func):
    def wrapper():
        print("Before Decorator")
        func()
        print("After Decorator")
    return wrapper

@my_Decrator
def greet():
    print("Hello Bharath")

greet()



try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except Exception as error:
    print("error:", error)

else:
    print("Calculation successful!")

finally:
    print("Execution completed.")
"""
"""

lst=[1,[2,[3,4,[5,6],7,8],9],10]


flat=[]

for item in lst:
    if type(item) is list:
        for num in item:
            if type(num) is list:
                for i in num:
                    if type(i) is list:
                        flat.extend(i)

                    else:
                        flat.append(i)
            else:
                flat.append(num)
    else:
        flat.append(item)


print(flat)

"""

"""
lst=[1,(2,(3,4,(5,6),7,8),9),10,12,(13,14,15),16]

flat=[]

def flatten(lst):
    for item in lst:
        if isinstance(item, tuple):
            flatten(item)
        else:
            flat.append(item)

flatten(lst)
print(flat)

"""
"""

lst=[1,2,3,[4,5,6],7,8]

flat=[]


def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            flatten(item)

        else:
            flat.append(item)
    return flatten

print(flatten(lst))
"""

"""
lst = [1,[2,3,[4,5],6,7],8]


def itterate_nums(lst):
    for item in lst:
        if isinstance(item, list):
            itterate_nums(item)
        else:
            print(item)


itterate_nums(lst)

for num in range(100, 201):
    if str(num) == str(num)[::-1]:
        print(num)

"""
"""
for num in range (1,1001):
    order=len(str(num))
    temp=num
    total =0

    while temp >0:
        digit=temp%10

        total=total+digit**order
        temp=temp//10

    if num == total:
        print(num)
"""
lst = [1, 2, 3, 6, 7, 9]

lst = [0 if x == 6 else x for x in lst]

print(lst)


lst = [1, 2, 3, 6, 7, 9]

for i in range(len(lst)):
    if lst[i] == 6:
        lst[i] = 0

print(lst)

import re
emails = ["abc@gmail.com", "test@yahoo.com", "hello@gmail.com", "user@outlook.com"]

gmails=[]


for mail in emails:
    if re.fullmatch(r"[\w\.-]+@gmail\.com",mail):
       gmails.append(mail)
print(gmails)


def safe_divide():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
    except ValueError:
        print("Invalid input! Please enter integers only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"Result = {result}")
    finally:
        print("Operation completed.")


safe_divide()

import pandas as pd


def test_read_excel():
    df = pd.read_excel(r"C:\Users\Bharath\Downloads\data.xlsx")

    for i, row in df.iterrows():
        print(row["Name"], row["Age"])