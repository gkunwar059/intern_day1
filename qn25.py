# 25. Write a Python program to check whether all dictionaries in a list are empty or 
# not. 
# Sample list : [{},{},{}] 
# Return value : True 
# Sample list : [{1,2},{},{}] 
# Return value : False 

sample_list=[{2:3},{},{}] 

for item in sample_list:
    item=dict(item)
    
    if not item:
        continue
    else:
        print("Not Empty") 
        exit()
        
print("empty")   