
# 15. Write a Python function to insert a string in the middle of a string. 
# Sample function and result : 
# insert_sting_middle('[[]]', 'Python') -> [[Python]] 
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}} 


def insert_middle(str,word):
    
    return str[:2] + word + str[2:]
    
    
print(insert_middle('[[]]','Python'))
print(insert_middle('{{}}','PHP'))
