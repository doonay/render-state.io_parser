from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x150") 
 
value_var = IntVar(value=30)
 
progressbar =  ttk.Progressbar(orient="horizontal", variable=value_var)
progressbar.pack(fill=X, padx=6, pady=6)
 
label = ttk.Label(textvariable=value_var)
label.pack(anchor=NW, padx=6, pady=6)
 
root.mainloop()