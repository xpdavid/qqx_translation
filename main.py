import tkinter as tk
from qqx.gui import position, output, progress, analysis

store = {}
window = tk.Tk()

position.center_window(window, height=300)
output.output_boxes(window, store)
progress.analysis_progress(window, store)
analysis.button(window, store)

window.title("千秋戏图像识别")

window.mainloop()
