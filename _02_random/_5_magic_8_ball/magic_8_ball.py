import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer

    # Make a variable and initialize it to a random number between 0 and 3
name1 = simpledialog.askinteger(title='greeter', prompt="Pick a number between 0 and 3")

    # If the random number is 0
if name1 =="0":
    messagebox.showinfo(title='greeter', message="Yes")
    if name1 == "1":
        messagebox.showinfo(title='greeter', message="No")
    if name1 == "2":
        messagebox.showinfo(title='greeter', message="Maybe, you should ask google")
    if name1 == "3":
            messagebox.showinfo(title='greeter', message="Think about it again")

        # tell the user "Yes"

    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
