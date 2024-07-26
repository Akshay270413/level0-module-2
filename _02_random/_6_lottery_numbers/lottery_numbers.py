import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    name = random.randint(1, 100)
    name1 = random.randint(1, 100)
    name2 = random.randint(1, 100)
    name3 = random.randint(1, 100)
    name4 = random.randint(1, 100)
    name5 = random.randint(1, 100)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title='greeter', message=str(name)+" "+str(name1)+" "+str(name2)+" "+str(name3)+" "+str(name4)+" "+str(name5))
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
