import random
import sys
from tkinter import messagebox, Tk, simpledialog
from playsound import playsound

def crack_the_safe():
    pass
    # TODO: Your mission: Use the try_code method to crack the safe
    #  by trying all possible combinations


# ======================= DO NOT EDIT THE CODE BELOW =========================

random_code = random.randint(0, 999)


def try_code(guess):
    print("trying " + str(guess))

    secret_code = 999999 - hidden

    if guess == secret_code:
        messagebox.showinfo(None, "Congratulations! You cracked the safe with " + str(guess))
        play_the_sound_of_success()
        sys.exit(0)
def play_the_sound_of_success():
    playsound('me-gusta.wav')


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    crack_the_safe()
