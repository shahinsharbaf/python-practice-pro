import random

letters = "abcdefghijklmnopqrstuyxwzABCDEFGHIJKLMNOPQRSTUYXZ"
numbers = "0123456789"
symbols = "!@#$%^&*"
try:
    letters_count = int(
        input("How many leeters do you want to use in password? "))
    numbers_count = int(
        input("How many numbers do you want to use in password? "))
    symbols_count = int(
        input("How many symbols do you want to use in password? "))
except:
    print("not valid")
else:
    password_length = letters_count + numbers_count + symbols_count
    password = ""
    while password_length > 0:
        random_character = random.randint(1, 3)
        if random_character == 1 and letters_count != 0:
            rnd = random.randint(0, 51)
            password += letters[rnd]
            password_length -= 1
            letters_count -= 1
            continue
        if random_character == 2 and numbers_count != 0:
            rnd = random.randint(0, 9)
            password += numbers[rnd]
            password_length -= 1
            numbers_count -= 1
            continue
        if random_character == 3 and symbols_count != 0:
            rnd = random.randint(0, 7)
            password += symbols[rnd]
            password_length -= 1
            symbols_count -= 1
            continue
    print(password)
