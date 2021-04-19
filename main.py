import pandas as pd
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"
word = {}

#Getting the french word
data = pd.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")
learned_words = []


#Initialize the front side of the card
def frontside():
    global word, turn_wait, learned_words
    words_to_learn = [ch for ch in data_dict if ch not in learned_words]
    window.after_cancel(turn_wait)
    word = random.choice(words_to_learn)
    fr_word = word["French"]
    canvas.itemconfig(card_face, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=fr_word, fill="black")
    turn_wait = window.after(3000, backside)

#Shows the backside of the card
def backside():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word["English"], fill="white")
    canvas.itemconfig(card_face, image=card_back)



#saves the learned words
def learned():
    global learned_words, word
    learned_words.append(word)
    frontside()



#GUI
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
turn_wait =window.after(3000 ,frontside)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_face = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text="", fill="black",font=('Ariel 40 italic'))
card_word = canvas.create_text(400, 263, text="", fill="black",font=('Ariel 60 bold'))
canvas.grid(row=0, column=0, columnspan=2)


right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=learned)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=frontside)
wrong_button.grid(row=1, column=1)


frontside()#starts with a card

window.mainloop()


