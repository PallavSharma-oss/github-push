"""
Greeting utility module.

This module provides functions to greet a user,
ask for user input, and repeat greetings multiple times.
"""


def greet(name: str) -> None:
    """Print a greeting message."""
    print(f"Hello, {name}!")


def ask_user_name() -> str:
    """Ask the user for their name and return it."""
    user_input = input("Enter your name: ")
    return user_input.strip()


def greet_multiple_times(name: str, times: int = 1) -> None:
    """Greet the user multiple times."""
    for count in range(times):
        print(f"{count + 1}. Hello again, {name}!")


def main() -> None:
    """Main entry point of the program."""
    user_name = ask_user_name()

    if not user_name:
        print("No name entered.")
        return

    greet(user_name)
    greet_multiple_times(user_name, times=3)


if __name__ == "__main__":
    main()
