#used to create complex rules/conditions
# #include and, or, not

#and operator returns true only if both are true, and false if any is false
price =25
print(price>10 and price<20) #and operator to check if price is between 10 and 30

#or operator returns true if atleast one condition is true
item =5
print(item>10 or item<30)

#not operator will inverse false to true and vice versa
print(not item>10)