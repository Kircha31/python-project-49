from brain_games import ans_que as a


def start_game(game_name):
    player = a.welcome_user()
    if game_name.is_winner():
        print(f'Congratulations, {player}!')
    else:
        print(f"Let's try again, {player}!")
