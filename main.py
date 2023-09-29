import random
import string
import pyperclip  # For copying to clipboard (you may need to install this library)


def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    characters = ''

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    length = int(input("Enter the password length: "))
    use_uppercase = input("Include uppercase letters (yes/no): ").lower() == "yes"
    use_lowercase = input("Include lowercase letters (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters (yes/no): ").lower() == "yes"

    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)

    if password:
        print("Generated Password:", password)
        copy_to_clipboard = input("Copy to clipboard (yes/no): ").lower() == "yes"
        if copy_to_clipboard:
            pyperclip.copy(password)
            print("Password copied to clipboard.")
