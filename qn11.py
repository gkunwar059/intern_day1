# 11. Write a Python program to count the occurrences of each word in a given 
# sentence.

string=input("Enter the sentence ")
string=string.split(' ')

new_list={}

for word in string:
    if word not in new_list:
        new_list[word]=1
    else:
        new_list[word]+=1
        
print(new_list)
        