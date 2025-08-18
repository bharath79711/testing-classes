def multi(x,y):
    return x*y
print(multi(10,3))

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def is_even(x):
    return x % 2 == 0

def is_odd(x):
    return x % 2 != 0

def revstr(s):
    return s[::-1]
print(revstr("python"))

def get_max_value(listseq):
    return max(listseq)
print(get_max_value([1,2,3,4,5,6,7,8,9]))


def vowel_count(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
print(vowel_count("bangalore is great city"))

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

print(merge_dicts({"a":1, "b":2}, {"a":1, "b":4, "c":3}))


