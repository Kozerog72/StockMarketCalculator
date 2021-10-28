# "Calculator of Trader"

from tkinter import *

root = Tk()
root["bg"] = '#707070'
root.title("Trader's Calculator")
root.geometry("400x524")
root.resizable(False, False)


frame = LabelFrame(root, text=" Trading on Stock Market ", font='Times 20 bold', fg="#F8C729", bg="#707070")
frame.pack(padx=10, pady=10)

"""
    balance = float(e1.get())
    quantity_1 = float(e2.get())
    price_1 = float(e3.get())
    quantity_2 = float(e4.get())
    price_2 = float(e5.get())
    buy or sell side == 1 or 2 = e6.get()
    forecast = float(e7.get())
"""


def calculate1():
    result1 = float(e2.get()) * float(e3.get())

    order_1["text"] = round(result1, 2)

    print(f"0. Beginning Account Balance == {(round(float(e1.get()), 2))} USD")
    print(f"1. Total Value of Order_1 == {(round(result1, 2))} USD")


def calculate2():
    result2 = float(e4.get()) * float(e5.get())

    order_2["text"] = round(result2, 2)

    print(f"2. Total Value of Order_2 == {(round(result2, 2))} USD")


def calculate3():
    value1 = float(e2.get()) * float(e3.get())
    value2 = float(e4.get()) * float(e5.get())
    result3 = value1 + value2

    all_orders["text"] = round(result3, 2)

    print(f"3. Total Cost of All Orders == {(round(result3, 2))} USD")


def calculate4():
    x1 = float(e2.get()) * float(e3.get())
    x2 = float(e4.get()) * float(e5.get())
    x3 = float(e2.get()) + float(e4.get())

    result4 = (x1 + x2) / x3

    if result4 < 0:
        new_price["text"] = round(result4, 5)
    else:
        new_price["text"] = round(result4, 5)

    print(f"4. New Price Per Quantity == {(round(result4, 5))} USD")


def calculate5():
    x1 = float(e2.get()) * float(e3.get())
    x2 = float(e4.get()) * float(e5.get())

    result5 = float(e1.get()) - (x1 + x2)

    if result5 < 0:
        trading_power["text"] = f"-{(round(result5, 2))}"
    else:
        trading_power["text"] = round(result5, 2)

    print(f"5. Trading Power == {(round(result5, 2))} USD")


def calculate6():
    quantity1 = float(e2.get())
    quantity2 = float(e4.get())
    price1 = float(e3.get())
    price2 = float(e5.get())
    forecast = float(e7.get())

    value1 = quantity1 * price1
    value2 = quantity2 * price2

    price3 = (value1 + value2) / (quantity1 + quantity2)

    buy = (forecast * (quantity1 + quantity2)) - (price3 * (quantity1 + quantity2))
    sell = (price3 * (quantity1 + quantity2)) - (forecast * (quantity1 + quantity2))

    if e6.get() == "1":
        r1 = buy
        if r1 < 0:
            profit_loss["text"] = f"{(round(r1, 2))}"
            print(f"6.Buy. Loss == {(round(r1, 2))} USD")
        else:
            profit_loss["text"] = f"+{(round(r1, 2))}"
            print(f"6.Buy. Profit == {(round(r1, 2))} USD")

    else:
        r2 = sell
        if r2 < 0:
            profit_loss["text"] = f"{(round(r2, 2))}"
            print(f"6.Sell. Loss == {(round(r2, 2))} USD")
        else:
            profit_loss["text"] = f"+{(round(r2, 2))}"
            print(f"6.Sell. Profit == {(round(r2, 2))} USD")


def calculate7():
    quantity1 = float(e2.get())
    quantity2 = float(e4.get())
    price1 = float(e3.get())
    price2 = float(e5.get())
    balance = float(e1.get())
    forecast = float(e7.get())

    value1 = quantity1 * price1
    value2 = quantity2 * price2
    price3 = (value1 + value2) / (quantity1 + quantity2)

    buy = (forecast * (quantity1 + quantity2)) - (price3 * (quantity1 + quantity2))
    sell = (price3 * (quantity1 + quantity2)) - (forecast * (quantity1 + quantity2))

    if e6.get() == "1":
        r1 = balance + buy
        if buy < 0:
            new_balance["text"] = f"{(round(r1, 2))} (-)"
            print(f"7.Buy. New Account Balance = with Loss == {(round(r1, 2))} USD")
        else:
            new_balance["text"] = f"{(round(r1, 2))} (+)"
            print(f"7.Buy. New Account Balance = with Profit == {(round(r1, 2))} USD")
    else:
        r2 = balance + sell
        if sell < 0:
            new_balance["text"] = f"{(round(r2, 2))} (-)"
            print(f"7.Sell. New Account Balance = with Loss == {(round(r2, 2))} USD")
        else:
            new_balance["text"] = f"{(round(r2, 2))} (+)"
            print(f"7.Sell. New Account Balance = with Profit == {(round(r2, 2))} USD")


