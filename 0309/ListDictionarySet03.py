text = "Hello, world!"

mydict = {}

for char in text:
    if char not in mydict:
        mydict[char] = 1
    else:
        mydict[char] = mydict[char] + 1
print(mydict)