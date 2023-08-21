number = int(input("Enter number? "))

my_set_div3 = set()
my_set_div4 = set()

my_set_div3 = set(range(3, number+1, 3))
my_set_div4 = set(range(4, number+1, 4))

print(my_set_div3.intersection(my_set_div4))
