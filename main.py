from tkinter import *
from random import *
import pandas

BACKGR0UND_COLOR = "#B1DDC6"
word_list = {}

# french_words = data.French.to_list()
try:
    with open("words_to_learn.csv") as data_file:
        data = pandas.read_csv('words_to_learn.csv')
        french_words = data.to_dict(orient='records')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
    french_words = (data.to_dict(orient='records'))
# print(french_words)


# Button Functionality
def next_card():
    global word_list, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=old_image)
    word_list = choice(french_words)
    french_word = word_list['French']
    canvas.itemconfig(title_text, text="French", fill='black')
    canvas.itemconfig(word_text, text=f'{french_word}', fill='black')
    flip_timer =  window.after(3000, flip_card)


def flip_card():
    english_word = word_list['English']
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=english_word, fill='white')


def is_known():
    french_words.remove(word_list)
    updated_data = pandas.DataFrame(french_words)
    updated_data.to_csv('words_to_learn.csv', index=False)
    next_card()


# UI Setup
window = Tk()
window.title('Flash Card Program')
window.config(padx=50, pady=50, bg=BACKGR0UND_COLOR)
flip_timer = window.after(3000, flip_card)


canvas = Canvas()
old_image = PhotoImage(file='images/card_front.png')
canvas.config(height=526, width=800, bg=BACKGR0UND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=old_image)
title_text = canvas.create_text(400, 150, text='Title', font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text='Word', font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

x_image = PhotoImage(file='images/wrong.png')
x_button = Button(image=x_image, highlightthickness=0, bg=BACKGR0UND_COLOR, command=next_card)
x_button.grid(row=1, column=0)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGR0UND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

next_card()


new_image = PhotoImage(file='images/card_back.png')



window.mainloop()


