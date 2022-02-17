from tkinter import *


# App Window
window = Tk()
canvas = Canvas(window, width=300, height=500)
window.title("Etsy Price Calculator")
window.configure(background="black")

# Global Variables- Mostly to avoid weak warnings :P

whole = float(0)

# Welcome message
intro = Label(window, text='Welcome to the etsy price calculator!', bg="black", fg="white")
intro.grid(row=0, column=0, sticky=W)

# # 1st Calculation
# 1st Question

inv = Label(window, text="How much did we pay for the item? :", bg="gray", fg="white")
inv.grid(row=1, column=0, sticky=W)

textentry1 = Entry(window, width=70, bg="white", fg="black")
textentry1.grid(row=2, column=0, sticky=W)
invinput: float = textentry1.get()


def click1():
    invinput: float = textentry1.get()
    print(invinput)


click1()


btn1 = Button(window, text="Submit", width=6, command=click1)
btn1.grid(row=2, column=1, sticky=E)


# 2nd Question
prof = Label(window, text="How much profit would you like to get out of each sale? :", bg="gray", fg="white")
prof.grid(row=3, column=0, sticky=W)

textentry2 = Entry(window, width=70, bg="white", fg="black")
textentry2.grid(row=4, column=0, sticky=W)
profinput: float = textentry2.get()


def click2():
    profinput: float = textentry2.get()
    print(profinput)
    whole1 = invinput + profinput



click2()

whole1 = invinput + profinput
btn2 = Button(window, text="Submit", width=6, command=click2)
btn2.grid(row=4, column=1, sticky=E)


def click3():
    print(invinput + profinput)


click3()


btn3 = Button(window, text="BTN3", width=6, command=click3)
btn3.grid(row=5, column=2, sticky=E)
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
    #whole = (float(investment) + float(profit))
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

