import random

# Set the initial values
guess_attempt = 0

random_value = random.randint(1, 10)

def attempts_remaining():
    return attempts_available - guess_attempt


# Keep letting the player guess until they get it right or run out of attempts
player_guessed_number = int(input("Guess a number between 1 and 10: \n"))
attempts_available = 3
while player_guessed_number != random_value and attempts_available > 0:
    # Get the user's guess inside the loop
    
    guess_attempt += 1

    # Check for remaining attempts and display appropriate message
    if attempts_available > 0:
        print("You have ", attempts_remaining(), " attempts remaining.")
    else:
        print("Oh no, you are out of chances! The correct answer is:", random_value)

# Display congratulations message if the player guessed correctly
if player_guessed_number == random_value:
    print("Congratulations! You have guessed the right number.")
    print("You have guessed the number in", guess_attempt, "attempts.")
