course = 'python for Beginners'
#where a function is part of an object we refer to it as a method

print(course.upper()) #upper method is used to convert a string into uppercase

topic = 'VARIABLES'
print(topic.lower()) #lower method is used to convert a string into lowercase

#.find method helps find if a string has a certain chacter or a sequence of characters

variable = 'integer'
print(variable.find('e'))

#can find a sequence of xters
variable = 'integer one'
print(variable.find('one'))

#.replace method helps replace something in a string with something else
integer = 'integers are numbers'
print(integer.replace('are', 'r'))

#in operator is a special keyword and returns a boolean value

bensoli = "junior developer"
print('developer' in bensoli)