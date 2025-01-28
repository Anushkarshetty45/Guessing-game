#GUESSING GAME


import random

secret_number = random.randint(1, 101)

def random_number(attempts):
    for attempt in range(attempts):
        print(f"Attempt {attempt + 1} of {attempts}")
        number = input("ENTER A NUMBER FROM 1 TO 100: ")
        if int(number) > secret_number:
            print("Try a lower number.")
            print()
        elif int(number) < secret_number:
            print("Try a higher number.")
            print()
        else:
            print(f"{secret_number} is correct, you guessed it right!")
            print()
              
    print(f"You've used all {attempts} attempts. You lose!")
    print(f"The correct number was {secret_number}.")
    print()
    print("****************")
    print()
    random_number(attempts)  

while True:
    try:
        max_attempts = int(input("How many attempts would you like? "))
        if max_attempts <= 0:
            print("Please enter a positive number.")
            continue
    except Exception as e:
        print(e)
        continue


    random_number(max_attempts)

print(f"The correct number was {secret_number}. Thanks for playing!")


