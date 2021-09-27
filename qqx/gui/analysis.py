import threading
import tkinter as tk
from tkinter import messagebox

import numpy as np
from PIL import ImageGrab

from qqx.gui import progress, output
from qqx.gui.debug import image_debug
from qqx.gui.debug import log_debug
from qqx.logic import core


def button(window, store):
    # Analysis
    store['btn'] = tk.Button(window, text='分析', bd='5', command=lambda: on_click(window, store))
    store['btn'].pack()

    store['is_robust'] = tk.IntVar()
    store['is_robust_chk'] = tk.Checkbutton(window, text="超级分析（贼慢）", variable=store['is_robust'])
    store['is_robust_chk'].pack()

    # Debug
    debug_frame = tk.Frame(window)
    store['btn_debug'] = tk.Button(debug_frame, text='图像', bd='5',
                                   command=lambda: image_debug.create_window(window, store))
    store['btn_debug'].pack(side=tk.LEFT)
    store['btn_debug_log'] = tk.Button(debug_frame, text='日志', bd='5',
                                       command=lambda: log_debug.create_window(window, store))
    store['btn_debug_log'].pack(side=tk.RIGHT)
    debug_frame.pack()


def set_disable(store):
    store['btn']['state'] = 'disabled'
    store['btn_debug']['state'] = 'disabled'
    store['btn_debug_log']['state'] = 'disabled'
    store['is_robust_chk'].config(state=tk.DISABLED)


def set_enable(store):
    store['btn']['state'] = 'normal'
    store['btn_debug']['state'] = 'normal'
    store['btn_debug_log']['state'] = 'normal'
    store['is_robust_chk'].config(state=tk.NORMAL)


def update_progress_bar(val, store, window):
    progress.set_value(val, store)
    window.update()


def logger(log, store):
    print(log)
    store['log'].append(str(log))


def on_click(window, store):
    im = ImageGrab.grabclipboard()
    if im is None:
        messagebox.showwarning('错误', '剪切板内没有图像')
        return

    # init state
    set_disable(store)
    store['log'] = []

    threading.Thread(target=run_analysis, args=(im, store, window)).start()


def run_analysis(im, store, window):
    try:
        public_cards, my_cards, img_rgb = core.process(
            np.array(im),
            progress_updater=lambda val: update_progress_bar(val, store, window),
            logger=lambda log: logger(log, store),
            is_robust=store['is_robust'].get()
        )
        store['img_rgb'] = img_rgb
        output.set_my_cards(my_cards, store)
        output.set_public_cards(public_cards, store)
    except Exception:
        messagebox.showwarning('分析出错', '请查看日志')
    finally:
        set_enable(store)
