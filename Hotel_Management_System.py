from tkinter import *
from PIL import ImageTk, Image
import mysql.connector as mc
from tkinter import messagebox as mb
import random

con=mc.connect(host="localhost",user="root",passwd="password")
cur=con.cursor()

cur.execute("create database if not exists HMS")
cur.execute("use HMS")
cur.execute("create table if not exists ROOM_BOOKINGS(NAME varchar(30),PHONE_NUMBER char(10),CHECK_IN varchar(10),CHECK_OUT varchar(10))")
cur.execute("create table if not exists  GAMING_ZONE(NAME varchar(30),FIFA int,BOWLING int,CALL_OF_DUTY int,SMASH int,TOTAL float)")
cur.execute("create table if not exists  RESTAURANT(NAME varchar(30),PASTA int,PIZZA int,HOT_CHOCOLATE int,CAKE int,TOTAL float)")
cur.execute("create table if not exists  BILLS(ROOM_NUM int,NAME varchar(30),PHONE_NUM char(10),CHECK_IN varchar(10),CHECK_OUT varchar(10),G_BILL float,R_BILL float,TOTAL float)")

window=Tk()
window.geometry('400x660')
window.title('')
window['bg']='black'
sp2=Label(text='',height=1,bg='black').pack()
wlcm=Label(text='THE PARADISE INN',bg='black',fg='light blue',font=('Courier New Bold',20)).pack()


def bkroom():
    bk=Tk()
    bk.geometry('450x250')
    bk.title('Book A Room')
    bk['bg']='black'
    bk1=Label(bk,text='',height=1,bg='black').grid(row = 0,column = 0)
    bk2=Label(bk,text='',height=1,bg='black').grid(row = 1,column = 0)
    ttl=Label(bk,text='ROOM BOOKING',bg='black',fg='light blue',font=('Courier New Bold',13)).grid(row = 2,column = 2)
    a = Label(bk ,text = "Enter your name:",bg='black',fg='light blue').grid(row = 3,column = 1)
    b = Label(bk ,text = "Enter your phone number:",bg='black',fg='light blue').grid(row = 4,column = 1)
    c = Label(bk ,text = "Enter check-in date:",bg='black',fg='light blue').grid(row = 5,column = 1)
    d = Label(bk ,text = "Enter check-out date:",bg='black',fg='light blue').grid(row = 6,column = 1)
    a2=Label(bk,text='',height=1,bg='black').grid(row = 3,column = 2)
    b2=Label(bk,text='',height=1,bg='black').grid(row = 4,column = 2)
    c2=Label(bk,text='',height=1,bg='black').grid(row = 5,column = 2)
    d2=Label(bk,text='',height=1,bg='black').grid(row = 6,column = 2)
    a1 = Entry(bk,bg='grey')
    a1.grid(row = 3,column = 3)
    b1 = Entry(bk,bg='grey')
    b1.grid(row = 4,column = 3)
    c1 = Entry(bk,bg='grey')
    c1.grid(row = 5,column = 3)
    d1 = Entry(bk,bg='grey')
    d1.grid(row = 6,column = 3)
    
    def conf():
        global name
        global pn
        global checkin
        global checkout
        global roomno
        name=str(a1.get())
        pn=b1.get()
        checkin=c1.get()
        checkout=d1.get()
        cur.execute("insert into ROOM_BOOKINGS values('{}',{},'{}','{}')".format(name,pn,checkin,checkout))
        con.commit()
        bk.destroy()
        roomno=random.randint(100,10000)
        mb.showinfo("","ROOM BOOKED SUCCESSFULLY,YOUR ROOM NUMBER IS "+str(roomno))
    confirm=Button(bk,text='CONFIRM',fg='black',bg='light blue',height=1,command=conf).grid(row=7,column=2)


