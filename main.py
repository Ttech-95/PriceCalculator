from tkinter import *
from tkinter import ttk

#App Window
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()

#App Mechanics
def cost_profit_input():
    cost = input("How much did we pay for the item? :")
    profit = input("How much profit would you like to get out of each sale? :")
    global whole
    whole = (float(cost) + float(profit))
    return
cost_profit_input()

def weight():
    size = input("Will the shipping box fit the Normal/Registrado requirements (ENTER = yes / 0 = no ? :")
    if size == "":
        grams = int(input("How much does the item weigh in grams? :"))
        global shipping
        if grams > 0 and grams < 250:
            shipping = 8
        if grams > 251 and grams < 500:
            shipping = 12
        if grams > 501 and grams < 1000:
            shipping = 18
        if grams > 1001 and grams < 2000:
            shipping = 23
        if grams >= 2000:
            shipping = 30
    else:
        shipping = 50
    return
weight()

def cost():
    global base_cost
    base_cost = ( shipping + whole)
    return
cost()

def percentage():
    print("The total cost including materials, profit and shipping is " + str(base_cost) +"euros.")
    global desired
    desired = input("Considering this, what price seems fitting? :")
    percent = 15
    global fees
    fees = percent * float(desired) / 100.0
percentage()


print ( "Listing this item at " + desired +" euros will cost you " + str(fees) + "euros in fees." )