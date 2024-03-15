import random
import password_generator

abc = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

password = password_generator.generated_password

print(f"Your generated password is: {password}")

while True:
    question = input("Do you want to crack your password? [Y/N]  ").lower()
    if question == "y" or question == "yes":

        tries = 0
        tried_pw = ""

        while tried_pw != password:
            tried_pw = ""
            tries += 1

            for x in range(len(password)):
                tried_pw += random.choice(abc)

        print(f"The password was: {tried_pw}. Number of tries: {tries}")
        exit()
    elif question == "n" or question == "no":
        print("Bye!")
        exit()
    else:
        print('Invalid input! Only "Yes" or "No" [Y/N] accepted.')
