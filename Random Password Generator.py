import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    character_pool = ''
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("No characters selected to generate the password")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the length of the password: "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
        
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
        print(f"Generated password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")
