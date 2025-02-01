import random
import tkinter as tk
from tkinter import messagebox
attempts_left=5
random_number=random.randint(1,100)
def guess():
    global attempts_left
    try:
        user_guess=int(entry.get())
        if user_guess < random_number:
            attempts_left-=1
            messagebox.showinfo("Result",f"Too low! {attempts_left} attempts left.")
        elif user_guess > random_number:
            attempts_left-=1
            messagebox.showinfo("Result",f"Too high! {attempts_left} attempts left.")
        else:
            messagebox.showinfo("Result","Congratulations! You guessed it right.")
            reset_game()
            return
        if attempts_left==0:
            messagebox.showinfo("Game Over",f"You lost! The number was {random_number}.")
            reset_game()
    except ValueError:
        messagebox.showwarning("Error","Please enter a valid number.")
def reset_game():
    global attempts_left, random_number
    attempts_left=5
    random_number=random.randint(1, 100)
    entry.delete(0, tk.END)
    messagebox.showinfo("New Game","New game started! You have 5 attempts.")
root=tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x250")
label=tk.Label(root, text="Guess a number between 1 and 100:",font=("Arial", 12))
label.pack(pady=10)
entry=tk.Entry(root, font=("Arial",12))
entry.pack(pady=5)
button_check=tk.Button(root,text="Check",command=guess,font=("Arial", 12))
button_check.pack(pady=5)
button_reset=tk.Button(root,text="Reset",command=reset_game,font=("Arial", 12),fg="white",bg="red")
button_reset.pack(pady=5)
root.mainloop()