def game():
    g=Tk()
    g.geometry('400x250')
    g.title('Gaming Zone')
    g['bg']='black'
    g1=Label(g,text='',height=1,bg='black').grid(row = 0,column = 0)
    g2=Label(g,text='',height=1,bg='black').grid(row = 1,column = 0)
    tgl=Label(g,text='GAMING ZONE',bg='black',fg='light blue',font=('Courier New Bold',13),width=15).grid(row = 2,column = 2)
    ga = Label(g ,text = "1. FIFA         --> Rs.400 ",bg='black',fg='light blue',anchor='w',justify=LEFT,width=25).grid(row = 3,column = 1)
    gb = Label(g ,text = "2. BOWLING      --> Rs.800 ",bg='black',fg='light blue',anchor='w',justify=LEFT,width=25).grid(row = 4,column = 1)
    gc = Label(g ,text = "3. CALL OF DUTY --> Rs.400 ",bg='black',fg='light blue',anchor='w',justify=LEFT,width=25).grid(row = 5,column = 1)
    gd = Label(g ,text = "4. SMASH        --> Rs.500 ",bg='black',fg='light blue',anchor='w',justify=LEFT,width=25).grid(row = 6,column = 1)
    ga2=Label(g,text='',height=1,bg='black').grid(row = 3,column = 2)
    gb2=Label(g,text='',height=1,bg='black').grid(row = 4,column = 2)
    gc2=Label(g,text='',height=1,bg='black').grid(row = 5,column = 2)
    gd2=Label(g,text='',height=1,bg='black').grid(row = 6,column = 2)
    ga1 = Spinbox(g, from_=0, to=50,bg='light grey',width=3)
    ga1.grid(row = 3,column = 3)
    gb1 = Spinbox(g, from_=0, to=50,bg='light grey',width=3)
    gb1.grid(row = 4,column = 3)
    gc1 = Spinbox(g, from_=0, to=50,bg='light grey',width=3)
    gc1.grid(row = 5,column = 3)
    gd1 = Spinbox(g, from_=0, to=50,bg='light grey',width=3)
    gd1.grid(row = 6,column = 3)
    
    def conf():
        global gt
        gaq=ga1.get()
        gbq=gb1.get()
        gcq=gc1.get()
        gdq=gd1.get()
        gt=(int(gaq)*400)+(int(gbq)*800)+(int(gcq)*400)+(int(gdq)*500)
        cur.execute("insert into GAMING_ZONE values('{}',{},{},{},{},{})".format(name,gaq,gbq,gcq,gdq,gt))
        con.commit()
        g.destroy()
        mb.showinfo("","SEATS BOOKED SUCCESSFULLY")
    cfrm=Button(g,text='CONFIRM',fg='black',bg='light blue',height=1,command=conf).grid(row=7,column=2)

