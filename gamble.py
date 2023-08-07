import os
import time

def main():
    print("Welcome to the Custom Calculator!")
    while True:
        initial_number = get_initial_number()
        if initial_number is None:
            print("Invalid initial number. Please try again.")
            continue

        user_input = get_user_input()
        if user_input is None:
            print("Invalid input. Please try again.")
            continue

        result = calculate_result(initial_number, user_input)
        print(f"The result is: {result}")

        time.sleep(5)  
        clear_console()


def get_initial_number():
    try:
        initial_number = int(input("Enter an initial number (20, 10, 5, 3): "))
        if initial_number not in [20, 10, 5, 3]:
            return None
        return initial_number
    except ValueError:
        return None


def get_user_input():
    try:
        user_input = float(input("Enter a number to multiply with the initial number: "))
        return user_input
    except ValueError:
        return None


def calculate_result(initial_number, user_input):
    factors = {20: 0.01, 10: 0.02, 5: 0.05, 3: 0.08}
    factor = factors.get(initial_number)
    if factor is None:
        return None

    return user_input * factor


def clear_console(): 
        os.system("cls")

if __name__ == "__main__":
    main()
