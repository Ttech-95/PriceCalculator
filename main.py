from tkinter import *


# App Window
window = Tk()
canvas = Canvas(window, width=150, height=500)
window.title("Etsy Price Calculator")
window.configure(background="grey", padx=10, pady=10)

# Global Variables- Mostly to avoid weak warnings :P
text1 = StringVar()
text2 = StringVar()

# Welcome message
intro = Label(window, text='Welcome to the Etsy price calculator!', font=35, bg="grey", fg="white", pady=10)
intro.grid(row=0, column=0, sticky=W, pady=5, padx=5)

# # 1st Calculation
# 1st Question


def click1():
    return text1.get()


click1()


inv = Label(window, text="How much did we pay for the item? :", bg="gray", fg="white")
inv.grid(row=1, column=0, sticky=W, pady=5, padx=5)

textentry1 = Entry(window, textvariable=text1, width=70, bg="white", fg="black")
textentry1.grid(row=2, column=0, sticky=W, padx=5)

btn1 = Button(window, text="Submit", width=6, command=click1)
btn1.grid(row=2, column=1, sticky=E, pady=5, padx=5)


# 2nd Question
prof = Label(window, text="How much profit would you like to get out of each sale? :", bg="gray", fg="white")
prof.grid(row=3, column=0, sticky=W, pady=5, padx=5)

textentry2 = Entry(window, textvariable=text2, width=70, bg="white", fg="black")
textentry2.grid(row=4, column=0, sticky=W, padx=5)


def click2():
    return textentry2.get()


click2()


btn2 = Button(window, text="Submit", width=6, command=click2)
btn2.grid(row=4, column=1, sticky=E, pady=5, padx=5)


#def click3():
#    print(float(click1()) + float(click2()))
#
#
#click2()
#
#
#btn3 = Button(window, text="Submit", width=6, command=click3)
#btn3.grid(row=5, column=1, sticky=E)

# Loop Closer
window.mainloop()


# Functional Cli App
shipping = 0
base_cost = 0
desired = 0
fees = 0


# App Mechanics


def cost_profit_input():

    investment = input("How much did we pay for the item? :")
    profit = input("How much profit would you like to get out of each sale? :")
    global whole
    # whole = (float(investment) + float(profit))
    return


cost_profit_input()


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
    base_cost = (shipping + whole)
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
