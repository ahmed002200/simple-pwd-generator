import random
import string
import math


def generate(num_of_chars, include_numbers, include_special):
    num_of_caps = math.ceil(num_of_chars * 0.4)
    chars = list(string.ascii_lowercase)
    special_chars = list(string.punctuation)
    password = []
    for _ in range(0, num_of_chars):
        password.append(chars[random.randint(0, len(chars) - 1)])
    for _ in range(0, num_of_caps):
        random_index = random.randint(0, len(password)-1)
        password[random_index] = password[random_index].upper()
    if include_numbers == "yes":
        for _ in range(0, math.ceil((len(password)-1) * 0.3)):
            password[random.randint(0, len(password)-1)] = random.randint(0,9)
    if include_special == "yes":
        for _ in range(0, math.ceil((len(password)-1) * 0.1)):
            while True:
                number_index = random.randint(0, len(password)-1)
                item = str(password[number_index])
                if item.isalpha():
                    if item.islower():
                        password[number_index] = random.choice(special_chars)
                        break

    result = ''.join(str(item) for item in password)
    print(f"Here is your password: {result}")




def start():
    answers = ["yes", "no"]
    while True:
        try:
            num_of_chars = int(input("How many characters would you like your password to be (8-32)? "))
            include_numbers = input("Would you like to include numbers in you password (yes/no)? ").lower()
            include_special = input("Would you like to include special characters in your password (yes/no)? ").lower()
            if (include_numbers in answers) and (include_special in answers):
                generate(num_of_chars, include_numbers, include_special)
                break
            else:
                print("Only yes or no allowed. Try again.")
        except ValueError:
            print("Your input was invalid. Try again.")

start()
