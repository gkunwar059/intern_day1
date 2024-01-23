# 2. Write a Python program to get a string made of the first 2 and the last 2 chars 
# from a given a string. If the string length is less than 2, return instead of the 
# empty string. 
# Sample String : 'Python' 
# Expected Result : 'Pyon' 
# Sample String : 'Py' 
# Expected Result : 'PyPy' 
# Sample String : ' w' 
# Expected Result : Empty String 


def string_name(str):
    if len(str)<2:
        return ' '
    
    return str[0:2]+str[-2:]

print(string_name('python'))
