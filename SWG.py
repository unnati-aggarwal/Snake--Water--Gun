# Snake water gun game
import random
user_score =0
computer_score =0
for i in range(5):
    print(f"Round No. {i+1}")
    computer_choice = random.choice(["S", "W", "G"])

    user_answer = input("Please Enter S for Snake, W for Water, G for Gun: ").upper()
    if user_answer not in ["S", "W", "G"]:
        print("Invalid Name")
    else:
        print(computer_choice)

    if user_answer == computer_choice:
        print("It is a Draw")
    elif (user_answer == "S" and computer_choice == "W") or \
        (user_answer == "W" and computer_choice == "G") or \
        (user_answer == "G" and computer_choice == "S"):
        print("You Won")
        user_score +=1
    else:
        print("Try Again!")
        computer_score +=1

    print(f"Your Score: {user_score}| Computer: {computer_score}")

print("Final Score")
print(f"Your Score: {user_score}| Computer: {computer_score}")

if user_score > computer_score:
    print("You Won")
else:
    print("Retry")