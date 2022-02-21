from tkinter import *


# App Window
window = Tk()
canvas = Canvas(window, width=150, height=700)
window.title("Etsy Price Calculator")
window.configure(background="grey", padx=10, pady=10)

# Global Variables- Mostly to avoid weak warnings :P
text1 = StringVar()
text2 = StringVar()
text3 = IntVar()
# whole = StringVar()

ischecked1 = IntVar()


# Welcome message
intro = Label(window, text='Welcome to the Etsy price calculator!', font=35, bg="grey", fg="white", pady=10)
intro.grid(row=0, column=0, sticky=W, pady=5, padx=5)

# # 1st Calculation
# Whole Frame
lf1 = LabelFrame(window, text="Cost + Profit", bg="grey", fg="white")
lf1.grid(column=0, row=1, padx=10, pady=10)
# 1st Question


def click1():
    return text1.get()


click1()


inv = Label(lf1, text="How much did we pay for the item? :", bg="gray", fg="white")
inv.grid(row=1, column=0, sticky=W, pady=5, padx=5)

textentry1 = Entry(lf1, textvariable=text1, width=50, bg="white", fg="black")
textentry1.grid(row=2, column=0, sticky=W, padx=5)

btn1 = Button(lf1, text="Submit", width=6, command=click1)
btn1.grid(row=2, column=1, sticky=E, pady=5, padx=5)


# 2nd Question
prof = Label(lf1, text="How much profit would you like to get out of each sale? :", bg="gray", fg="white")
prof.grid(row=3, column=0, sticky=W, pady=5, padx=5)

textentry2 = Entry(lf1, textvariable=text2, width=50, bg="white", fg="black")
textentry2.grid(row=4, column=0, sticky=W, padx=5)


def click2():
    return text2.get()


click2()


btn2 = Button(lf1, text="Submit", width=6, command=click2)
btn2.grid(row=4, column=1, sticky=E, pady=5, padx=5)

# Cost + Profit Button


def click3():
    whole = (float(click1()) + float(click2()))
    lwhole.configure(text=whole)


lwhole = Label(lf1, text="result", bg="white", fg="black")
lwhole.grid(row=5, column=1, sticky=W, pady=5, padx=5)
btn3 = Button(lf1, text="Cost + Profit", width=10, command=click3)
btn3.grid(row=5, column=0, sticky=E, pady=5, padx=5)

# # Weight estimate
# Size Frame
lf2 = LabelFrame(window, text="Shipping", bg="grey", fg="white")
lf2.grid(row=6, column=0, padx=10, pady=10)

# Size Question Label
size = Label(lf2, text="Will the shipping box fit the Normal/Registrado requirements?", bg="gray", fg="white")
size.grid(row=0, column=0, pady=5, padx=5, sticky=W)

# Checkbuttons


def click4():
    return text3.get()


click4()

grams1 = int(click4())
ischecked1.set(1)


def checkbox_yes():
    if ischecked1.get() == 1:
        if 0 < grams1 < 250:
            shipping = 8
            print(grams1)


checkbox_yes()


def checkbox_no():
    if ischecked1.get() == 2:
        print("no")
        shipping = 50
        print(shipping)


rb1 = Radiobutton(lf2, text="Yes", command=checkbox_yes, variable=ischecked1, value=1)
rb1.grid(row=0, column=2)
rb2 = Radiobutton(lf2, text="No", command=checkbox_no, variable=ischecked1, value=2)
rb2.grid(row=0, column=3, sticky=W)

# Weight Question Label
weight = Label(lf2, text="How much does the item weigh in grams?", bg="gray", fg="white")
weight.grid(row=2, column=0, pady=5, padx=5, sticky=W)


textentry3 = Entry(lf2, textvariable=text3, width=50, bg="white", fg="black")
textentry3.grid(row=3, column=0, sticky=W, padx=5)

btn4 = Button(lf2, text="Submit", width=6, command=click4)
btn4.grid(row=3, column=1, sticky=E, pady=5, padx=5)


# Loop Closer
window.mainloop()


# Functional Cli App

base_cost = 0
desired = 0
fees = 0


# App Mechanics

def weight():
    size = input("Will the shipping box fit the Normal/Registrado requirements (ENTER = yes / 0 = no ? :")
    if size == "":
        grams = int(input("How much does the item weigh in grams? :"))
        global shipping
        if 0 < grams < 250:
            shipping = 8
        if 251 < grams < 500:
            shipping = 12
        if 501 < grams < 1000:
            shipping = 18
        if 1001 < grams < 2000:
            shipping = 23
        if grams >= 2000:
            shipping = 30
    else:
        shipping = 50
    return


weight()


def cost():
    global base_cost
    #base_cost = (shipping + whole)
    return


cost()


def percentage():
    print("The total cost including materials, profit and shipping is " + str(base_cost) + "euros.")
    global desired
    desired = input("Considering this, what price seems fitting? :")
    percent = 15
    global fees
    fees = percent * float(desired) / 100.0


percentage()


print("Listing this item at " + str(desired) + " euros will cost you " + str(fees) + "euros in fees.")
