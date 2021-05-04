def prime(x):
    i = 2   #start from bottom
    while i * i <= x:   # allow i to go to deliverable
        if x % i:   # if remainder
            i += 1  #increase i and 1
        else:   #if divison results in whole number
            x //= i     # Floor /// Gets results of x if result is whole number /// Largest stays value x
    return x     #go to top

This_number = 600851475143
prime(This_number)  #call function
ans = prime(This_number)    # answer from prime(x)

print("""
The prime factors of 13195 are 5, 7, 13 and 29.

TASK: What is the largest prime factor of the number 600851475143 ?
      """)

print("Answer: ", ans)
