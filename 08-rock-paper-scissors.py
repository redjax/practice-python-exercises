"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),
compare them, print out a message of congratulations
to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

# Global counter to keep number separate from game()
round_count = 1
# Global player score tracker
player_score = 0
# Global computer score tracker
computer_score = 0


def get_player_input():
    """Ask player for move, then validate."""
    player_move = input("""
    Enter first letter only for choice:
    (R)ock
    (P)aper
    (S)cissors

    Entry: """)

    # Convert move to lower case for uniform comparison
    player_move = player_move.lower()

    valid_move = validate_choice(player_move)
    return valid_move


def validate_choice(move):
    """Ensure user chose a valid option."""
    valid_options = ['r', 'p', 's']

    if move in valid_options:
        if move == 'r':
            return 'rock'
        elif move == 'p':
            return 'paper'
        elif move == 's':
            return 'scissors'
    else:
        input("\nEnter either 'r', 'p', or 's'. Press a key to try again:")
        game()


def generate_computer_move():
    import random

    moves = ['rock', 'paper', 'scissors']
    return random.choice(moves)


def choose_winner(player_move, computer_move):

    if player_move == computer_move:
        print("It's a tie!")
    elif player_move == 'rock':
        if computer_move == 'scissors':
            print("Rock wins!")
            add_to_score('human')
        else:
            print("Paper wins!")
            add_to_score('computer')
    elif player_move == 'paper':
        if computer_move == 'rock':
            print("Paper wins!")
            add_to_score('human')
        else:
            print("Scissors win!")
            add_to_score('computer')
    elif player_move == 'scissors':
        if computer_move == 'paper':
            print("Scissors win!")
            add_to_score('player')
        else:
            print("Rock wins!")
            add_to_score('computer')


def add_to_score(player):
    global player_score
    global computer_score

    if player == 'human':
        player_score += 1
    elif player == 'computer':
        computer_score += 1


def compare_score():
    global player_score
    global computer_score

    print("""
    Your score: {}
    Computer score: {}""".format(player_score, computer_score))

    print('\n')

    if player_score == computer_score:
        print("It's a tie!")
    elif player_score > computer_score:
        print('You win!')
    else:
        print('The computer wins!')


def game():
    global round_count

    def round_tracker(round):
        round = round + 1
        return round

    player_move = get_player_input()
    computer_move = generate_computer_move()

    print('\nYou chose {}.'.format(player_move))
    print('\nThe computer chose {}.'.format(computer_move))
    print('\n')
    choose_winner(player_move, computer_move)
    print('\n')

    play_again = input('Would you like to play again? "Y" or "N": ')
    play_again = play_again.upper()

    if len(play_again) > 1:
        print('Invalid choice. Ending the game.')
        print('You lasted {} rounds!'.format(round_count))
        exit()

    elif play_again == 'Y':
        print('\n')
        round_num = round_tracker(round_count)
        round_count += 1
        input('Alright! Round {}, here we go!'.format(round_num))
        game()

    elif play_again == 'N':
        compare_score()

        input("""
        You lasted {} rounds. Good job!

        Good game. Press enter to quit:
        """.format(round_count))
        exit()

    else:
        print('Invalid choice. Ending the game.')
        print('You lasted {} rounds!'.format(round_count))
        exit()


game()
