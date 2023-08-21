my_string = input("Enter message translate pig? ")
vowels = ['a', 'e', 'i', 'o', 'u']


def pig_latin(mystring):
    my_tuple = tuple(mystring.split(" "))
    for word in my_tuple:
        if word[0].lower() in vowels:
            print(word.capitalize()+"yay", end=' ')
        else:
            print(word[1:].capitalize() + word[0] + 'ay', end=' ')


pig_latin(my_string)
