import tkinter as tk

from qqx.gui import position


def create_window(parent_window, store):
    if 'log' not in store:
        return

    new_window = tk.Toplevel(parent_window)

    log_text = tk.Text(new_window, height=16)
    log_text.insert(tk.END, '\n'.join(store['log']))
    log_text.pack()

    position.center_window(new_window)

    new_window.mainloop()
