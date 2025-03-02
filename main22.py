l=[2,4,6,8,10,12,14,16,18,20,1]
i=0
smallest=l[i]
for i in range (len(l)):
    if l[i]<smallest:
        smallest=l[i]
print("smallest no. is",smallest)


# Adding a feature to find the largest number as well
largest = l[0]
for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]

print("largest no. is", largest)

# Adding a feature to calculate the sum of all numbers
total_sum = sum(l)
print("sum of all numbers is", total_sum)

# Adding a feature to calculate the average of all numbers
average = total_sum / len(l)
print("average of all numbers is", average)
