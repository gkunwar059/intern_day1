
# 5. Write a Python program to add 'ing' at the end of a given string (length should 
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the 
# string length of the given string is less than 3, leave it unchanged. 
# Sample String : 'abc' 
# Expected Result : 'abcing' 
# Sample String : 'string' 
# Expected Result : 'stringly' 


string=input("Enter the string")
if len(string) <3:
    print(string)
    exit()
if string[-3:]=="ing":
    new_string=string+"ly"
else:
    new_string=string+"ing"

print(new_string)
