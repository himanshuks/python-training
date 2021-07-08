# Random library is used to generate random numbers between provided range
import random

# Both X and Y are included in the range for random number
randNum = random.randint(1, 100)

userGuess = None
numberOfGuesss = 0

# Below game takes username and number of guess
# If number is greater, we ask them to enter smaller number else vice versa
userName = input("Enter your name: ")

while userGuess != randNum:
    userGuess = int(input("Enter you guess (1-100): "))
    numberOfGuesss += 1
    if userGuess == randNum:
        print("Bingo, it's the perfect guess...!!!")
    else:
        if userGuess > randNum:
            print("Wrong guess. Enter a smaller number.")
        else:
            print("Wrong guess. Enter a larger number.")

print(f"You have taken {numberOfGuesss} guesses to get finish the game.")


# Post correct guess, save UserName and Hi-Score of number of guess taken
fileContent = f"""Player Name : {userName}
Hi Score : {numberOfGuesss}\n"""

# Save file with above captured data
with open(
    "d:\\visual studio\\python practice\\advanced\\randomGameHiScore.txt", "a"
) as f:
    f.write(fileContent)
