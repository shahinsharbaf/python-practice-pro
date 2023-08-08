import random

def get_upper_lower_numbers():
    while True:
        try:
            upper_band_number = int(input("Enter upper band? "))
            lower_band_number = int(input("Enter lower band? "))
        except:
            print("Try again")
        else:
            return (upper_band_number, lower_band_number)


upper_band_number, lower_band_number = get_upper_lower_numbers()
random_number = random.randint(upper_band_number, lower_band_number)

while True:
    user_guess = int(input("Enter guess number? "))
    if user_guess > random_number:
        print("too high")
        continue
    if user_guess < random_number:
        print("too low")
        continue
    if user_guess == random_number:
        print("ok")
        break
