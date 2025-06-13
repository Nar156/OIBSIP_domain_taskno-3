import random
import string
from datetime import datetime

def user_input():
    while True:
        try:
            length = int(input("Enter password length"))
            if length < 4:
                print("Password length must be at 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")


    print("\nSelect characters types to include:")
    use_letters = input("Include letters? (y/n)").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n)").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n)").strip().lower() == 'y'

    if not (use_letters or use_digits or use_numbers):
        print("Select atleast one character type")
        return user_input()
    
    while True:
        try:
            count = int(input("How many password to generate?"))
            if count<=0:
                print("Enter a number greater than 0")
                continue
            break
        except ValueError:
            print("Enter a valid number.")

    
    save_to_file = input("Save passwords? (y/n)").strip().lower() == 'y'

    return length, use_letters, use_digits, use_numbers, count, save_to_file

def gen_pass(length, use_letters, use_digits, use_numbers):
    char_pools = []
    guarenteed_chars = []

    if use_letters:
        letters = string.ascii_letters
        char_pools.append(letters)
        guarenteed_chars.append(random.choice(letters))


    if use_digits:
        digits = string.digits
        char_pools.append(digits)
        guarenteed_chars.append(random.choice(digits))

    if use_numbers:
        numbers = string.punctuation
        char_pools.append(numbers)
        guarenteed_chars.append(random.choice(numbers))

    all_chars = ''.join(char_pools)
    remaining_length = length - len(guarenteed_chars)

    if remaining_length < 0:
        raise ValueError("Password length too short.")
    
    random_chars = [random.choice(all_chars) for _ in range(remaining_length)]
    password_chars = guarenteed_chars + random_chars
    random.shuffle(password_chars)

    return ''.join(password_chars)

def save_password(passwords):
    filename = f"passwords_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w') as file:
        for pwd in passwords:
            file.write(pwd + '\n')
    print(f"\nPasswords saved to {filename}")

def main():
    print("==== Password Generator====")
    length, use_letters, use_digits, use_numbers, count, save = user_input()

    password = []
    for _ in range(count):
        pwd = gen_pass(length, use_letters, use_digits, use_numbers)
        password.append(pwd)

    print("\nGenerated Password(s):")
    for pwd in password:
        print(pwd)

    if save:
        save_password(password)

if __name__ == "__main__":
    main()