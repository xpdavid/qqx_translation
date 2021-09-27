import tkinter as tk
from tkinter import ttk


def analysis_progress(window, store):
    store['progress_label'] = tk.Label(window, text="0%")
    store['progress_label'].pack()
    store['progress'] = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=100, mode='determinate')
    store['progress'].pack()


def set_value(value, store):
    store['progress_label'].config(text='{}%'.format(value))
    store['progress']['value'] = value
