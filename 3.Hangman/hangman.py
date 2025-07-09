import random
from words import words, hangman

def display_hangman(count):
    print(f'Hangman: {hangman[count]}')

def display_answer(word):
    print("Target: ", ' '.join(word))

def main():
    word = random.choice(words).lower()    
    answer = ["_"] * len(word)
    chances = 0
    guessed_letters = set()

    display_hangman(chances)
    display_answer(answer)

    while True:
        
        guess = input('Guess a letter: ').lower()

        if guess in guessed_letters:
            print("You already guessed it")
        else:
            if guess in word:
                for i, c in enumerate(word):
                    if c == guess:
                        answer[i] = guess
                display_answer(answer)
            else:
                chances += 1

                if(chances == len(hangman)-1):
                    print("Sorry!! Try again #######")
                    display_hangman(chances)
                    display_answer(word)
                    break
                display_hangman(chances)
                display_answer(answer)
        guessed_letters.add(guess)
        
        if '_' not in answer:
            print(f"Congrats!! You guessed the '{word}' ")
            break
        
        

if __name__ == "__main__":
    main()