# 10. Write a Python program to remove the characters which have odd index 
# values of a given string.

string =input("Enter the charater")
new_string=''
for index,value in enumerate(string):
    if index%2==0:
        new_string=new_string+value
        
print(new_string)