# Options:

l1 = Label(frame, text="Account Balance:", width=25, pady=5, fg="white", bg="#454545")
l1.grid(row=0, column=0)

e1 = Entry(frame, width=12, borderwidth=4, justify=CENTER)
e1.get()
e1.insert(0, '')
e1.grid(row=0, column=1)

l2 = Label(frame, text="Quantity of Order_1:", width=25, pady=5, fg="white", bg="#454545")
l2.grid(row=1, column=0)

e2 = Entry(frame, width=12, borderwidth=4, justify=CENTER)
e2.get()
e2.insert(0, '')
e2.grid(row=1, column=1)

l3 = Label(frame, text="Price Per Quantity:", width=25, pady=5, fg="white", bg="#454545")
l3.grid(row=2, column=0)

e3 = Entry(frame, width=12, borderwidth=4, justify=CENTER)
e3.get()
e3.insert(0, '')
e3.grid(row=2, column=1)

l4 = Label(frame, text="Quantity of Order_2:", width=25, pady=5, fg="white", bg="#454545")
l4.grid(row=3, column=0)

e4 = Entry(frame, width=12, borderwidth=4, justify=CENTER)
e4.get()
e4.insert(0, '')
e4.grid(row=3, column=1)

l5 = Label(frame, text="Price Per Quantity:", width=25, pady=5, fg="white", bg="#454545")
l5.grid(row=4, column=0)

e5 = Entry(frame, width=12, borderwidth=4, justify=CENTER)
e5.get()
e5.insert(0, '')
e5.grid(row=4, column=1)

l6 = Label(frame, text="Buy == 1 <> Sell == 2:", width=25, pady=5, fg="white", bg="#454545")
l6.grid(row=5, column=0)

e6 = Entry(frame, width=12, borderwidth=4, justify=CENTER)
e6.get()
e6.insert(0, '')
e6.grid(row=5, column=1)

l7 = Label(frame, text="Future Forecast:", width=25, pady=5, fg="white", bg="#454545")
l7.grid(row=6, column=0)

e7 = Entry(frame, width=12, borderwidth=4, justify=CENTER)
e7.get()
e7.insert(0, '')
e7.grid(row=6, column=1)

# Calculations:

c1 = Button(frame, text="Total Value of Order_1:", font='Helvetica 15 bold', width=25, pady=7, borderwidth=2,
            fg="#850000", command=calculate1)
c1.grid(row=7, column=0)

order_1 = Label(frame, width=13, pady=5, bg="#F8C729")
order_1.grid(row=7, column=1)
order_1.bind("<Button>", calculate1)

c2 = Button(frame, text="Total Value of Order_2:", font='Helvetica 15 bold', width=25, pady=7, borderwidth=2,
            fg="#850000", command=calculate2)
c2.grid(row=8, column=0)

order_2 = Label(frame, width=13, pady=5, bg="#F8C729")
order_2.grid(row=8, column=1)
order_2.bind("<Button>", calculate2)

c3 = Button(frame, text="Total Cost of All Orders:", font='Helvetica 15 bold', width=25, pady=7, borderwidth=2,
            fg="#850000", command=calculate3)
c3.grid(row=9, column=0)

all_orders = Label(frame, width=13, pady=5, bg="#F8C729")
all_orders.grid(row=9, column=1)
all_orders.bind("<Button>", calculate3)

c4 = Button(frame, text="New Price Per Quantity:", font='Helvetica 15 bold', width=25, pady=7, borderwidth=2,
            fg="#850000", command=calculate4)
c4.grid(row=10, column=0)

new_price = Label(frame, width=13, pady=5, bg="#F8C729")
new_price.grid(row=10, column=1)
new_price.bind("<Button>", calculate4)

c5 = Button(frame, text="Trading Power:", font='Helvetica 15 bold', width=25, pady=7, borderwidth=2,
            fg="#850000", command=calculate5)
c5.grid(row=11, column=0)

trading_power = Label(frame, width=13, pady=5, bg="#F8C729")
trading_power.grid(row=11, column=1)
trading_power.bind("<Button>", calculate5)

c6 = Button(frame, text="Forecast -- Profit or Loss:", font='Helvetica 15 bold', width=25, pady=7, borderwidth=2,
            fg="#850000", command=calculate6)
c6.grid(row=12, column=0)

profit_loss = Label(frame, width=13, pady=5, bg="#F8C729")
profit_loss.grid(row=12, column=1)
profit_loss.bind("<Button>", calculate6)

c7 = Button(frame, text="Account Balance - NEW:", font='Helvetica 15 bold', width=25, pady=7, borderwidth=2,
            fg="#850000", command=calculate7)
c7.grid(row=13, column=0)

new_balance = Label(frame, width=13, pady=5, bg="#F8C729")
new_balance.grid(row=13, column=1)
new_balance.bind("<Button>", calculate7)

root.mainloop()
