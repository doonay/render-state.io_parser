from tkinter import *
from tkinter import messagebox
import sqlite3
root = Tk()
root.title("Подбор щеток AEZ.")
root.geometry('600x400')

def printRecords():
    connection = sqlite3.connect('render-state.db')
    cur = connection.cursor()

    cur.execute("SELECT * FROM categories WHERE id = ?", (wi.get(),))
    results = cur.fetchall()
    messagebox.showinfo("", results)
    print(results)

Label(root, text = "Введите ширину и высоту:      ").grid()


wi = Entry()
wi.grid(row=0,column=1, padx=5, pady=5)
root.update()

SearchButton = Button(root, text="Search", command=printRecords)
SearchButton.grid(row=0, column=2)

root.mainloop()