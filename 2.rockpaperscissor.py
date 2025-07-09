import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    print(f"Your choice: {user}\nComputer choice: {computer}")
    # r > s, s > p, p > r
    if user == computer:
        return 'It\'s a tie!'
    
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return 'You won!'

    return 'You lost!'

print(play())

    