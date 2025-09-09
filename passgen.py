import random
import string

def generate_pass(min_len, numbers=True, spec_char=True):
    letters = string.ascii_letters
    digits = string.digits
    spec = string.punctuation

    char = letters
    if numbers:
        char += digits
    if spec_char:
        char += spec

    pwd = ""
    meets_cri = False
    has_number = False
    has_spec = False

    while not meets_cri or len(pwd) < min_len:
        new_char = random.choice(char)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in spec:
            has_spec = True

        meets_cri = True
        if numbers:
            meets_cri = has_number
        if spec_char:
            meets_cri = meets_cri and has_spec

    return pwd

try:
    min_len = int(input("Enter the minimum length: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

has_num = input("Do you want to have numbers (y/n): ").lower() == "y"
has_spec = input("Do you want to have special characters (y/n): ").lower() == "y"

pwd = generate_pass(min_len, has_num, has_spec)
print("The Generated password is:", pwd)
