import random

active_player = 0
scores = [0, 0]
current_score = 0

max_score = int(input("What is the maximum score for playing that you want? "))
print(f"Max score is {max_score}")

while True:
    print("Ulazak u while")
    dice = random.randint(1,6)
    print(dice)

    if dice != 1:
        current_score += dice
        print(f"Current score is {current_score}")
        print('-----------')
        print(f"Current player is {active_player}")

        if current_score >= max_score:
            print(f"Player {active_player} won")
            break

        answer = input("Do you want to save your score and let second player to play(press y if you want that).")
        if answer == 'y':
            scores[active_player] += current_score
            current_score = 0
            if scores[active_player] >= max_score:
                print(f"Player {active_player} won")
                break
            if active_player == 0:
                active_player = 1
                print(f"Active player now is {active_player}")
                current_score = scores[active_player]
            else:
                active_player = 0
                print(f'Active player now is {active_player}')
                current_score = scores[active_player]
    else:
        print("Now is turn for another player, you got 1")
        current_score = 0
        scores[active_player] = 0
        if active_player == 0:
            active_player = 1
        else:
            active_player = 0