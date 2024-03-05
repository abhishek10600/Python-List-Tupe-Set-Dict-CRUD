thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# length of dictionary
print(len(thisdict))

# dictionaries store data as a key value pair. It can be considered as a hashmap.
# Dictionaries are ordered, changeable and do not allow duplicates.

print(thisdict)

# KEY VALUE
print(thisdict["brand"])  # we pass the key and we get the value.


# DICTIONARY ITEMS-DATA TYPES
dict1 = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(dict1)


# dict() constructor
dict2 = dict(name="Abhishek Sharma", age=23, country="India")
print(dict2)


# ACCESSING ITEMS IN A DICT
dict3 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

model_name = dict3["model"]  # printing the value of key model
print(model_name)

# this will return the value of key named speed, if the key doest not exist it will create a key with name speed and assign 233 as the value of key speed.
speed = dict3.get("speed", 233)
print(speed)


# GET THE KEYS
print(dict3.keys())


# UPDATING THE DICTIONARY.

dict4 = {
    "name": "Abhishek Sharma",
    "age": 23,
    "country": "India"
}

print(dict4)

# CREATING A NEW KEY VALUE IN THE DICTIONARY dict4.
dict4["city"] = "Kolkata"
print(dict4)

# UPDATING THE VALUE OF EXISTING KEY VALUE.
dict4["name"] = "Mr. Abhishek Sharma"
print(dict4)

# GET ALL THE VALUES
print(dict4.values())

# it will return the key value pairs of the dictionary as list of tuples container [('key', 'value'),('key', 'value')]
print(dict4.items())


# CHECK IF A KEY EXISTS
dict5 = {
    "name": "Abhishek Sharma",
    "age": 23,
    "country": "India"
}

if "carname" in dict5:
    print("It exists.")
else:
    print("It does not exists.")


# CHANGE VALUES IN A DICTIONARY
dict5 = {
    "name": "Abhishek Sharma",
    "age": 23,
    "country": "India"
}

dict5["age"] = 27
print(dict5)

# we can also do the above operation using update
# it will update existing key value or will create new key value if key does not exists.
dict5.update({"year": 2024})
print(dict5)


# REMOVE VALUES FROM A DICTIONARY
dict6 = {
    "name": "Abhishek Sharma",
    "age": 23,
    "country": "India"
}
print(dict6)
dict6.pop("age")  # it will remove the key and value of key country.
print(dict6)

dict7 = {
    "name": "Abhishek Sharma",
    "age": 23,
    "country": "India"
}
print(dict7)
dict7.popitem()  # it will delete the last inserted key value in dictionary.
print(dict7)

dict8 = {
    "name": "Abhishek Sharma",
    "age": 23,
    "country": "India"
}
print(dict8)
del dict8["name"]  # it will remove the key and value of key country.
print(dict8)


# LOOP THROUGH DICTIONARIES
dict10 = {
    "name": "Abhishek Sharma",
    "age": 23,
    "country": "India"
}

for item in dict10:  # looping through the keys
    print(item)


for item in dict10:  # looping throught the values
    print(dict10[item])


for item in dict10.values():  # another wat to loop through values
    print(item)


for item in dict10.keys():  # looping through keys
    print(item)


for key, value in dict10.items():
    print(key, value)


# COPY DICTIONARY
dict11 = dict10.copy()
print(dict11)

dict12 = dict(dict11)
print(dict12)
