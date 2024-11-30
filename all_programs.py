
# Tip Calculator
def tip_calculator():
    print("Welcome to the Tip calculator!")
    bill = float(input("What was the total bill? € "))
    tip = int(input("How much tip would you like to give? "))
    people = int(input("How many people to split the bill? "))
    bill_with_tip = round((tip / 100 * bill) + bill, 2)
    print(f"The total bill is {bill_with_tip} €.")
    bill_per_person = round((bill_with_tip / people), 1)
    print(f"Each person should pay: {bill_per_person} €.")

# Lifespan Calculator
def lifespan_calculator():
    age = int(input("What is your age? "))
    years_left = 90 - age
    weeks_left = years_left * 52
    print(f"You have {weeks_left} weeks left in your lifespan.")

# BMI Calculator
def bmi_calculator():
    print("What's your height? ")
    height = float(input())  # Only in meters
    print("And your weight? ")
    weight = int(input())  # Only in kilograms
    BMI = round(weight / (height ** 2), 1)
    if BMI < 18.2:
        print(f"Your BMI is {BMI}, which is categorized as underweight.")
    elif BMI < 25.0:
        print(f"Your BMI is {BMI}, which is categorized as normal.")
    elif BMI < 30.0:
        print(f"Your BMI is {BMI}, which is categorized as slightly overweight.")
    elif BMI < 35:
        print(f"Your BMI is {BMI}, which is categorized as obese.")
    else:
        print(f"Your BMI is {BMI}, categorized as severely obese.")

# Leap Year Checker
def leap_year_checker():
    year = int(input("Which year do you want to check? "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"The year {year} is a leap year.")
            else:
                print(f"The year {year} is not a leap year.")
        else:
            print(f"The year {year} is a leap year.")
    else:
        print(f"The year {year} is not a leap year.")

# Rollercoaster Ticketing System
def rollercoaster_ticketing():
    print("Welcome to the thriller park!")
    height = int(input("Please insert your height, in cm: "))
    bill = 0
    if height >= 120:
        print("You are eligible to ride the rollercoaster.")
        age = int(input("What is your age? "))
        if age < 12:
            bill = 10
        elif age <= 18:
            bill = 15
        elif 45 <= age <= 55:
            bill = 0
        else:
            bill = 20
        photo = input("Do you want a photo taken? (Y/N): ").lower()
        if photo == "y":
            bill += 4
        print(f"Your total bill is {bill} €. Enjoy!")
    else:
        print("You are not tall enough to ride the rollercoaster.")

# Pizza Ordering System
def pizza_ordering():
    print("Welcome to the Pizza shop!")
    size = input("Choose a size (S, M, L): ").upper()
    bill = 0
    if size == "S":
        bill += 7
    elif size == "M":
        bill += 12
    else:
        bill += 17
    pepperoni = input("Add pepperoni? (Yes/No): ").lower()
    if pepperoni == "yes":
        bill += 2
    cheese = input("Add extra cheese? (Yes/No): ").lower()
    if cheese == "yes":
        bill += 4
    print(f"Your total bill is {bill} €. Enjoy your meal!")


# Treasure Island Adventure Game
def treasure_island():
    print("Welcome to Treasure Island!")
    print("Your mission is to find the treasure.")
    choice1 = input("Do you want to go left or right? ").lower()
    if choice1 == "left":
        choice2 = input("Swim or wait? ").lower()
        if choice2 == "wait":
            choice3 = input("Which door? (Red/Blue/Yellow): ").lower()
            if choice3 == "yellow":
                print("You found the treasure! You win!")
            else:
                print("Game over!")
        else:
            print("Game over!")
    else:
        print("Game over!")

# Toss a Coin Game
def toss_coin():
    import random
    coin = random.choice(["Heads", "Tails"])
    print(f"The coin toss result is: {coin}")

# Randomized Paying System
def randomized_payer():
    import random
    friends = ["Patrik", "Bob", "Carlos"]
    payer = random.choice(friends)
    print(f"{payer} is paying!")

# Rock-Paper-Scissors Game
def rock_paper_scissors():
    import random
    options = ["Rock", "Paper", "Scissors"]
    user_choice = int(input("Choose 0 for Rock, 1 for Paper, or 2 for Scissors: "))
    if user_choice >= 3 or user_choice < 0:
        print("Invalid choice. You lose!")
    else:
        computer_choice = random.randint(0, 2)
        print(f"You chose {options[user_choice]}")
        print(f"The computer chose {options[computer_choice]}")
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 0 and computer_choice == 2) or
        (user_choice == 1 and computer_choice == 0) or
        (user_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("You lose!")

# Average Height Calculator
def average_height():
    heights = list(map(int, input("Enter heights separated by space: ").split()))
    if heights:
        avg_height = sum(heights) / len(heights)
        print(f"The average height is {avg_height:.2f}")

# FizzBuzz
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Password Generator
def password_generator():
    import random
    import string
    letters = int(input("How many letters? "))
    digits = int(input("How many digits? "))
    symbols = int(input("How many symbols? "))
    password = [
        random.choice(string.ascii_letters) for _ in range(letters)
    ] + [
        random.choice(string.digits) for _ in range(digits)
    ] + [
        random.choice(string.punctuation) for _ in range(symbols)
    ]
    random.shuffle(password)
    print(f"Your password is: {''.join(password)}")

