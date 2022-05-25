import random
lucky=random.randrange(0,9)
guess_count=0
guess_limit=random.randrange (1,6)
while guess_count<guess_limit:
    guess=int(input("Guess a number_"))
    if guess==lucky:
        print(f"You won!. {lucky} is the lucky number!")
        break
    elif guess!=lucky:
        guess_count+=1
        if guess_count<guess_limit:
            print("Try again:")
  
else:
    print(f"You lost, the lucky number is {lucky}!")