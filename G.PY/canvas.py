import re
from tkinter import *
from tkinter import ttk,font,messagebox
from PIL import ImageTk,ImageTk,Image
import pymysql as mysql   



def studentregistration(win):
    win.destroy()
    win=Tk()
    win.geometry('500x500')
    f1=Frame(win,width=1500,height=50,bg="orchid3")
    f1.pack()


    img=ImageTk.PhotoImage(Image.open("train.jpeg"))
    canvas=Canvas(img)
    canvas.create_image(690,390,image=img)
    canvas.pack(fill="both",expand=True)
    label_font=font.Font(weight="bold",family="Helvetica",size=17)
    canvas.create_text(815,30,text="Name",fill="Black",font=label_font)