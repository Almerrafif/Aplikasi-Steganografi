from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()
root.title("Steganography - Hide a Secret Text Message In an Image")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#2f4115")

def show_image():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image file',
                                          filetype=(("PNG file", "*.png"),
                                                    ("JPG file", "*.jpg"),
                                                    ("All files", "*.*")))  # Changed "All file" to "All files" and "*.txt" to "*.*"
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image = img  # Changed "lbl.Image" to "lbl.image"

def hide_data():
    global secret
    message = Text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)

def show_data():
    clear_message = lsb.reveal(filename)
    Text1.delete(1.0, END)
    Text1.insert(END, clear_message)

def save_image():
    secret.save("hidden.png")

# icon
image_icon = PhotoImage(file="Logo-Siliwangi.png")
root.iconphoto(False, image_icon)

# logo
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)
Label(root, text="Steganography", bg="#2d4155", fg="white", font="Arial 25 bold").place(x=100, y=20)

# first frame
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

# second frame
frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=80)

Text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
Text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=Text1.yview)
Text1.configure(yscrollcommand=scrollbar1.set)

# third frame
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="Arial 14 bold", command=show_image).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="Arial 14 bold", command=save_image).place(x=180, y=30)
Label(frame3, text="picture, image, photo file", bg="#2f4155", fg="yellow").place(x=20, y=5)

# fourth frame
frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", width=10, height=2, font="Arial 14 bold", command=hide_data).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="Arial 14 bold", command=show_data).place(x=180, y=30)
Label(frame4, text="picture, image, photo file", bg="#2f4155", fg="yellow").place(x=20, y=5)

root.mainloop()
