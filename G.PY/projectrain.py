import tkinter
from tkinter import*
from tkinter import ttk, font, messagebox
from PIL import  Image
from PIL.ImageTk import PhotoImage





def customerregister(r):
      r.destroy()
      r=Tk()
      r.geometry("1000x1000")
      r.attributes('-fullscreen', True)
      r.configure(bg="gray44")
      f=Frame(r,width=1500,height=50,bg="black").pack()
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="METRO BOOKING",font=lf,bg="black",fg="white")
      x.place(relx=0.4,rely=0.01)

    #   f=Frame(r,width=500,height=540,bg="khaki1").place(relx=0.4,rely=0.150)
      x=Label(f,text="CustomerRegistration",font=lf,bg="gray44").place(relx=0.388,rely=0.220)
      lf=font.Font(weight="bold",family="Times New Roman",size=17)
      x=Label(r,text="Name",font=lf,bg="gray44").place(relx=0.366,rely=0.330)
      x=Label(r,text="Pho no",font=lf,bg="gray44").place(relx=0.366,rely=0.4)
      x=Label(r,text="Aadhar no",font=lf,bg="gray44").place(relx=0.366,rely=0.470)
      x=Label(r,text="Email id",font=lf,bg="gray44").place(relx=0.366,rely=0.550)
      x=Label(r,text="Pancard no",font=lf,bg="gray44").place(relx=0.366,rely=0.620)
      x=Label(r,text="Address",font=lf,bg="gray44").place(relx=0.366,rely=0.690)
      a1=Entry(r)
      a1.place(relx=0.5,rely=0.330,width=180, height=25)
      b1=Entry(r)
      b1.place(relx=0.5,rely=0.4,width=180, height=25)
      c1=Entry(r)
      c1.place(relx=0.5,rely=0.470,width=180, height=25)
      d1=Entry(r)
      d1.place(relx=0.5,rely=0.540,width=180, height=25)
      e1=Entry(r)
      e1.place(relx=0.5,rely=0.620,width=180, height=25)
      f1=Entry(r)
      f1.place(relx=0.5,rely=0.690,width=180, height=40)


      f=Frame(r,width=1500,height=51,bg="black").place(relx=0,rely=0.940)
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="@EXPRESS 3/28",font=lf,bg="black",fg="white").place(relx=0.4,rely=0.94)


def adminlogin(r):
       



      r.destroy()
      r=Tk()
      r.geometry("1000x1000")
      r.attributes('-fullscreen', True)
      r.configure(bg="gray44")
      f=Frame(r,width=1500,height=50,bg="black").pack()
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="METRO BOOKING",font=lf,bg="black",fg="white")
      x.place(relx=0.4,rely=0.01)

    
      x=Label(f,text="AdminLogin",font=lf,bg="gray44").place(relx=0.388,rely=0.220)
      lf=font.Font(weight="bold",family="Times New Roman",size=17)
      x=Label(r,text="User Name",font=lf,bg="gray44").place(relx=0.366,rely=0.330)
      x=Label(r,text="Password",font=lf,bg="gray44").place(relx=0.366,rely=0.4)
     
      a1=Entry(r)
      a1.place(relx=0.5,rely=0.330,width=180, height=25)
      b1=Entry(r)
      b1.place(relx=0.5,rely=0.4,width=180, height=25)
      c1=Entry(r)
      

      f=Frame(r,width=1500,height=51,bg="black").place(relx=0,rely=0.940)
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="@EXPRESS 3/28",font=lf,bg="black",fg="white").place(relx=0.4,rely=0.94)

def Available(r):
      r.destroy()
      r=Tk()
      r.geometry("1000x1000")
      r.attributes('-fullscreen', True)
      r.configure(bg="gray44")
      f=Frame(r,width=1500,height=50,bg="black").pack()
      lf=font.Font(weight="bold",family="Times New Roman",size=25)
      x=Label(f,text="METRO BOOKING",font=lf,bg="black",fg="white")
      x.place(relx=0.4,rely=0.01)
      
      
      x=Label(f,text="Available",font=lf,bg="gray44").place(relx=0.388,rely=0.220)
      lf=font.Font(weight="bold",family="Times New Roman",size=17)
      x=Label(r,text="Train No: 15705  Train Name:  Champaran Humsafar Express",font=lf,bg="gray44").place(relx=0.366,rely=0.330)
      x=Label(r,text="Train No: 12038  Train Name:  Shatabdi Express",font=lf,bg="gray44").place(relx=0.366,rely=0.4)
      x=Label(r,text="Train No: 19339  Train Name:  Dahod Bhopal Intercity Express",font=lf,bg="gray44").place(relx=0.366,rely=0.470)
      x=Label(r,text="Train No: 14722  Train Name:  Abohar Jodhpur Express ",font=lf,bg="gray44").place(relx=0.366,rely=0.550)
      x=Label(r,text="Train No: 09757  Train Name:  Badgam Baramulla DEMU Express Special",font=lf,bg="gray44").place(relx=0.366,rely=0.620)
    
      b

     
      # a1=Entry(r)
      # a1.place(relx=0.5,rely=0.330,width=180, height=25)
      # b1=Entry(r)
      # b1.place(relx=0.5,rely=0.4,width=180, height=25)
      # c1=Entry(r)
      # c1.place(relx=0.5,rely=0.470,width=180, height=25)
      # d1=Entry(r)
      # d1.place(relx=0.5,rely=0.540,width=180, height=25)
      # e1=Entry(r)
      # e1.place(relx=0.5,rely=0.620,width=180, height=25)
      # f1=Entry(r)
      # f1.place(relx=0.5,rely=0.690,width=180, height=40)
      

      f=Frame(r,width=1500,height=51,bg="black").place(relx=0,rely=0.940)
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="@EXPRESS 3/28",font=lf,bg="black",fg="white").place(relx=0.4,rely=0.94)


    
      






