
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

length = int(input("Enter password length: "))

if length < 8:
    print("Password must be at least 8 characters.")
else:
    password = generate_password(length)
    print("Generated password:", password)
