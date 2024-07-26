import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment
    for i in range(10):
        name = simpledialog.askinteger(title='greeter', prompt="enter a number")
        if name=="1":
            messagebox.showinfo(title='greeter', message="you are nice")
        else:
            messagebox.showinfo(title='greeter', message="you are smart")




    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
