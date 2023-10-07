import random
import tkinter as tk
from tkinter import messagebox

def check_guess():
    global guesses
    user_guess = guess_entry.get()
    guess_entry.delete(0, 'end')

    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess == random_number:
            messagebox.showinfo("Congratulations", f"Yess!! You got it in {guesses} guesses!")
            window.quit()
        
        elif user_guess > random_number:
            messagebox.showinfo("Guess Result", "You were above the number")
            guesses += 1
                
        else:
            messagebox.showinfo("Guess Result", "You were below the number")
            guesses += 1
    else:
        messagebox.showinfo("Invalid Input", "Please type a number.")

seed = int(input("Enter a random number (integer): "))
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

window = tk.Tk()
window.title("Number Guessing Game")

label = tk.Label(window, text="Guess the number:")
label.pack(pady=10)

guess_entry = tk.Entry(window, width=10)
guess_entry.pack()

guess_button = tk.Button(window, text="Submit Guess", command=check_guess)
guess_button.pack(pady=10)

window.mainloop()
