max = 20
numbers = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
n = 2520 # Ans divisible from 1-10
switch = 0
#while switch == 0:
while not multiples(n, numbers):
    n += 2520


def multiples(n, numbs) : bool
for x in numbs:
    if (n % x) != 0:
        return False    


print("""
TASK: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
""")
print(n)
