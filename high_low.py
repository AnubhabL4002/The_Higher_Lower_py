import random
from art import logo, vs
from game_data import data

print(logo)
game_over=False
score=0

while True:
    index1 = random.randint(0,49)
    index2 = random.randint(0,49)
    if index1 != index2:
        break

while not game_over:
    print(f"Compare A: {data[index1]["name"]}, a {data[index1]["description"]}, from {data[index1]["country"]}")
    print(vs)
    print(f"Compare B: {data[index2]["name"]}, a {data[index2]["description"]}, from {data[index2]["country"]}")
    answer = input("Who has more followers? Type 'A' or 'B'.").lower()
    if answer == 'a':
        if data[index1]["follower_count"] > data[index2]["follower_count"]:
            score+=1
            print(f"****You are correct!***** \nCurrent Score: {score}\n")
        elif data[index1]["follower_count"] == data[index2]["follower_count"]:
            print(f"****Actually both same.***** \nCurrent Score: {score} (No extra score)")
        else:
            print("\n"*100)
            print(logo)
            print(f"Sorry that's Wrong. Final score: {score}")
            game_over = True
    else:
        if data[index1]["follower_count"] < data[index2]["follower_count"]:
            score+=1
            print(f"****You are correct!***** \nCurrent Score: {score}\n")
        elif data[index1]["follower_count"] == data[index2]["follower_count"]:
            print(f"****Actually both same.***** \nCurrent Score: {score} (No extra score)")
        else:
            print("\n"*100)
            print(logo)
            print(f"Sorry that's Wrong. Final score: {score}")
            game_over = True
    index1 = index2
    index2 = random.randint(0,49)
