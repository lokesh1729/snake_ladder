import random

def run_game(turns, is_crooked_dice):
    position = 1
    snakes = [(97, 62), (77, 33), (54, 28), (38,11)]
    while turns > 0 and position < 100 :
        if is_crooked_dice is True:
            number = random.randint(1,6)
        else:
            number = random.choice([2,4,6])
        position += number
        if position > 100:
            break
        snake_on_path = next(filter(lambda item: item[0] == position, snakes), None)
        if snake_on_path is not None:
            position = snake_on_path[1]
        turns -= 1
    return position


def main():
    print("Crooked Dice ? (Y/N) : ", end="")
    is_crooked_dice = False
    if input().strip().lower() == 'y':
        is_crooked_dice = True
    print("Enter number of turns for the game to run : ", end="")
    try:
        turns = int(input().strip())
    except ValueError:
        turns = 10
    position = run_game(turns, is_crooked_dice)
    if position >= 100:
        print("You win! congrats!")
    else:
        print("game ended! you reached %s" % position)


if __name__ == "__main__":
    main()
