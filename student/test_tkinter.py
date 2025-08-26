import tkinter as tk

window = tk.Tk()
window.title("Test Window")
window.geometry("300x150")

label = tk.Label(window, text="Tkinter is working!")
label.pack()

window.mainloop()
