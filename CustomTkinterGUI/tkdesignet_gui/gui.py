from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox
import re
from tkdesigner.designer import Designer
'''
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("img/")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
'''
def btn_clicked():
    #token = token_entry.get() #забираем токен из поля для ввода токена
    token = 'figd_TEhZLBnnuki3Pnh4y0fMY8X4Gt26N8yLAT1LLa_a'
    #URL = URL_entry.get() #забираем урл из поля для ввода урлы
    URL = 'https://www.figma.com/file/HAwfAa8jOWo5b4bUjnNEEx/Untitled'
    #output_path = path_entry.get()#забираем путь из поля для ввода пути
    output_path = 'build/'
    output_path = output_path.strip()#чистим путь

    if not token:
        messagebox.showerror(
            title="Empty Fields!", message="Please enter Token.")
        return
    if not URL:
        messagebox.showerror(
            title="Empty Fields!", message="Please enter URL.")
        return
    if not output_path:
        messagebox.showerror(
            title="Invalid Path!", message="Enter a valid output path.")
        return

    match = re.search(r'https://www.figma.com/file/([0-9A-Za-z]+)', URL.strip())
    if match is None:
        messagebox.showerror("Invalid URL!", "Please enter a valid file URL.")
        return
    file_key = match[1].strip()
    token = token.strip()
    output = Path(f"{output_path}").expanduser().resolve()

    if output.exists() and not output.is_dir():
        messagebox.showerror(
            "Exists!",
            f"{output} already exists and is not a directory.\n"
            "Enter a valid output directory.")
    elif output.exists() and output.is_dir() and tuple(output.glob('*')):
        response = messagebox.askyesno(
            "Continue?",
            f"Directory {output} is not empty.\n"
            "Do you want to continue and overwrite?")
        if not response:
            return

    designer = Designer(token, file_key, output)
    designer.design()

    messagebox.showinfo("Success!", f"Project successfully generated at {output}.")

window = Tk()
window.geometry("356x106")
window.configure(bg = "#58805A")
canvas = Canvas(window,bg = "#58805A",height = 106,width = 356,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)
canvas.create_text(10.0,11.0,anchor="nw",text="Figma link:",fill="#000000",font=("Inter", 12 * -1))
canvas.create_text(10.0,32.0,anchor="nw",text="Figma token:",fill="#000000",font=("Inter", 12 * -1))
canvas.create_text(10.0,54.0,anchor="nw",text="Result path:",fill="#000000",font=("Inter", 12 * -1))
entry_bg_1 = canvas.create_image(219.0,15.5)
URL_entry = Entry(bd=0,bg="#BBA9A9",fg="#000716",highlightthickness=0)
URL_entry.place(x=93.0,y=10.0,width=252.0,height=9.0)
entry_bg_2 = canvas.create_image(219.0,37.5)
token_entry = Entry(bd=0,bg="#BBA9A9",fg="#000716",highlightthickness=0)
token_entry.place(x=93.0,y=32.0,width=252.0,height=9.0)
entry_bg_3 = canvas.create_image(219.0, 59.5)
path_entry = Entry(bd=0,bg="#BBA9A9",fg="#000716",highlightthickness=0)
path_entry.place(x=93.0,y=54.0,width=252.0,height=9.0)
button_image_1 = PhotoImage(file="img/button_1.png")
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
button_1.place(x=131.0, y=76.0, width=95.0, height=19.0)
window.resizable(False, False)
window.mainloop()
