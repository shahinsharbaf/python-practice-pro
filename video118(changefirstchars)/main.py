my_string = input("Enter string? ")


def first_last_chars(word):
    if len(word) <= 2:
        return 0
    # return word[0:2] + word[len(word)-2] + word[len(word)-1]
    return word[0:2] + word[-2:]


print(first_last_chars(my_string))
