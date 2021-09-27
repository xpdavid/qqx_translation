import tkinter as tk

from PIL import Image, ImageTk

from qqx.gui import position


def create_window(parent_window, store):
    if 'img_rgb' not in store:
        return

    new_window = tk.Toplevel(parent_window)
    height, width, _ = store['img_rgb'].shape

    img = ImageTk.PhotoImage(image=Image.fromarray(store['img_rgb']))

    canvas = tk.Canvas(new_window, width=width, height=height)
    canvas.pack()
    canvas.create_image(width / 2, height / 2, image=img)

    position.center_window(new_window, width=width, height=height)

    new_window.mainloop()
