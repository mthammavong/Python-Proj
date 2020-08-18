"""Lunch Order Menu

Author: Michael Thammavong
Date: 8/5/2020

"""

from tkinter import *
from PIL import ImageTk,Image 



window = Tk()
window.title("Lunch Order")
window.geometry('550x420')  # Width x Height
window.resizable(0, 0)  # Don't allow resizing in the x or y direction

"""
# Gets the requested values of the height and width.
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
#print("Width",windowWidth,"Height",windowHeight)

# Gets both half the screen width/height and window width/height
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the page.
window.geometry("+{}+{}".format(positionRight, positionDown))
"""

# Main Course Frame
my_frame_1 = Frame(window, bd=2).grid()
label_frame = LabelFrame(my_frame_1, text="Main Course", font=('bold', 12))
label_frame.grid(sticky=W, column=0, row=0, padx=30, pady=50)

# Def function selection
selected = IntVar()


def img_selected():
    if selected.get() == 2:
        pizza = ImageTk.PhotoImage(Image.open("pizza_slice.png"))
        ham.config(image=pizza)
        ham.image = pizza
        label_frame5.grid_remove()
        label_frame3.grid_remove()
        label_frame4.grid(column=1, row=0, padx=50)

    if selected.get() == 3:
        lettuce = ImageTk.PhotoImage(Image.open("lettuce.png"))
        ham.config(image=lettuce)
        ham.image = lettuce
        label_frame3.grid_remove()
        label_frame4.grid_remove()
        label_frame5.grid(column=1, row=0, padx=50)

    if selected.get() == 1:
        hamburger = ImageTk.PhotoImage(Image.open("hamburger.png"))
        ham.config(image=hamburger)
        ham.image = hamburger
        label_frame4.grid_remove()
        label_frame5.grid_remove()
        label_frame3.grid(column=1, row=0, padx=50)


# Radiobutton selection
# add radio buttons to my_frame_1
Radiobutton(label_frame, text='Hamburger - $6.95', value=1, variable=selected, command=img_selected,
            font=("Helvetica", 10)).pack(side=TOP, anchor=W)
Radiobutton(label_frame, text='Pizza - $5.95', value=2, variable=selected, command=img_selected,
            font=("Helvetica", 10)).pack(side=TOP, anchor=W)
Radiobutton(label_frame, text='Salad - $4.95', value=3, variable=selected, command=img_selected,
            font=("Helvetica", 10)).pack(side=TOP, anchor=W)
selected.set(1)

# Add-on hamburger condiments to my_frame_2
my_frame_2 = Frame(window, bd=2, padx=10).grid()
label_frame3 = LabelFrame(my_frame_2, text="Add-ons ($.25/each)", font=('bold', 12))
label_frame3.grid(column=1, row=0, padx=50)

# Hamburger Condiments
chk_state1 = IntVar()
Checkbutton(label_frame3, text='Lettuce, tomato, and onions', variable=chk_state1, onvalue=1, offvalue=0,
            font=("Helvetica", 10)).pack(anchor=W)
chk_state2 = IntVar()
Checkbutton(label_frame3, text='Mayonnaise', variable=chk_state2, onvalue=1, offvalue=0, font=("Helvetica", 10)).pack(
    anchor=W)
chk_state3 = IntVar()
Checkbutton(label_frame3, text='Mustard', variable=chk_state3, onvalue=1, offvalue=0, font=("Helvetica", 10)).pack(
    anchor=W)

# Add-on pizza condiments to my_frame_6
# Pizza Condiments
my_frame_6 = Frame(window, bd=2, padx=5)
label_frame4 = LabelFrame(my_frame_2, text="Add-ons ($.25/each)", font=('bold', 12))
label_frame4.grid(column=1, row=0, padx=50)

chk_state4 = IntVar()
Checkbutton(label_frame4, text='Pepperoni', variable=chk_state4, onvalue=1, offvalue=0, font=("Helvetica", 10)).pack(
    anchor=W)
chk_state5 = IntVar()
Checkbutton(label_frame4, text='Sausage', variable=chk_state5, onvalue=1, offvalue=0, font=("Helvetica", 10)).pack(
    anchor=W)
chk_state6 = IntVar()
Checkbutton(label_frame4, text='Mushrooms', variable=chk_state6, onvalue=1, offvalue=0, font=("Helvetica", 10)).pack(
    anchor=W)

# Add-on salad condiments to my_frame_7
my_frame_7 = Frame(window, bd=2, padx=5)
label_frame5 = LabelFrame(my_frame_2, text="Add-ons ($.25/each)", font=('bold', 12))
label_frame5.grid(column=1, row=0, padx=50)

chk_state7 = IntVar()
Checkbutton(label_frame5, text='Croutons', variable=chk_state7, onvalue=1, offvalue=0, font=("Helvetica", 10)).pack(
    side=TOP, anchor=W)
chk_state8 = IntVar()
Checkbutton(label_frame5, text='Bacon bits', variable=chk_state8, onvalue=1, offvalue=0, font=("Helvetica", 10)).pack(
    side=TOP, anchor=W)
