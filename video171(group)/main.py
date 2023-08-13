custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]

custom_dictionary = {}

for item in custom_list:
    if type(item) == int:
        if "int" in custom_dictionary:
            custom_dictionary["int"].append(item)
        else:
            custom_dictionary["int"] = [item]
    if type(item) == str:
        if "str" in custom_dictionary:
            custom_dictionary["str"].append(item)
        else:
            custom_dictionary["str"] = [item]

print(custom_dictionary)
