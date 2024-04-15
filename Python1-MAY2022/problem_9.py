for z in range(2, 1000):
    for y in range(2, 1000):
        x = 1000 - z - y
        if x ** 2 + y ** 2 == z ** 2:
            print(x * y * z)


print("TASK: Pythag triplet for a + b + c = 1000")
print(x * y * z)
