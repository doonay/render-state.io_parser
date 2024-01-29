import sqlite3
#import tkinter as tk
from tkinter import *
#import tkinter.ttk as ttk
import customtkinter
from set_app_position import set_app_position




customtkinter.deactivate_automatic_dpi_awareness() # отключить автоматическое масштабирование
#customtkinter.set_window_scaling(float_value)  # window geometry dimensions
#customtkinter.set_widget_scaling(float_value)  # widget dimensions and text size
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
set_app_position(app)


app.title("CustomTkinter")     # устанавливаем заголовок окна

app.mainloop()
#app.geometry("400x240")
'''
def button_function():
    print("button pressed")
'''
# Use CTkButton instead of tkinter Button
#button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
#button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)






#app.geometry("400x150")
'''
button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)
'''

'''
class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
  
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings
  
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
  
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
  
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)
  
  
data = ()
with sqlite3.connect('render-state.db') as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM categories")
    data = (row for row in cursor.fetchall())



'''


'''

root = Tk()     # создаем корневой объект - окно
root.title("Приложение на Tkinter")     # устанавливаем заголовок окна
#root.geometry("300x250")    # устанавливаем размеры окна
 
label = Label(text="Hello METANIT.COM") # создаем текстовую метку
label.pack()    # размещаем метку в окне
 



table = Table(root, headings=('Id', 'Item_id', 'Category', 'Link', 'Count'), rows=data)
table.pack(expand=tk.YES, fill=tk.BOTH)
root.mainloop()
'''