def my_encrypt(messgae, shift_number):
    encrypted_message = ''
    for my_char in messgae:
        encrypted_message += chr(ord(my_char)+shift_number)
    return (encrypted_message)


def my_decrypt(messgae, shift_number):
    encrypted_message = ''
    for my_char in messgae:
        encrypted_message += chr(ord(my_char)-shift_number)
    return (encrypted_message)


while True:
    encrypt_decrypt = input("Type 'E' to encrypt type 'D' to decrypt: ")
    if encrypt_decrypt.upper() == 'E':
        message = input("Enter you message? ")
        shift_number = int(input("Enter shift number? "))
        print("The encrypted messgae is: %s" %
              my_encrypt(message, shift_number))

    if encrypt_decrypt.upper() == 'D':
        message = input("Enter you message? ")
        shift_number = int(input("Enter shift number? "))
        print("The decrypted  messgae is: %s" %
              my_decrypt(message, shift_number))

    resume_not = input("Enter 'Y' want to go again. otherwise type 'N'? ")
    if resume_not.upper() == 'N':
        break
