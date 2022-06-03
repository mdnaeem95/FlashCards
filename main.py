from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOUR = "#B1DDC6"
current_card = {}
to_learn = {}

# ------------ Generating random words from CSV file ----------------- #
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card_wrong():

    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card, image=card_pic)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    timer = window.after(3000, func=flip_card)


def next_card_correct():

    to_learn.remove(current_card)
    next_card_wrong()
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)


def flip_card():

    canvas.itemconfig(card, image=flipped_card)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')


# ------------------- UI Setup ------------------ #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, width=900, height=630, bg=BACKGROUND_COLOUR)

timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOUR)
card_pic = PhotoImage(file='C:/Users/User/PycharmProjects/Flash Cards/images/card_front.png')
flipped_card = PhotoImage(file='C:/Users/User/PycharmProjects/Flash Cards/images/card_back.png')
card = canvas.create_image(400, 263, anchor='center', image=card_pic)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text='', font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

correct_image = PhotoImage(file='C:/Users/User/PycharmProjects/Flash Cards/images/right.png')
correct_button = Button(image=correct_image, highlightthickness=0, command=next_card_correct)
correct_button.grid(row=1, column=1)

wrong_image = PhotoImage(file='C:/Users/User/PycharmProjects/Flash Cards/images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card_wrong)
wrong_button.grid(row=1, column=0)

next_card_wrong()

window.mainloop()
