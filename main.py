import random
from students import padilla_tarea  

# ANSI color codes
COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[32m"
COLOR_RED = "\033[31m"
COLOR_YELLOW = "\033[33m"
COLOR_CYAN = "\033[36m"

EXERCISES = [
    "Add difficulty levels to the guessing game.",
    "Track how many games the user has played.",
    "Improve input validation in the main menu.",
    "Add a rock-paper-scissors mini-game.",
    "Allow the user to change their username.",
    "Add more console colors for different message types.",
    "Track how many attempts the user needed to guess correctly.",
    "Show a short history of the last game results.",
    "Add a clear_screen() helper function and use it.",
    "Create a configuration menu for game options.",
    "Move color constants to a separate file.",
    "Create a utils.py file with helper functions.",
    "Improve error messages to be more user-friendly.",
    "Add an 'About contributors' screen.",
    "Add decorative separators between sections.",
    "Make the program bilingual.",
    "Add a 'lucky number of the day' feature.",
    "Add manual testing instructions.",
    "Expand the README.",
    "Add an automatic demo mode."
]

def greet():
    """Ask for user's name and greet them."""
    name = input("What's your name? ")
    print(f"{COLOR_CYAN}Hello, {name}! Welcome to the GitHub collaboration demo.{COLOR_RESET}")

def guess_the_number():
    """Simple number guessing game with 3 attempts."""
    print(f"{COLOR_YELLOW}I'm thinking of a number from 1 to 10. You have 3 tries.{COLOR_RESET}")
    secret_number = random.randint(1, 10)
    attempts = 3

    while attempts > 0:
        try:
            attempt = int(input("Enter a number: "))
        except ValueError:
            print(f"{COLOR_RED}Please enter a valid number.{COLOR_RESET}")
            continue

        if attempt == secret_number:
            print(f"{COLOR_GREEN}Correct! You guessed the number.{COLOR_RESET}")
            return
        elif attempt < secret_number:
            print("The secret number is higher.")
        else:
            print("The secret number is lower.")

        attempts -= 1
        print(f"You have {attempts} attempts left.\n")

    print(f"{COLOR_RED}Out of attempts! The number was {secret_number}.{COLOR_RESET}")

def show_program_info():
    """Show information about the program."""
    print(f"{COLOR_GREEN}=== Program Information ==={COLOR_RESET}")
    print("Project: GitHub Collaboration Demo")
    print("Description: A basic project for practicing branches and pull requests.")
    print("Author: Your Name")

def show_random_exercise():
    """Show a random exercise idea from the list."""
    print(f"{COLOR_GREEN}=== Random Exercise Idea ==={COLOR_RESET}")
    print(f"{COLOR_CYAN}{random.choice(EXERCISES)}{COLOR_RESET}")

def show_menu():
    """Display main menu."""
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Greet")
        print("2. Guess the number")
        print("3. Program Info")
        print("4. Random Exercise Idea")
        print("5. Feature Padilla (Validar Numero)")  # <--- Tu opción
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            greet()
        elif choice == "2":
            guess_the_number()
        elif choice == "3":
            show_program_info()
        elif choice == "4":
            show_random_exercise()
        elif choice == "5":
            # Aquí llamamos a TU función que está en students/padilla_tarea.py
            padilla_tarea.student_feature()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print(f"{COLOR_RED}Invalid option. Try again.{COLOR_RESET}")

# ESTO ES LO QUE FALTABA: El comando para que arranque
if __name__ == "__main__":
    show_menu()