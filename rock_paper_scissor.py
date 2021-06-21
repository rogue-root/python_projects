import random  # for computer to have random choice
import time  # for time delays so it feels more natural

# the number of turns the player wants to play
terms = int(input("enter how many turns you want to play for: "))
c_score = 0
h_score = 0

for i in range(terms):
    # for comouter to have a random choice
    ch = ["rock", "paper", "scissors"]
    computer = random.choice(ch)

    # human choice
    human = input("please enter your choice r, p, s: ")
    human = human.lower()
    if human == 'r':
        human = "rock"
    elif human == 'p':
        human = "paper"
    elif human == "s":
        human = "scissors"
    else:
        print("please enter a valid choice")
        continue

    print("you choose: ", human)
    time.sleep(2)
    print("computer choose: ", computer)

    time.sleep(1)
    if computer == human:
        print("Its a draw!")
    elif (computer == 'rock' and human == 'paper') or (computer == 'paper' and human == 'scissors') or (computer == 'scissors' and human == 'rock'):
        print(human, "destroyed", computer)
        time.sleep(1)
        print("You win!")
        h_score += 1
    else:
        print(computer, "destroyed", human)
        time.sleep(1)
        print("computer win!")
        c_score += 1

    time.sleep(1)
    print("computer score: ", c_score)
    print("human score: ", h_score)
