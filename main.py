from tkinter import *


# App Window
window = Tk()
canvas = Canvas(window, width=300, height=500)
window.title("Etsy Price Calculator")
window.configure(background="black")


# Text
intro = Label(window, text='Welcome to the etsy price calculator!', bg="black", fg="white")
intro.grid(row=0, column=0, sticky=W)

textentry1 = Entry(window, width=70, bg="white")
textentry1.grid(row=1, column=0, sticky=W)
btn1 = Button(window, text="Submit", width=6, command=print("Hi"))
btn1.grid(row=1, column=1, sticky=E)

window.mainloop()
# App Mechanics

whole = 0
shipping = 0
base_cost = 0
desired = ""
fees = ""


# App Mechanics
def cost_profit_input():
    investment = input("How much did we pay for the item? :")
    profit = input("How much profit would you like to get out of each sale? :")
    global whole
    whole = (float(investment) + float(profit))
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


print("Listing this item at " + desired + " euros will cost you " + str(fees) + "euros in fees.")
