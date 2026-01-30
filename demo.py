def greet(name: str) -> None:
    """Print a greeting message."""
    print(f"Hello, {name}!")


def ask_user_name() -> str:
    """Ask the user for their name and return it."""
    name = input("Enter your name: ")
    return name.strip()


def greet_multiple_times(name: str, times: int = 1) -> None:
    """Greet the user multiple times."""
    for i in range(times):
        print(f"{i + 1}. Hello again, {name}!")


def main() -> None:
    user_name = ask_user_name()

    if not user_name:
        print("You did not enter a name.")
        return

    greet(user_name)
    greet_multiple_times(user_name, times=3)


if __name__ == "__main__":
    main()
