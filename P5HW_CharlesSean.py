# CTI-110 Random Mat Quiz
# 11/14/2023
# CTI-110 P5HW - Math Quiz
# Sean Charles
#

import random

def display_menu():
    print("Menu:")
    print("1. Add numbers and guess the result")
    print("2. Subtract numbers and guess the remainder")
    print("3. Exit")

def generate_numbers():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def add_numbers():
    while True:
        num1, num2 = generate_numbers()
        result = num1 + num2
        guess = int(input(f"What is {num1} + {num2}? Enter your guess: "))

        if guess == result:
            print("Congratulations! Your guess is correct.")
            break
        else:
            print("Sorry, incorrect guess. Try again.")

def subtract_numbers():
    while True:
        num1, num2 = generate_numbers()
        result = num1 - num2
        guess = int(input(f"What is {num1} - {num2}? Enter your guess for the remainder: "))

        if guess == result:
            print("Congratulations! Your guess is correct.")
            break
        else:
            print("Sorry, incorrect guess. Try again.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1, 2, 3): ")

        if choice == "1":
            add_numbers()

        elif choice == "2":
            subtract_numbers()

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Error: Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
