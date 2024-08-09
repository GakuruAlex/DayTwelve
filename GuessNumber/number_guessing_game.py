from random import randint

#Number Generator
def number_generator() -> int:
    """_Generate a random number between 1 or 100_

    Returns:
        int: _An int between 1 and 100_
    """
    return randint(1, 100)

def number_guessing_game(number: int,guess: int) -> tuple:
    """_Check guess against generated number_

    Args:
        number (int): _Generated number_
        guess (int): _User guess_

    Returns:
        tuple: _A str for whether the guess is too low or too high and whether the game is still on_
    """
    if number == guess:
        return f"You got it right. The number was {number}", True
    elif number > guess:
        return f"Too low!", False
    else:
        return f"Too high", False

def play_game(number_of_tries: int, number: int):
        while number_of_tries > 0:
            print(f"You have {number_of_tries} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            if number_guessing_game(number, guess)[1]:
                print(number_guessing_game(number = number,  guess= guess)[0])
                break
            else:
                print(number_guessing_game(number = number,  guess= guess)[0])
                number_of_tries -= 1
        if number_of_tries == 0 and not number_guessing_game(number, guess)[1]:
            print(f"No more Tries. The Number was {number}")
