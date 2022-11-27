# Python Dictionaries

dict1 = {
    "Name": "Mohsin",
    "Email":"mohsin.afridi91@gmail.com",
    "Phone":123,
    "Colors": ["red", "white", "blue"] 
}

print(dict1)
print("Type is ",type(dict1))
print("Length is ",len(dict1))

new_dic  = dict(name = "John", age = 36, country = "Norway")
print(new_dic["name"])
new_dic["country"] = "Pakistan"
new_dic["color"] = "red"
print(new_dic.keys())
new_dic.pop("color")
print(new_dic.items())