import random
random_num = random.randint(1,100)
attempts=0
while True:
    guess = int(input("guess a num"))
    attempts+=1

    if guess < random_num:
        print("too low")
    elif guess > random_num:
        print("too high")
    elif guess == random_num:
        print("congratulations, you cracked")
        break