import random

active_player = 0
scores = [0, 0]
current_score = 0

max_score = int(input("What is the maximum score for playing that you want? "))
print()
print(f"Max score is {max_score}")

while True:
    print('----------')
    print()
    print("Total score is", scores[active_player])
    dice = random.randint(1,6)
    print("You got ", dice)

    if dice != 1:
        current_score += dice
        print(f"Current score is {current_score}")
        print(f"Current player is {active_player}")
        print()
        print('-----------')

        if scores[active_player] + current_score >= max_score:
            print('***********')
            print(f"Player {active_player} won")
            print('***********')
            break

        answer = input("Do you want to save your score and let second player to play(press y if you want that).")
        if answer == 'y':
            scores[active_player] += current_score
            current_score = 0

            # active_player = 1 if active_player == 0 else 0
            # active_player = (active_player + 1) % len(scores)

            if active_player == 0:
                active_player = 1
            else:
                active_player = 0

            print()
            print("PLAYERS ARE CHANGED")
            print('Now is another turn for another player')
            print(f"Active player now is {active_player}")
            print()
        else:
            print()
            print(f"Player {active_player} is still playing.")
    else:
        print()
        print("Now is turn for another player, you got 1")
        print("PLAYERS ARE CHANGED")
        current_score = 0
        if active_player == 0:
            active_player = 1
        else:
            active_player = 0
        print(f'Active player now is {active_player}')
        print()
