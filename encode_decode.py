from cryptography.fernet import Fernet

# making and storing encryption key


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("secret.key", "rb").read()


def encrypt_message(message):
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    print("the encrypted message is: ", encrypted_message)


def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())


# taking user defined message
if __name__ == "__main__":
    msg = input("enter your message: ")
    en_msg = encrypt_message(msg)

# for decryption uncomment below line
#    decrypt_message(en_msg)
