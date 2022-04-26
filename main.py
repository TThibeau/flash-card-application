from email.mime import image
from tkinter import *
from random import randint,choice
from tkinter import font
import pandas
import os

os.system('cls || clear')
TIMER_LENGTH = 3
BACKGROUND_COLOR = "#B1DDC6"
FONT_IT = ("Ariel",40,"italic")
FONT_B = ("Ariel",60,"bold")
FONT_B_small = ("Ariel",30,"bold")
try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except:
    df = pandas.read_csv("./data/ko_en_list.csv")

to_learn = df.to_dict(orient="records")
current_card = {}

def remove_card():
    to_learn.remove(current_card)   # Remove the current card dict from to learn list
    try:
        data = pandas.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv",index=False)
        new_card()
    except:
        print("All flash cards have been processed. No more words to learn!")
        card_canvas.itemconfig(language_text,text="Done!") 
        card_canvas.itemconfig(word_text,text="You finished learning all words :)",font=FONT_B_small)
    

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card(english_word):
    global timer
    window.after_cancel(id=timer)
    card_canvas.itemconfig(card_img,image=card_back_img)
    card_canvas.itemconfig(language_text,text="English") 
    card_canvas.itemconfig(word_text,text=f"{english_word}")

# ---------------------------- NEW CARD ------------------------------- #
def new_card():
    global timer
    window.after_cancel(id=timer)
    kor,en = pick_random_card()
    card_canvas.itemconfig(card_img,image=card_front_img)
    card_canvas.itemconfig(language_text,text="Korean") 
    card_canvas.itemconfig(word_text,text=f"{kor}") 

    timer = window.after(TIMER_LENGTH*1000,flip_card,en)

# ---------------------------- PICK RANDOM CARD ----------------------- #
def pick_random_card():
    global current_card
    current_card = choice(to_learn)
    
    return current_card["korean"],current_card["english"]
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

# Card
card_canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_img = card_canvas.create_image(400,263,image=card_front_img)

language_text = card_canvas.create_text(400,150,font=FONT_IT)     
word_text = card_canvas.create_text(400,263,font=FONT_B)

card_canvas.grid(row=0,column=0,columnspan=2)

# Buttons
wrong_button = Button(image=wrong_img, highlightthickness=0,borderwidth=0, command=new_card)
wrong_button.grid(row=1,column=0)

right_button = Button(image=right_img, highlightthickness=0,borderwidth=0, command=remove_card)
right_button.grid(row=1,column=1)

timer = window.after(0,new_card)

# Countdown timer
# timer_text = card_canvas.create_text(650,50,fill="black",font=FONT_B)
window.mainloop()