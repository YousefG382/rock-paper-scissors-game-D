import random 

options = ["rock","paper","scissors"]



user_wins = 0 
computer_wins = 0 

while True:
    user_input = input("Choose rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("computer pick", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
     print("you won!")
     user_wins += 1
            


    elif user_input == "paper" and computer_pick == "rock":
     print("you won!")
     user_wins += 1
            

    elif user_input == "scissors" and computer_pick == "paper":
     print("you won!")
     user_wins += 1
    else:
     print("you lost!")
     computer_wins += 1

print("Goodbye! ")
print("your wins are " , user_wins , " and computer wins are ", computer_wins)
#done by yousefg382
