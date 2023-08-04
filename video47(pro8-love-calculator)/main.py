name = input("Enter you name? ").lower()
love = input("Enter you love name? ").lower()

count_of_true = name.count('t')+love.count('t')+name.count('r')+love.count(
    'r')+name.count('u')+love.count('u')+name.count('e')+love.count('e')
count_of_love = name.count('l')+love.count('l')+name.count('o')+love.count(
    'o')+name.count('v')+love.count('v')+name.count('e')+love.count('e')

print(count_of_love, count_of_love)
