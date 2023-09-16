import random


def shuffle(letter_password, nums_password, symbol_password):
    password = ""
    while (len(letter_password)+len(nums_password)+len(symbol_password)) != 0:
        my_rnd = random.randint(0, 3)
        if my_rnd == 0 and len(letter_password) != 0:
            password += letter_password.pop()
        if my_rnd == 1 and len(nums_password) != 0:
            password += nums_password.pop()
        if my_rnd == 2 and len(symbol_password) != 0:
            password += symbol_password.pop()
    return password


def generate_password():
    letters = "abcdefghijklmnopqrstuxwyzABCDEFGHIJKLMNOPQRSTUYWXZ"
    nums = "0123456789"
    symbol = "!@#$%^&*()"

    letter_password = [letters[random.randint(0, 49)] for _ in range(0, 5)]
    nums_password = [nums[random.randint(0, 9)] for _ in range(0, 5)]
    symbol_password = [symbol[random.randint(0, 9)] for _ in range(0, 5)]

    return letter_password, nums_password, symbol_password


a, b, c = generate_password()
print(shuffle(a, b, c))
