from tkinter import *
from random import *

initiative_track = []
label_list = []

# Make some functions


def add():
    if character_entry.get() != "":

        character_text = character_entry.get()
        roll_text = roll_entry.get()

        initiative_track.append(roll_text.zfill(2) + " " + character_text)
        initiative_track.sort(reverse=True)

        for z in label_list:
            z.destroy()

        list_position = 0
        for x in initiative_track:
            list_position += 1
            global initiative_list
            initiative_list = Label(window, text=x, font="none 12 bold")
            initiative_list.grid(row=10 + list_position, column=0, sticky=W)
            label_list.append(initiative_list)

        character_entry.delete(0, END)
        roll_entry.delete(0, END)


def roll():
    if character_entry.get() != "":

        character_text = character_entry.get()
        if modifier_entry.get() == "":
            modifier_text = 0
        else:
            modifier_text = modifier_entry.get()
        roll_text = randint(1, 20) + int(modifier_text)

        initiative_track.append(str(roll_text).zfill(2) + " " + character_text)
        initiative_track.sort(reverse=True)

        for z in label_list:
            z.destroy()

        list_position = 0
        for x in initiative_track:
            list_position += 1
            global initiative_list
            initiative_list = Label(window, text=x, font="none 12 bold")
            initiative_list.grid(row=10 + list_position, column=0, sticky=W)
            label_list.append(initiative_list)

        character_entry.delete(0, END)
        modifier_entry.delete(0, END)


def clear():

    initiative_track.clear()
    for x in label_list:
        x.destroy()
    label_list.clear()


def toggle_ontop():

    if ontop_toggle.config('text')[-1] == 'Enable always on top':
        ontop_toggle.config(text="Disable always on top")
        window.wm_attributes("-topmost", 1)
    else:
        ontop_toggle.config(text="Enable always on top")
        window.wm_attributes("-topmost", 0)


# main:
window = Tk()
window.title("Initiative Tracker")

# Create Labels
Label(window, text="Character:", fg="black", font="none 12 bold") .grid(row=1, column=0, sticky=W)
Label(window, text="Result:", fg="black", font="none 12 bold") .grid(row=1, column=2, sticky=W)
Label(window, text="Modifier:", fg="black", font="none 12 bold") .grid(row=2, column=2, sticky=W)
Label(window, text="Initiative Order:", fg="black", font="none 12 bold") .grid(row=10, column=0, columnspan=2, sticky=W)

# Create a text entry box
character_entry = Entry(window, width=15, bg="white")
character_entry.grid(row=1, column=1, sticky=W)
roll_entry = Entry(window, width=5, bg="white")
roll_entry.grid(row=1, column=3, sticky=W)
modifier_entry = Entry(window, width=5, bg="white")
modifier_entry.grid(row=2, column=3, sticky=W)

# Create some buttons
Button(window, text="Add", width=10, command=add) .grid(row=1, column=4, padx=10, pady=10, sticky=W)
Button(window, text="Roll", width=10, command=roll) .grid(row=2, column=4, padx=10, pady=10, sticky=W)
Button(window, text="Clear", width=10, command=clear) .grid(row=4, column=0, padx=10, pady=10, sticky=W)
ontop_toggle = Button(window, text="Enable always on top", width=20, command=toggle_ontop)
ontop_toggle.grid(row=4, column=3, columnspan=2, padx=10, pady=10, sticky=W)

# Run the main loop
window.mainloop()