chk_state9 = IntVar()
Checkbutton(label_frame5, text='Bread sticks', variable=chk_state9, onvalue=1, offvalue=0, font=("Helvetica", 10)).pack(
    side=TOP, anchor=W)

# Default Condiments Checkbox
chk_state1.set(1), chk_state2.set(0), chk_state3.set(1)

my_frame_3 = Frame(window, bd=2).grid()
label_frame1 = LabelFrame(my_frame_3, text="Order Total", font=('bold', 12))
label_frame1.grid(column=0, row=2, padx=30)

# Declare initial types
sub_total = DoubleVar()
tax1 = DoubleVar()
tot_due = DoubleVar()

Label(label_frame1, text="Subtotal: ", font=("Helvetica", 10)).grid(sticky=W, column=0, row=0, padx=3, pady=12)
Label(label_frame1, textvariable=sub_total, width=5, bg='#e6f9ff', font=("Helvetica", 11)).grid(column=1, row=0,
                                                                                                padx=10)
Label(label_frame1, text="Sales Tax (.0825%) ", font=("Helvetica", 10)).grid(sticky=W, column=0, row=1, padx=3, pady=3)
Label(label_frame1, textvariable=tax1, width=5, bg='#e6f9ff', font=("Helvetica", 11)).grid(column=1, row=1, padx=10)
Label(label_frame1, text="Total Due: ", font=("Helvetica", 10)).grid(sticky=W, column=0, row=2, padx=3, pady=3)
Label(label_frame1, textvariable=tot_due, width=5, bg='#e6f9ff', font=("Helvetica", 11)).grid(column=1, row=2, padx=10,
                                                                                              pady=10)


# Button commands
def place_order():
    # Declare variables
    hamBurger = 6.95
    pizza = 5.95
    salad = 4.95
    addons = 0

    # If hamburger is selected do calculation
    if selected.get() == 1:

        if chk_state1.get():
            addons += .25
        if chk_state2.get():
            addons += .25
        if chk_state3.get():
            addons += .25

        subTotal = hamBurger + addons
        tax = subTotal * .0825
        totalDue = subTotal + tax

        # print('$'+ format(totalDue, ',.2f')) This will print to terminal console
        sub_total.set('$' + format(subTotal, ',.2f')), tax1.set('$' + format(tax, ',.2f')), tot_due.set(
            '$' + format(totalDue, ',.2f'))

    # If Pizza is selected do calculation
    if selected.get() == 2:
        if chk_state4.get():
            addons += .25
        if chk_state5.get():
            addons += .25
        if chk_state6.get():
            addons += .25

        subTotal = pizza + addons
        tax = subTotal * .0825
        totalDue = subTotal + tax

        # print('$'+ format(totalDue, ',.2f')) This will print to terminal console
        sub_total.set('$' + format(subTotal, ',.2f')), tax1.set('$' + format(tax, ',.2f')), tot_due.set(
            '$' + format(totalDue, ',.2f'))

    # If Salad is selected do calculation
    if selected.get() == 3:
        if chk_state7.get():
            addons += .25
        if chk_state8.get():
            addons += .25
        if chk_state9.get():
            addons += .25

        subTotal = salad + addons
        tax = subTotal * .0825
        totalDue = subTotal + tax

        # print('$'+ format(totalDue, ',.2f')) This will print to terminal console
        sub_total.set('$' + format(subTotal, ',.2f')), tax1.set('$' + format(tax, ',.2f')), tot_due.set(
            '$' + format(totalDue, ',.2f'))


# add button widget to my_frame_4
my_frame_4 = Frame(window)
my_frame_4.grid(column=1, row=4, pady=10)


# This will clear check box and clear calculations  - Updated 7/16/20 to clear all check boxes
def clear_order():
    sub_total.set(""), tax1.set(""), tot_due.set(""), chk_state1.set(0), chk_state2.set(0), chk_state3.set(
        0), chk_state4.set(0), chk_state5.set(0), chk_state6.set(0),
    chk_state7.set(0), chk_state8.set(0), chk_state9.set(0)


# Place order, Clear order and Exit Button
Button(my_frame_4, text='Place Order', width=9, font=("Helvetica", 10), command=place_order).pack(side=LEFT, padx=2,
                                                                                                  pady=1)

Button(my_frame_4, text='Clear Order', width=9, font=("Helvetica", 10), command=clear_order).pack(side=LEFT, padx=2,
                                                                                                  pady=1)

Button(my_frame_4, text='Exit', width=9, font=("Helvetica", 10), command=exit).pack(side=LEFT, padx=2, pady=1)

# Image Frame
my_frame_5 = Frame(window)
my_frame_5.grid(column=1, row=2)

# Default image on Menu Order
hamburger = ImageTk.PhotoImage(Image.open("hamburger.png"))
ham = Label(my_frame_5, image=hamburger)
ham.pack(side=RIGHT, padx=1)

# These two lines of code will hide pizza and salad frame as default
label_frame4.grid_remove()
label_frame5.grid_remove()

window.mainloop()
