# 40. Write a Python program to add an item in a tuple. 

fruits=('orange','banana')

# converting tuples into list
new_fruits=list(fruits)
new_fruits.append('apple')

fruits=tuple(new_fruits)
print(fruits)

