custom_dic = {
    "name": "Elshad",
    "age": 28,
    "city": None
}

keys_deleted = []
for key, value in custom_dic.items():
    if value == None:
        keys_deleted.append(key)

for item in range(0, len(keys_deleted)):
    custom_dic.pop(keys_deleted[item])

print(custom_dic)
