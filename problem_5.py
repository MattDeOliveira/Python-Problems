#numbers = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

def Find_multiples(n, x):
    for i in range(1, x):
        if x % i != 0:
            return False   # NOT multiple
        return True # multiple of every number

def factorial(x):
    if x > 1:
        x * factorial(x - 1)
        return x
    elif x >= 0:
        return 1
    else:
        return -1 #does not exist

def smallest_positive_number(x):
    for i in range(x, factorial(x) + 1, x):
        if Find_multiples(i, x):
            return i
        return -1

print(smallest_positive_number(20))


print("""
TASK: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
""")
