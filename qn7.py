# 7. Write a Python function that takes a list of words and returns the length of the 
# longest one. 


def get_method(words:list):
    max_num=0
    for word in words:
        if len(word)>max_num:
            max_num=len(word)
            
    print(max_num)
    
get_method(["hello","Hey","woeeeeeee"])