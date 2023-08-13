my_string = input("Enter a str? ")


def count_chars(my_string):
    count_chars_dictionary = {}
    for my_char in my_string:
        if my_char in count_chars_dictionary:
            count_chars_dictionary[my_char] += 1
        else:
            count_chars_dictionary[my_char] = 1
    return (count_chars_dictionary)


print(count_chars(my_string))
