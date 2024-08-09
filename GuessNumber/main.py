from number_guessing_game import play_game, number_generator
def main() -> None:

    print("Welcome to number guessing Game!\n I am thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        number_of_tries = 10
    elif difficulty == "hard":
        number_of_tries = 5
    else:
        print("Invalid Choice!")

    number = number_generator()
    play_game(number_of_tries, number)
    

if __name__ == "__main__":
    main()
