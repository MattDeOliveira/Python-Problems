field = range(100, 1000)
big_drome = None    #biggest palindrome

for i in field:
    for j in field:
        ans = i * j
        if str(ans) == str(ans)[::-1]: # all items in string to be reversed and compared
            if ans > big_drome:
                big_drome = ans


print("""
TASK: A palindromic number reads the same both ways. The largest palindrome made from the
product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.\n\n\
""")
print(big_drome)
