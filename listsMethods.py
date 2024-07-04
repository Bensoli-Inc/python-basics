#declare a list of numbers
numbers = [1,2,3,4,5]
numbers.append(6) #adds a new number at the end of the list
print(numbers)

#insert method will add a number at the middle of start of the list
numbers.insert(0, -1)
print(numbers)

#remove method
numbers.remove(3)
print(numbers)

#in operator to search if an item appears in the list- returns boolean
print(1 in numbers)

#length function- to normal total number of items in list
print(len(numbers))

#clear method- removes all itmes in the list
numbers.clear()
print(numbers)