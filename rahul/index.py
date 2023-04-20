# a=200
# b=33
# if b>a:
#     print("yes, b is > a")
# else:
#     print("no b is < a")
# x=200
# print(bool(x))
string = "Favtutor Blog: How to Remove multiple characters in a string in Python"
print("Original string: ", string)
to_remov = {"t": "T", "l": "L", "r": "R", "s": "S"}
for char in to_remov.keys():
    # dictionaryName[keys] - another way to get value
    string = string.replace(char, to_remov[char])

print("Altered string: " + string)




