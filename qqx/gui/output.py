import tkinter as tk


def output_boxes(window, store):
    tk.Label(window, text="公共牌").pack()
    store['txt1'] = tk.Text(window, height=4)
    store['txt1'].pack()
    tk.Label(window, text="我方手牌").pack()
    store['txt2'] = tk.Text(window, height=4)
    store['txt2'].pack()


def set_public_cards(text, store):
    store['txt1'].delete(1.0, tk.END)
    store['txt1'].insert(tk.END, text)


def set_my_cards(text, store):
    store['txt2'].delete(1.0, tk.END)
    store['txt2'].insert(tk.END, text)
