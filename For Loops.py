#iterate over a list and access each item individually
numbers = [1,2,3,4,5]
for item in numbers:
    print(item)

#the while loop version of it is too long
i=0
while i<len(numbers):
    print(numbers[i])
    i+=1