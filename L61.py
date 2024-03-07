#Therese Burns Samantha Patin
def too_long(x):
    if len(x)>140:
        print("message is too long")

y=input("enter message:\n")
too_long(y)


import unicodedata
print(unicodedata.lookup("snake"))
print(unicodedata.lookup("dog"))
print(unicodedata.lookup("rose"))
print(unicodedata.lookup("sun"))
print(unicodedata.lookup("cat"))
print(unicodedata.lookup("two hearts"))

#sentences
sent_1="I saw a snake outside"+unicodedata.lookup("snake")
print(len(sent_1))
print(sent_1)     

sent_2="I like dogs"+unicodedata.lookup("dog")
print(len(sent_2))
print(sent_2)

sent_3="The sun is bright"+unicodedata.lookup("sun")
print(len(sent_3))
print(sent_3)

sent_4="The cat is cute"+unicodedata.lookup("cat")
print(len(sent_4))
print(sent_4)

sent_5="happy valentines day"+unicodedata.lookup("rose")
print(len(sent_5))
print(sent_5)


print(unicodedata.name("&"))
print(unicodedata.name("["))
print(unicodedata.name("/"))
print(unicodedata.name("~"))

