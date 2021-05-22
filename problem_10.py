primes_to_find_upTo = 2000000 # 2 mill
x = 3
index = 0
list_of_primes = [2]
check_primes = []

while list_of_primes[-1] < primes_to_find_upTo: # until last element less than number looking for
    if all(x % prime for prime in check_primes):
        list_of_primes.append(x)
        if list_of_primes[index] < x ** 0.5 + 1:
            check_primes.append(list_of_primes[index])
            index += 1
    x += 1


#print(list_of_primes)
list_of_primes.pop(-1)
#print(list_of_primes)



print("Find the sum of all the primes below two million.")
print(sum(list_of_primes))
