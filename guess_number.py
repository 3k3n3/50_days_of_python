"""
Write a function called guess_a_number. The function 
should ask a user to guess a randomly generated number. If the 
user guesses a higher number, the code should tell them that the 
guess is too high, if the user guesses low, the code should tell 
them that their guess is too low. The user should get a maximum 
of three guesses. When the user guesses right, the code should 
declare them a winner. After three wrong guesses, the code 
should declare them a loser.
"""
import random


def guess_a_number():
    num = random.choice(range(10))
    status = True
    count = 0
    while status == True:
        try:
            count += 1
            guess = int(input("Guess a number between 0 and 10: "))
            if guess == num:
                print("Correct! You win!")
                status = False
            elif guess > num and count < 4:
                count += 1
                print("Hint: Guess a lower number!")
            elif guess < num and count < 4:
                count += 1
                print("Hint: Guess an higher number!")
            else:
                print("You lose!\nAnswer is", num)
                status = False
        except ValueError as e:
            print(e)


guess_a_number()
