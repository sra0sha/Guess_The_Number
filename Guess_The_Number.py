import random
import math


def get_range():
    while True:
        try:
            n = int(input("Choose The Ceilimg Of Your Range: "))
            if n > 1:
                return n
            else:
                print("The range ceiling must be greater than 1!")
        except ValueError:
            print("You Can Just Insert Unsigned Integers!")


def generate_number(n):
    return random.randint(1, n)


def get_guess(player, n):
    while True:
        try:
            choice = int(input(f"{player}, Your Guess Is: "))
            if 1 <= choice <= n:
                return choice
            else:
                print(f"The number That You Entered Is not Within The Range 1 To {n}!")
        except ValueError:
            print("You Can Just Insert Unsigned Integers!")


def play_solo_game(player1, number, n, BigO):
    counter = 0
    print(f"Guess The number That We Have Chosen From 1 To {n}")
    print(f"You Can Find The Answer In {BigO} Attempts!    GLHF ;)")

    while True:
        counter += 1
        choice = get_guess(player1, n)
        if choice == number:
            print(f"Congratulations, {player1}! You Guessed It In {counter} Attempts.")
            return player1
        elif choice < number:
            print("Guess Higher!")
        else:
            print("Guess Lower!")

        if counter > BigO:
            print(
                f"{player1}, you have used all your attempts. The number was:", number
            )
            return None


def play_multiplayer_game(player1, player2, number, n, BigO):
    counter = 0
    print(f"Guess The number That We Have Chosen From 1 To {n}")
    print(f"You Can Find The Answer In {BigO} Attempts!    GLHF ;)")

    while True:
        counter += 1
        print(f"\n{player1}'s Turn:")
        choice = get_guess(player1, n)
        if choice == number:
            print(f"Congratulations, {player1}! You Guessed It In {counter} Attempts.")
            return player1
        elif choice < number:
            print("Guess Higher!")
        else:
            print("Guess Lower!")

        counter += 1
        print(f"\n{player2}'s Turn:")
        choice = get_guess(player2, n)
        if choice == number:
            print(f"Congratulations, {player2}! You Guessed It In {counter} Attempts.")
            return player2
        elif choice < number:
            print("Guess Higher!")
        else:
            print("Guess Lower!")

        if counter > BigO * 2:
            print("Both players have used all their attempts. The number was:", number)
            return None


def main():
    while True:

        exit_program = input(
            "\nIf You Want To Play Just Simply Press 'Enter Button' \n   If not, Type 'exit' To Leave The Game: "
        )
        if exit_program.lower() == "exit":
            print("Hope You Enjoyed Playing; See You...")
            break

        game_mode = input(
            "\nif you want to play by yourself type 'solo', if not type 'multiplayer' to start the 1vs1 game: "
        )

        n = get_range()
        number = generate_number(n)
        BigO = math.ceil(math.log2(n))

        player1 = input("Enter Player 1's name: ")
        if game_mode.lower() == "multiplayer":
            player2 = input("Enter Player 2's name: ")
        else:
            player2 = None

        if game_mode.lower() == "solo":
            winner = play_solo_game(player1, number, n, BigO)
        elif game_mode.lower() == "multiplayer":
            winner = play_multiplayer_game((player1, player2, number, n, BigO))
        else:
            print(
                "Invalid game mode selected. Please choose between 'solo' and 'multiplayer'."
            )
            continue

        if winner:
            print(f"{winner} is the winner!")
        else:
            print("It's a tie! no one guessed the number.")


if __name__ == "__main__":
    main()