def Bookingdetails(r):
       



      r.destroy()
      r=Tk()
      r.geometry("1000x1000")
      r.attributes('-fullscreen', True)
      r.configure(bg="gray44")
      f=Frame(r,width=1500,height=50,bg="black").pack()
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="METRO BOOKING",font=lf,bg="black",fg="white")
      x.place(relx=0.4,rely=0.01)

    
      x=Label(f,text="Booking Details",font=lf,bg="gray44").place(relx=0.388,rely=0.220)
      lf=font.Font(weight="bold",family="Times New Roman",size=17)
      x=Label(r,text="From",font=lf,bg="gray44").place(relx=0.366,rely=0.330)
      x=Label(r,text="To",font=lf,bg="gray44").place(relx=0.366,rely=0.4)
      x=Label(r,text="General",font=lf,bg="gray44").place(relx=0.366,rely=0.470)
      x=Label(r,text="DD/MM/YY",font=lf,bg="gray44").place(relx=0.366,rely=0.550)
      x=Label(r,text="All Cases",font=lf,bg="gray44").place(relx=0.366,rely=0.620)
      
     
      a1=Entry(r)
      a1.place(relx=0.5,rely=0.330,width=180, height=25)
      b1=Entry(r)
      b1.place(relx=0.5,rely=0.4,width=180, height=25)
      c1=Entry(r)
      c1.place(relx=0.5,rely=0.470,width=180, height=25)
      d1=Entry(r)
      d1.place(relx=0.5,rely=0.540,width=180, height=25)
      e1=Entry(r)
      e1.place(relx=0.5,rely=0.620,width=180, height=25)
      

      

      f=Frame(r,width=1500,height=51,bg="black").place(relx=0,rely=0.940)
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="@EXPRESS 3/28",font=lf,bg="black",fg="white").place(relx=0.4,rely=0.94)






def Next(r):
        r.destroy()
        r=Tk()
        r.geometry("1000x1000")
        r.attributes('-fullscreen', True)
        r.configure(bg="gray44")
        f=Frame(r,width=1500,height=50,bg="black").pack()
        lf=font.Font(weight="bold",family="Times New Roman",size=25 )
        x1=Label(f,text="METRO BOOKING",font=lf,bg="black",fg="white")
        x1.place(relx=0.4,rely=0.01)
        



        





        b=Button(r,text="Customer Register",font=lf,width=15,height=1,bg="black",fg="white",command=lambda:customerregister(r)).place(relx=0.150,rely=0.3)
        b=Button(r,text="Admin Login",font=lf,bg="black",fg="white",command=lambda:adminlogin(r)).place(relx=0.433,rely=0.3)
        b=Button(r,text="Available",font=lf,bg="black",fg="white",command=lambda:Available(r)).place(relx=0.655,rely=0.3)
        b=Button(r,text="Booking Details",font=lf,bg="black",fg="white",command=lambda:Bookingdetails(r)).place(relx=0.244,rely=0.6)
        b=Button(r,text="Cancel",font=lf,width=10,height=1,bg="black",fg="white").place(relx=0.544,rely=0.6)



        f=Frame(r,width=1500,height=51,bg="black").place(relx=0,rely=0.940)
        lf=font.Font(weight="bold",family="Times New Roman",size=25 )
        x=Label(f,text="@EXPRESS 3/28",font=lf,bg="black",fg="white").place(relx=0.4,rely=0.94)
      



    

  

#home
r=Tk()
r.title("Train")
r.attributes('-fullscreen', True)
r.configure(bg="gray1")
f=Frame(r,width=1500,height=51,bg="black").pack()
lf=font.Font(weight="bold",family="Times New Roman",size=25 )
x=Label(f,text="EMPIRE BUILDER EXPRESS",font=lf,bg="black",fg="white").place(relx=0.33,rely=0.0)

f=Frame(r,width=100,height=10).pack()
img=PhotoImage(Image.open("train.jpeg"))
x=Label(f,image=img).place(relx=0,rely=0.1)


lf=font.Font(weight="bold",family="Times New Roman",size=20 )
b=Button (r,text="Next",font=lf,bg="white",fg="black",command=lambda:Next(r)).place(relx=0.9,rely=0.8)






r.mainloop()

