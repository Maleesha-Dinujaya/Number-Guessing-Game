import random

seed = int(input("Enter a random seed (integer): "))
random.seed(seed)

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please type a number.")
    quit()

random_number = random.randint(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Please Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
        if user_guess == random_number:
            print("Yess!! You got it!")
            break 
        
        elif user_guess > random_number:
            print("You were above the number")
                
        else:
            print("You were below the number")
    else:
        print("Please type a number.")
        
print("Congratulations!! You got it", str(guesses), "guesses")
