primes_to_find = 10001
x = 2
list_of_primes =[]
while (len(list_of_primes) < primes_to_find):
    if all(x % prime_number for prime_number in list_of_primes): #all must be true
        list_of_primes.append(x)
    x += 1

print('''
TASK: What is the 10 001st prime number?
      ''')
#print(list_of_primes)
print(list_of_primes[-1]) #last item (10001st)
