import random
import string


def generate_password(length):
    # Define character sets for different complexity levels
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+=-[]{}|;:'<>,.?/~"

    # Combine character sets based on complexity level
    if length < 6:
        print("Password length should be at least 6 characters.")
        return
    elif length < 10:
        charset = lowercase_letters + uppercase_letters + digits
    else:
        charset = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate the password using random.choices()
    password = ''.join(random.choices(charset, k=length))
    return password


def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))

    password = generate_password(length)

    if password:
        print("Generated Password:", password)
    else:
        print("Password generation failed.")


if __name__ == "__main__":
    main()
