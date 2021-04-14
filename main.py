def main():
    turns = 10
    position = 1
    snakes = [(97, 62), (77, 33), (54, 28), (38,11)]
    while turns > 0 and position < 100 :
        try:
            number = int(input().strip())
            position += number
            snake_on_path = next(filter(lambda item: item[0] == position, snakes), None)
            if snake_on_path is not None:
                position = snake_on_path[1]
        except ValueError:
            print("please enter a valid input! only positive")
    if position == 100:
        print("You win! congrats!")
    else:
        print("game ended! you reached %s" % position)


if __name__ == "__main__":
    main()
