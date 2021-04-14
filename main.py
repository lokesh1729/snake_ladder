def main():
    turns = 10
    position = 0
    while turns > 0 & position < 100 :
        try:
            number = int(input().strip())
            position += number
        except ValueError:
            print("please enter a valid input! only positive")
        
    print("game ended!")


if __name__ == "__main__":
    main()
