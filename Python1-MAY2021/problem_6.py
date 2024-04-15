sum = 0 # sum of squaring every number
square_sum = 0 # squaring sum

for i in range(1, 101):
    sum += i
    square_sum += i ** 2

sum = sum ** 2 # square total of 100 factorial (addition) sum

diff = sum - square_sum
print('''
     TASK: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
     ''')

print(diff)
