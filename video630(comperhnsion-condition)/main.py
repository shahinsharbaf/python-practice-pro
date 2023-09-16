pre_list = [-1, 10, -20, 2, -90, 60, 45]

new_list = [item for item in pre_list if item > 0]

print(new_list)


sentence = "my name is elshad"


def is_consonant(my_letter):
    vowels = "aeiou"
    if (my_letter in vowels):
        return True
    return False


my_sentence = [letter for letter in sentence if is_consonant(letter) == False]


print(my_sentence)