def food():
    f=Tk()
    f.geometry('400x250')
    f.title('Restaurant')
    f['bg']='black'
    f1=Label(f,text='',height=1,bg='black').grid(row = 0,column = 0)
    f2=Label(f,text='',height=1,bg='black').grid(row = 1,column = 0)
    tfl=Label(f,text='RESTAURANT',bg='black',fg='light blue',font=('Courier New Bold',13),width=15).grid(row = 2,column = 2)
    fa = Label(f ,text = "1. PASTA          --> Rs.500 ",bg='black',fg='light blue',anchor='w',justify=LEFT,width=25).grid(row = 3,column = 1)
    fb = Label(f ,text = "2. PIZZA          --> Rs.800 ",bg='black',fg='light blue',anchor='w',justify=LEFT,width=25).grid(row = 4,column = 1)
    fc = Label(f ,text = "3. HOT CHOCOLATE  --> Rs.200 ",bg='black',fg='light blue',anchor='w',justify=LEFT,width=25).grid(row = 5,column = 1)
    fd = Label(f ,text = "4. CAKE           --> Rs.500 ",bg='black',fg='light blue',anchor='w',justify=LEFT,width=25).grid(row = 6,column = 1)
    fa2=Label(f,text='',height=1,bg='black').grid(row = 3,column = 2)
    fb2=Label(f,text='',height=1,bg='black').grid(row = 4,column = 2)
    fc2=Label(f,text='',height=1,bg='black').grid(row = 5,column = 2)
    fd2=Label(f,text='',height=1,bg='black').grid(row = 6,column = 2)
    fa1 = Spinbox(f, from_=0, to=50,bg='light grey',width=3)
    fa1.grid(row = 3,column = 3)
    fb1 = Spinbox(f, from_=0, to=50,bg='light grey',width=3)
    fb1.grid(row = 4,column = 3)
    fc1 = Spinbox(f, from_=0, to=50,bg='light grey',width=3)
    fc1.grid(row = 5,column = 3)
    fd1 = Spinbox(f, from_=0, to=50,bg='light grey',width=3)
    fd1.grid(row = 6,column = 3)
    
    def conf():
        global ft
        faq=fa1.get()
        fbq=fb1.get()
        fcq=fc1.get()
        fdq=fd1.get()
        ft=(int(faq)*500)+(int(fbq)*800)+(int(fcq)*200)+(int(fdq)*500)
        cur.execute("insert into RESTAURANT values('{}',{},{},{},{},{})".format(name,faq,fbq,fcq,fdq,ft))
        cur.execute("insert into BILLS values({},'{}','{}','{}','{}',{},{},{})".format(roomno,name,pn,checkin,checkout,gt,ft,gt+ft))
        con.commit()
        f.destroy()
        mb.showinfo("","ORDER PLACED SUCCESSFULLY")
    cfrm=Button(f,text='PLACE ORDER',fg='black',bg='light blue',height=1,command=conf).grid(row=7,column=2)


def show():
    cur.execute("select * from BILLS")
    cf=cur.fetchall()
    cfh=("ROOM NUMBER","NAME","PHONE NUMBER","CHECK-IN","CHECK-OUT","GAME BILL","RESTAURANT BILL","TOTAL BILL")
    b_window=Tk()
    b_window.title("Bill & Bookings")
    for i in range(8):
        bh=Entry(b_window,width=16,justify=CENTER,bg="black",fg="crimson",font=('Courier New',13,'bold italic'))
        bh.grid(row=0,column=i)
        bh.insert(END,cfh[i])
    for ro in range(len(cf)):
        for col in range(8):
            b=Entry(b_window,width=20,justify=CENTER,bg="black",fg="cyan",font=('Cambria',11,'italic'))
            b.grid(row=ro+1,column=col)
            b.insert(END,cf[ro][col])

    
brm=Canvas(window, width = 342, height=150,bg='black',highlightthickness=0)  
brm.pack()
img = ImageTk.PhotoImage(Image.open("bedroom-clipart-hotel-room-2.jpg"))  
brm.create_image(20, 20, anchor=NW, image=img) 
Bkrm=Button(window,text='BOOK A ROOM',bg='light blue',fg='black',height=1,width=43,command=bkroom)
Bkrm.pack()

games=Canvas(window, width = 350, height=150,bg='black',highlightthickness=0)  
games.pack()
img2 = ImageTk.PhotoImage(Image.open("gaming-zone.png"))  
games.create_image(20, 20, anchor=NW, image=img2) 
gm=Button(window,text='GAMING ZONE',bg='light blue',fg='black',height=1,width=43,command=game)
gm.pack()

rs=Canvas(window, width = 350, height=150,bg='black',highlightthickness=0)  
rs.pack()
img3 = ImageTk.PhotoImage(Image.open("res.jpg"))  
rs.create_image(20, 20, anchor=NW, image=img3) 
rsb=Button(window,text='RESTAURANT',bg='light blue',fg='black',height=1,width=43,command=food)
rsb.pack()

sp1=Label(text='',height=1,bg='black').pack()
billb=Button(window,text='SHOW BILLS AND BOOKING',bg='light blue',fg='black',height=2,width=43,command=show)
billb.pack()
