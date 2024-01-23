
# 8. Write a Python program to remove the nth index character from a nonempty 
# string.

def remove_char(str,n):
    
    first=str[:n]
    
    second=str[n+1:]
    
    return first+second

print(remove_char('python',0))
print(remove_char('python',2))
print(remove_char('python',3))
