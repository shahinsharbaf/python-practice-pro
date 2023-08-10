my_string = input("Enter string? ")
my_char = input("Enter char? ")


def count_letter(word, letter):
    count = 0
    for charaecter in word:
        if charaecter == letter:
            count += 1
    return count


print(count_letter(my_string, my_char))
