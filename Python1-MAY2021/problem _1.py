count, count2  = 0, 0
three_List, five_List = [], []

for i in range(0, 333):
    count += 3
    three_List.append(count)


for i in range(0, 199):     # 1000/5
    count2 += 5
    five_List.append(count2)


big_List = three_List + five_List   #combine list
#print(big_List) # List of all numbers

# index_position = [i for i in range(len(big_List))] #gains index position in list
# print(index_position)

def remove_duplicates(duplist):     # removes duplicates from list, recieves big_list
    no_duplicates = []  # return new list with no duplicates
    for element in duplist:     # every index in list being recieved (big_List)
        if element not in no_duplicates:    #if the element is not already in a list add to new list (no_duplicates)
            no_duplicates.append(element)    #add to list (no_duplicates)

    return no_duplicates

fat_List = remove_duplicates(big_List)  # List that will be returned after recieving Big_List (no_duplicates turned into fat_List)
# print(fat_List) # new big_List --> output of no_duplicates

#print('-*' * 20)

total = 0   #to count entire no_duplicates
next_element = 0    #count every element gone through no_duplicates

while (next_element < len(fat_List)):   # Adding every element  to a sum from the no_duplicates/fat_List
    total = total + fat_List[next_element]
    next_element += 1

print("""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.\nThe sum of these multiples is 23.
\n\nTASK: Find the sum of all the multiples of 3 or 5 below 1000.
      """)
print('-*' * 20)
print("Sum: ", total)
print('-*' * 20)
