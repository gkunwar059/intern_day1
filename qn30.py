# 30. Write a Python script to check whether a given key already exists in a 
# dictionary. 
# dictonaries
d={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 
13: 169, 14: 196, 15: 225} 

# d[x] dictonaries

def check_dic(x):
    if x in d:
        print("Already exists")
    else:
        print("Okey not exists")
        
check_dic(4)
check_dic(300)