
# 37. Write a Python program to multiply all the items in a dictionary. 
student={'name':10,'age':4,'location':5}

# store value
result=1

# for loop
for key in student:
    result=result*student[key]

print(result)