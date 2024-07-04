#You might want to convert the value of avariable from one type to another

birth_year = input("Enter your birth year: ") #the input function will return a value so we can store it a variable called birth_year

#code to calculate age of user
#currently its 2024

#replace the string birth_year with int(birth_year) to make it an integer
age = 2024 - int(birth_year)
print(age)

#got a bug after after running the code since birth-year is being returned as a string yet you can't subtract an integer from a string.
#so convert the birth_year from string to integer

#FLOAT function will convert a number to a decimal point number
float()
bool()  #convert value to a boolean
str() #convert value to a string