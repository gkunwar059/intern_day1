
# 14. Write a Python function to create the HTML string with tags around the 
# word(s). 
# Sample function and result : 
# add_tags('i', 'Python') -> '<i>Python</i>' 
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>' 



def tag_function(tag, word):
    return f"<{tag}>{word} <{tag}>"


print(tag_function('i','Python'))
print(tag_function('b','Python Tutorial'))