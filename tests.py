import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

for i in range(1, 16):
    label = tk.Label(frame, text=f"Variable {i}")
    label.grid(column=0, row= i)

root.mainloop()