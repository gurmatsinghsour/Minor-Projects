import sys
from random import randint

first = int(sys.argv[1])
last = int(sys.argv[2])

randomnum = randint(int(first), int(last))

while True:
    try: 
        user_num = int(input("Guess the random no.: "))
        if user_num == randomnum:
            print("Congratulation, you've won!")
            exit()

        else:
            print("Incorrect guess! Try again.")

    except ValueError as err:
        print(f"Hey, please enter a valid number")               

if __name__ == '__main__':
    main()
