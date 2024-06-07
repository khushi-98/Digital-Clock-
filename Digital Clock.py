from tkinter import *
from PIL import Image, ImageTk
import datetime

def date_time():
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    mi=time.strftime('%M')
    sec=time.strftime('%S')
    am =time.strftime("%p")
    date=time.strftime("%d")
    month=time.strftime("%m")
    year=time.strftime("%y")
    day=time.strftime("%a")

    l1.config(text=hr)
    l2.config(text=mi)
    l3.config(text=sec)
    l4.config(text=am)
    d1.config(text=date)
    d2.config(text=month)
    d3.config(text=year)
    d4.config(text=day)

    l1.after(200,date_time)




clock = Tk()
clock.title('Digital Clock')
clock.geometry("1000x500")

image = Image.open("C:/Users/bansa/Downloads/pic1.jpg")
image = image.resize((1000, 500))  
tk_image = ImageTk.PhotoImage(image)

label1 = Label(clock, image=tk_image)
label1.place(x=0, y=0, relwidth=1, relheight=1)

l1=Label(clock,text="00",font=('Times New Roman',50,"bold"),
bg='silver',fg='black')
l1.place(x=120,y=40,height=110,width=100)

l2=Label(clock,text="00",font=('Times New Roman',50,"bold"),
bg='silver',fg='black')
l2.place(x=340,y=40,height=110,width=100)

l3=Label(clock,text="00",font=('Times New Roman',50,"bold"),
bg='silver',fg='black')
l3.place(x=560,y=40,height=110,width=100)

l4=Label(clock,text="00",font=('Times New Roman',45,"bold"),
bg='silver',fg='black')
l4.place(x=780,y=40,height=110,width=100)

ll1=Label(clock,text="Hour",font=('Times New Roman',25,"bold"),
bg='silver',fg='black')
ll1.place(x=120,y=190,height=30,width=100)

ll2=Label(clock,text="Min",font=('Times New Roman',25,"bold"),
bg='silver',fg='black')
ll2.place(x=340,y=190,height=30,width=100)

ll3=Label(clock,text="Sec",font=('Times New Roman',25,"bold"),
bg='silver',fg='black')
ll3.place(x=560,y=190,height=30,width=100)

ll4=Label(clock,text="AM/PM",font=('Times New Roman',20,"bold"),
bg='silver',fg='black')
ll4.place(x=780,y=190,height=30,width=100)

# date_time()


d1=Label(clock,text="00",font=('Times New Roman',50,"bold"),
bg='silver',fg='black')
d1.place(x=120,y=270,height=110,width=100)

dd1=Label(clock,text="Date",font=('Times New Roman',25,"bold"),
bg='silver',fg='black')
dd1.place(x=120,y=410,height=30,width=100)

d2=Label(clock,text="00",font=('Times New Roman',50,"bold"),
bg='silver',fg='black')
d2.place(x=340,y=270,height=110,width=100)
dd2=Label(clock,text="Month",font=('Times New Roman',25,"bold"),
bg='silver',fg='black')
dd2.place(x=340,y=410,height=30,width=100)

d3=Label(clock,text="00",font=('Times New Roman',50,"bold"),
bg='silver',fg='black')
d3.place(x=560,y=270,height=110,width=100)
dd3=Label(clock,text="Year",font=('Times New Roman',25,"bold"),
bg='silver',fg='black')
dd3.place(x=560,y=410,height=30,width=100)

d4=Label(clock,text="00",font=('Times New Roman',45,"bold"),
bg='silver',fg='black')
d4.place(x=780,y=270,height=110,width=100)
dd4=Label(clock,text="Day",font=('Times New Roman',20,"bold"),
bg='silver',fg='black')
dd4.place(x=780,y=410,height=30,width=100)


date_time()
clock.mainloop()

