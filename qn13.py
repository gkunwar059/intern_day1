# 13. Write a Python program that accepts a comma separated sequence of words 
# as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red,white,black,red,green,black 
# Expected Result : black, green, red, white,red 


sample_string=input("Enter the string")
sample_string=sample_string.split(",")

sample_string.sort()
print(sample_string)

emptylist=[]
emptylist=list(set(sample_string))


emptylist.sort()
print(emptylist)


