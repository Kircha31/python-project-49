from brain_games.games import even_game as e
import sys

def main():
    print('Welcome to the Brain Games!')
    
    output = e.even()
    if output:
        sys.exit(0)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
