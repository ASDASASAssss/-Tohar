import random
import string

print ("@MadeByTohar!")

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    password = generate_password(password_length)
    print("PassWord Ready, do not share ur pass to anyone!:", password)