import random

abc = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")


def get_integer_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")


password_length = get_integer_input("How many characters do you want for your password?: ")


def generator(abc, length):
    random_pw = ""

    for _ in range(length):
        random_pw += random.choice(abc)

    return random_pw


generated_password = generator(abc, password_length)
