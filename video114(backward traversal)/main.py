my_string = input("Enter string? ")
lenght_string = len(my_string)

while (lenght_string > 0):
    print(my_string[lenght_string-1])
    lenght_string -= 1
