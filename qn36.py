# 36. Write a Python program to sum all the items in a dictionary. 

data_list={'ram':34, 'laxman':43,'harish':56}

sum=0

for key in data_list:
    sum=sum+data_list[key]
    
print(sum)