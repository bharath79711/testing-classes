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




