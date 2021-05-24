target = 20
x = 1
switch = False #answer found

while True:
    for i in range(1, target+1): #1 - 20
        if x % i != 0: # number found is not evenly divisible
            break
        if i == target: # target divisible by 'i'
            switch = True
    if switch: # breaks once answer is found
        break
    x += 1 # adds 1 until answer is found
#print(x)



print("""
TASK: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
""")
print(x)
