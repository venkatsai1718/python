import random

n = random.randint(1, 100)
user = -1
count = 0
while user != n:
    count += 1
    user = int(input("Guess the number between 1 and 100: "))
    if(user > n):
        print("Lower number please")
    elif(user < n):
        print("Higher number please")

print(f"Congratulations! You guessed the number {n} in {count} attempts")