import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)

# Set the number of available attempts
lives = 10

# Continue the game while the player has lives left
while lives > 0:
    user_guess = int(input("ENTER YOUR GUESS: "))

    if user_guess > secret_number:
        lives -= 1
        print("Lower", "[Lives] =", lives)
        print(30 * "=")

    elif user_guess < secret_number:
        lives -= 1
        print("Higher", "[Lives] =", lives)
        print(30 * "=")

    elif user_guess == secret_number:
        # End the game when the player guesses correctly
        print("You won, congrats! 🔥")
        break

    # Reveal the secret number when the player runs out of lives
    if lives == 0:
        print("The correct number =", secret_number)