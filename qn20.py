# 20. Write a Python program to count the number of strings where the string 
# length is 2 or more and the first and last character are same from a given list of 
# strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221'] 
# Expected Result : 2 


list_one= ['abc', 'xyz', 'aba', '1221']
count=0
for item in list_one:
    if str(item[0])==str(item[-1]):
        count=count+1
    
print(count)
