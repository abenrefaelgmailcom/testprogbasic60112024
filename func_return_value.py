import random

def my_rand_int(a: int, b: int) -> str:
    return 'hello'

#num: int = random.randint(1, 10)
word: str = my_rand_int(1, 10)
word: str = 'hello'
print(word)

def my_sum(x: int, y: int) -> int:
    sum_x_y: int = x + y
    return sum_x_y

z: int = my_sum(3, 7)
print(z)

# write a function that gets a number
#  and returns the number power 3
#  2 power 3 ==    2*2*2 == 8
# 10 power 3 == 10*10*10 == 1000
# 2 ** 3
def my_power(x: int, x_power: int) -> int:
    result: int = x ** x_power
    return result

my_power(5, 3)  # does nothing
power_5_3: int = my_power(5, 3)
print(power_5_3)
print(my_power(5, 3))

# write a function that gets a number and
# returns half of it (as int)
def half(num: int) -> int:
    result: int = num // 2
    return result

half_19: int = half(19)
print(half_19)

print(half(21))

# write a function that gets 2 floats and returns the smaller one
def smaller_float(a: float, b: float) -> float:
    # 1
    # shortcut:
    # return a if a < b else b
    # 2
    # return min(a, b)
    # 3
    if a < b:
        return a
    else:
        return b

print(smaller_float(8.1, 9.2))

# write a function that gets 2 string and returns the longer string
def shorter_str(st1: str, st2: str) -> str:
    # 1
    # shortcut
    # return st1 if len(st1) > len(st2) else st2
    # 2
    if len(st1) > len(st2):
        return st1
    else:
        return st2

# write a function that gets 2 bool and returns True if they are the same otherwise False
def same_bool(bool1: bool, bool2: bool) -> bool:
    # shortcut
    # return bool1 == bool2
    if bool1 == bool2:
        return True
    else:
        return False

# write a function that gets 2 list and returns the longer list
def longer_list(list1: list, list2: list) -> list:
    if len(list1) > len(list2):
        return list1
    else:
        return list2

# write a function that gets a string and returns the reversed string
def reverse_str(word: str) -> str:
    # return word[::-1]
    reversed_word: str =  word[::-1]
    return reversed_word

# write a function that gets a word and a list[word] return true if the word appear in the
#  list otherwise returns false
def word_in_list(list1: list[str], word: str) -> bool:
    if word in list1:
        return True
    else:
        return False

# *Bonus: write a function that gets a word and a list[word] return index of the word
# if it appears in the list otherwise returns None
def index_word(list1: list[str], word: str) -> int | None:
    #if word in list1:
    if word_in_list(list1, word):
        return list1.index(word)
    else:
        return None


















