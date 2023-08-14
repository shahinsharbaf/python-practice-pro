list_items = {
    "computer": {"price": 100, "stock": 10},
    "monitor": {"price": 200, "stock": 10},
    "keyboard": {"price": 300, "stock": 10},
    "mouse": {"price": 400, "stock": 10},
    "hdmi cable": {"price": 500, "stock": 10},
    "dvd drive": {"price": 600, "stock": 10},
}

print("Enter add option from the list? ")

list_items_keys = list(list_items.keys())

for i in range(0, len(list_items_keys)):
    print("%i: %s" % (i+1, list_items_keys[i]))
print("0: to finish ")

sum = 0
while True:
    select_item = int(input("> "))
    if (select_item == 0):
        break
    if (list_items[list_items_keys[select_item-1]
                   ]["stock"] == 0):
        print("%s is out of stock!" % list_items_keys[select_item-1]
              )
    else:
        list_items[list_items_keys[select_item-1]
                   ]["stock"] = list_items[list_items_keys[select_item-1]]["stock"]-1
        sum += list_items[list_items_keys[select_item-1]
                          ]["price"]

print("amount is %i", sum)
print(list_items)
