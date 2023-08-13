names_dict = {
    1: 'Elshad',
    2: "Renad",
    3: "Joanna",
    4: "Appmilers"
}


def value_length(my_dictinary):
    new_dictinary = {}
    for key, value in my_dictinary.items():
        new_dictinary[key] = {value: len(value)}
    return new_dictinary


print(value_length(names_dict))

print(names_dict.values())
