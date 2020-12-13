from tkinter import *
import sqlite3
import tabulate
import random
from datetime import time
import time
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

base = Tk()
base.geometry("1500x750")
#base.config(background="#ffa500")
base.config(background="#36648B")
base.title("Criminal Finder Application")

#------------------------------- Events Starts -------------------------------------------
def event1():
    temp = Frame(rightFrame, width=1055, height=710)
    temp.grid(row=0, column=1, padx=0, pady=0)
    temp.config(background="#283A90")

    def event1_back():
        temp.destroy()
        rightFrame = Frame(base, width=0, height=0)
        rightFrame.grid(row=0, column=1, padx=0, pady=90)

    h1 = Label(temp, text="ADD NEW CRIMINAL", height="2", width="30", font=20)
    h1.place(x=360, y=30)

    criminal_id = Label(temp, text="ENTER CRIMINAL ID", fg="white", background="#283A90", font="20")
    criminal_id.place(x=200, y=100)
    txt1 = Entry(temp, width="57")
    txt1.place(x=570, y=100)

    criminal_name = Label(temp, text="ENTER CRIMINAL NAME", fg="white", background="#283A90", font="20")
    criminal_name.place(x=200, y=140)
    txt2 = Entry(temp, width="57")
    txt2.place(x=570, y=140)

    criminal_mob = Label(temp, text="ENTER CRIMINAL MOBILE NUMBER", fg="white", background="#283A90", font="20")
    criminal_mob.place(x=200, y=180)
    txt3 = Entry(temp, width="57")
    txt3.place(x=570, y=180)

    criminal_dob = Label(temp, text="ENTER CRIMINAL D.O.B.", fg="white", background="#283A90", font="20")
    criminal_dob.place(x=200, y=220)
    txt4 = DateEntry(temp, font=('Times New Roman', 12, 'bold'), width=20)
    #txt4 = Entry(temp, width="40")
    txt4.place(x=570, y=220)

    criminal_gender = Label(temp, text="ENTER CRIMINAL GENDER.", fg="white", background="#283A90", font="20")
    criminal_gender.place(x=200, y=260)
    var = IntVar()
    Radiobutton(temp, text="Male", padx=5, variable=var, value=1).place(x=570, y=260)
    Radiobutton(temp, text="Female", padx=20, variable=var, value=2).place(x=670, y=260)
    Radiobutton(temp, text="Other", padx=20, variable=var, value=3).place(x=820, y=260)

    criminal_addr = Label(temp, text="ENTER CRIMINAL ADDRESS", fg="white", background="#283A90", font="20")
    criminal_addr.place(x=200, y=300)
    txt5 = Entry(temp, width="57")
    txt5.place(x=570, y=307)

    criminal_image = Label(temp, text="UPLOAD CRIMINAL IMAGE", fg="white", background="#283A90", font="20")
    criminal_image.place(x=200, y=340)
    upload = Button(temp, width="25", height="1", bd="2", activebackground="green", text="UPLOAD AN IMAGE")
    upload.place(x=570, y=344)

    crime_type = Label(temp, text="ENTER CRIME TYPE", fg="white", background="#283A90", font="20")
    crime_type.place(x=200, y=380)
    txt6 = Entry(temp, width="57")
    txt6.place(x=570, y=380)

    crime_city = Label(temp, text="ENTER CRIME CITY", fg="white", background="#283A90", font="20")
    crime_city.place(x=200, y=420)
    txt7 = Entry(temp, width="57")
    txt7.place(x=570, y=420)

    crime_date = Label(temp, text="ENTER CRIME DATE", fg="white", background="#283A90", font="20")
    crime_date.place(x=200, y=460)
    txt8 = DateEntry(temp, font=('Times New Roman', 12, 'bold'), width=20)
    txt8.place(x=570, y=460)

    crime_time = Label(temp, text="ENTER CRIME TIME", fg="white", background="#283A90", font="20")
    crime_time.place(x=200, y=500)
    txt9 = Entry(temp, width="57")
    txt9.place(x=570, y=500)

    jail_name = Label(temp, text="ENTER JAIL NAME", fg="white", background="#283A90", font="20")
    jail_name.place(x=200, y=540)
    txt10 = Entry(temp, width="57")
    txt10.place(x=570, y=540)

    jail_addr = Label(temp, text="ENTER JAIL ADDRESS", fg="white", background="#283A90", font="20")
    jail_addr.place(x=200, y=580)
    txt11 = Entry(temp, width="57")
    txt11.place(x=570, y=580)

    btn1 = Button(temp, width="13", height="1", bd="5", activebackground="green", text="SAVE")
    btn1.place(x=300, y=615)

    # ---------------------
    def event1_reset():
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt5.delete(0, END)
        txt6.delete(0, END)
        txt7.delete(0, END)
        txt8.delete(0, END)
        txt9.delete(0, END)
        txt10.delete(0, END)
        txt11.delete(0, END)
        txt1.focus()
    # ----------------------

    btn2 = Button(temp, width="13", height="1", bd="5", activebackground="yellow", text="Reset", command=event1_reset)
    btn2.place(x=500, y=615)

    btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event1_back)
    btn3.place(x=700, y=615)

def event2():
    temp = Frame(rightFrame, width=1055, height=710)
    temp.grid(row=0, column=1, padx=0, pady=0)
    temp.config(background="#283A90")

    def event2_back():
        temp.destroy()
        rightFrame = Frame(base, width=0, height=0)
        rightFrame.grid(row=0, column=1, padx=0, pady=90)

    h1 = Label(temp, text="UPDATE CRIMINAL INFO", height="2", width="30", font=20)
    h1.place(x=360, y=30)

    retrieve = Button(temp, width="13", height="1", bd="5", activebackground="green", text="Retrieve")
    retrieve.place(x=800, y=50)

    criminal_id = Label(temp, text="ENTER CRIMINAL ID", fg="white", background="#283A90", font="20")
    criminal_id.place(x=200, y=100)
    txt1 = Entry(temp, width="57")
    txt1.place(x=570, y=100)

    criminal_name = Label(temp, text="ENTER CRIMINAL NAME", fg="white", background="#283A90", font="20")
    criminal_name.place(x=200, y=140)
    txt2 = Entry(temp, width="57")
    txt2.place(x=570, y=140)

    criminal_mob = Label(temp, text="ENTER CRIMINAL MOBILE NUMBER", fg="white", background="#283A90", font="20")
    criminal_mob.place(x=200, y=180)
    txt3 = Entry(temp, width="57")
    txt3.place(x=570, y=180)

    criminal_dob = Label(temp, text="ENTER CRIMINAL D.O.B.", fg="white", background="#283A90", font="20")
    criminal_dob.place(x=200, y=220)
    txt4 = DateEntry(temp, font=('Times New Roman', 12, 'bold'), width=20)
    # txt4 = Entry(temp, width="40")
    txt4.place(x=570, y=220)

    criminal_gender = Label(temp, text="ENTER CRIMINAL GENDER.", fg="white", background="#283A90", font="20")
    criminal_gender.place(x=200, y=260)
    var = IntVar()
    Radiobutton(temp, text="Male", padx=5, variable=var, value=1).place(x=570, y=260)
    Radiobutton(temp, text="Female", padx=20, variable=var, value=2).place(x=670, y=260)
    Radiobutton(temp, text="Other", padx=20, variable=var, value=3).place(x=820, y=260)

    criminal_addr = Label(temp, text="ENTER CRIMINAL ADDRESS", fg="white", background="#283A90", font="20")
    criminal_addr.place(x=200, y=300)
    txt5 = Entry(temp, width="57")
    txt5.place(x=570, y=307)

    criminal_image = Label(temp, text="UPLOAD CRIMINAL IMAGE", fg="white", background="#283A90", font="20")
    criminal_image.place(x=200, y=340)
    upload = Button(temp, width="25", height="1", bd="2", activebackground="green", text="UPLOAD AN IMAGE")
    upload.place(x=570, y=344)

    crime_type = Label(temp, text="ENTER CRIME TYPE", fg="white", background="#283A90", font="20")
    crime_type.place(x=200, y=380)
    txt6 = Entry(temp, width="57")
    txt6.place(x=570, y=380)

    crime_city = Label(temp, text="ENTER CRIME CITY", fg="white", background="#283A90", font="20")
    crime_city.place(x=200, y=420)
    txt7 = Entry(temp, width="57")
    txt7.place(x=570, y=420)

    crime_date = Label(temp, text="ENTER CRIME DATE", fg="white", background="#283A90", font="20")
    crime_date.place(x=200, y=460)
    txt8 = DateEntry(temp, font=('Times New Roman', 12, 'bold'), width=20)
    txt8.place(x=570, y=460)

    crime_time = Label(temp, text="ENTER CRIME TIME", fg="white", background="#283A90", font="20")
    crime_time.place(x=200, y=500)
    txt9 = Entry(temp, width="57")
    txt9.place(x=570, y=500)

    jail_name = Label(temp, text="ENTER JAIL NAME", fg="white", background="#283A90", font="20")
    jail_name.place(x=200, y=540)
    txt10 = Entry(temp, width="57")
    txt10.place(x=570, y=540)

    jail_addr = Label(temp, text="ENTER JAIL ADDRESS", fg="white", background="#283A90", font="20")
    jail_addr.place(x=200, y=580)
    txt11 = Entry(temp, width="57")
    txt11.place(x=570, y=580)

    btn1 = Button(temp, width="13", height="1", bd="5", activebackground="green", text="SAVE")
    btn1.place(x=300, y=615)

    # ---------------------
    def event2_reset():
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt5.delete(0, END)
        txt6.delete(0, END)
        txt7.delete(0, END)
        txt8.delete(0, END)
        txt9.delete(0, END)
        txt10.delete(0, END)
        txt11.delete(0, END)
        txt1.focus()
    # ----------------------

    btn2 = Button(temp, width="13", height="1", bd="5", activebackground="yellow", text="Reset", command=event2_reset)
    btn2.place(x=500, y=615)

    btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event2_back)
    btn3.place(x=700, y=615)

def event3():
    temp = Frame(rightFrame, width=1055, height=710)
    temp.grid(row=0, column=1, padx=0, pady=0)
    temp.config(background="#283A90")

    def event3_back():
        temp.destroy()
        rightFrame = Frame(base, width=0, height=0)
        rightFrame.grid(row=0, column=1, padx=0, pady=90)

    h1 = Label(temp, text="REMOVE CRIMINAL", height="2", width="30", font=20)
    h1.place(x=360, y=30)

    r_criminal_id = Label(temp, text="ENTER CRIMINAL ID", fg="white", background="#283A90", font="20")
    r_criminal_id.place(x=200, y=150)
    txt1 = Entry(temp, width="57")
    txt1.place(x=570, y=150)

    btn1 = Button(temp, width="13", height="1", bd="5", activebackground="green", text="Remove")
    btn1.place(x=300, y=250)

    #---------------------
    def event3_reset():
        txt1.delete(0, END)
        txt1.focus()
    #----------------------

    btn2 = Button(temp, width="13", height="1", bd="5", activebackground="yellow", text="Reset",command=event3_reset)
    btn2.place(x=500, y=250)

    btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event3_back)
    btn3.place(x=700, y=250)

def event4():
    temp = Frame(rightFrame, width=1055, height=710)
    temp.grid(row=0, column=1, padx=0, pady=0)
    temp.config(background="#283A90")

    def event4_back():
        temp.destroy()
        rightFrame = Frame(base, width=0, height=0)
        rightFrame.grid(row=0, column=1, padx=0, pady=90)

    def s1():
        temp = Frame(rightFrame, width=1055, height=710)
        temp.grid(row=0, column=1, padx=0, pady=0)
        temp.config(background="#283A90")

        h1 = Label(temp, text="SEARCH BY CRIMINAL ID", height="2", width="30", font=20)
        h1.place(x=360, y=30)

        def event41_back():
            temp.destroy()
            rightFrame = Frame(base, width=0, height=0)
            rightFrame.grid(row=0, column=1, padx=0, pady=90)

        s_criminal_id = Label(temp, text="ENTER CRIMINAL ID", fg="white", background="#283A90", font="20")
        s_criminal_id.place(x=200, y=150)
        txt1 = Entry(temp, width="57")
        txt1.place(x=570, y=150)

        btn1 = Button(temp, width="13", height="1", bd="5", activebackground="green", text="Search")
        btn1.place(x=300, y=250)

        # ---------------------
        def event41_reset():
            txt1.delete(0, END)
            txt1.focus()
        # ----------------------

        btn2 = Button(temp, width="13", height="1", bd="5", activebackground="yellow", text="Reset",command=event41_reset)
        btn2.place(x=500, y=250)

        btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event41_back)
        btn3.place(x=700, y=250)

    def s2():
        temp = Frame(rightFrame, width=1055, height=710)
        temp.grid(row=0, column=1, padx=0, pady=0)
        temp.config(background="#283A90")

        h1 = Label(temp, text="SEARCH BY CRIMINAL NAME", height="2", width="30", font=20)
        h1.place(x=360, y=30)

        def event42_back():
            temp.destroy()
            rightFrame = Frame(base, width=0, height=0)
            rightFrame.grid(row=0, column=1, padx=0, pady=90)

        s_criminal_name = Label(temp, text="ENTER CRIMINAL NAME", fg="white", background="#283A90", font="20")
        s_criminal_name.place(x=200, y=150)
        txt2 = Entry(temp, width="57")
        txt2.place(x=570, y=150)

        btn1 = Button(temp, width="13", height="1", bd="5", activebackground="green", text="Search")
        btn1.place(x=300, y=250)

        # ---------------------
        def event42_reset():
            txt2.delete(0, END)
            txt2.focus()
        # ----------------------

        btn2 = Button(temp, width="13", height="1", bd="5", activebackground="yellow", text="Reset",command=event42_reset)
        btn2.place(x=500, y=250)

        btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event42_back)
        btn3.place(x=700, y=250)

    def s3():
        temp = Frame(rightFrame, width=1055, height=710)
        temp.grid(row=0, column=1, padx=0, pady=0)
        temp.config(background="#283A90")

        h1 = Label(temp, text="SEARCH BY CRIMINAL MOBILE NUMBER", height="2", width="40", font=20)
        h1.place(x=330, y=30)

        def event43_back():
            temp.destroy()
            rightFrame = Frame(base, width=0, height=0)
            rightFrame.grid(row=0, column=1, padx=0, pady=90)

        s_criminal_mob = Label(temp, text="ENTER CRIMINAL MOBILE NUMBER", fg="white", background="#283A90", font="20")
        s_criminal_mob.place(x=200, y=150)
        txt3 = Entry(temp, width="57")
        txt3.place(x=570, y=150)

        btn1 = Button(temp, width="13", height="1", bd="5", activebackground="green", text="Search")
        btn1.place(x=300, y=250)

        # ---------------------
        def event43_reset():
            txt3.delete(0, END)
            txt3.focus()
        # ----------------------

        btn2 = Button(temp, width="13", height="1", bd="5", activebackground="yellow", text="Reset",command=event43_reset)
        btn2.place(x=500, y=250)

        btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event43_back)
        btn3.place(x=700, y=250)

    h1 = Label(temp, text="SEARCH CRIMINAL", height="2", width="30", font=20)
    h1.place(x=360, y=30)

    btn1 = Button(temp, width="35", height="2", bd="5", activebackground="green", text="SEARCH BY CRIMINAL ID", command=s1)
    btn1.place(x=400, y=150)

    btn2 = Button(temp, width="35", height="2", bd="5", activebackground="red", text="SEARCH BY CRIMINAL NAME", command=s2)
    btn2.place(x=400, y=300)

    btn3 = Button(temp, width="35", height="2", bd="5", activebackground="red", text="SEARCH BY CRIMINAL MOBILE NUMBER", command=s3)
    btn3.place(x=400, y=450)

    btn4 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event4_back)
    btn4.place(x=480, y=600)

def event5():
    temp = Frame(rightFrame, width=1055, height=710)
    temp.grid(row=0, column=1, padx=0, pady=0)
    temp.config(background="#283A90")

    h1 = Label(temp, text="CRIME STATASTICS", height="2", width="30", font=20)
    h1.place(x=360, y=30)

    def event5_back():
        temp.destroy()
        rightFrame = Frame(base, width=0, height=0)
        rightFrame.grid(row=0, column=1, padx=0, pady=90)

    btn1 = Button(temp, width="35", height="2", bd="5", activebackground="green", text="STATEWISE STATASTICS")
    btn1.place(x=400, y=200)

    btn2 = Button(temp, width="35", height="2", bd="5", activebackground="blue",text="DISTRICTWISE STATASTICS")
    btn2.place(x=400, y=350)

    btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event5_back)
    btn3.place(x=480, y=500)

def event6():
    temp = Frame(rightFrame, width=1055, height=710)
    temp.grid(row=0, column=1, padx=0, pady=0)
    temp.config(background="#283A90")

    h1 = Label(temp, text="DOWNLOAD RECORD PDF", height="2", width="30", font=20)
    h1.place(x=360, y=30)

    def event6_back():
        temp.destroy()
        rightFrame = Frame(base, width=0, height=0)
        rightFrame.grid(row=0, column=1, padx=0, pady=90)

    btn1 = Button(temp, width="35", height="2", bd="5", activebackground="green", text="STATEWISE PDF")
    btn1.place(x=400, y=200)

    btn2 = Button(temp, width="35", height="2", bd="5", activebackground="blue",text="DISTRICTWISE PDF")
    btn2.place(x=400, y=350)

    btn3 = Button(temp, width="13", height="1", bd="5", activebackground="blue", text="Back", command=event6_back)
    btn3.place(x=480, y=500)

def event7():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if (res == True):
        base.destroy()
#------------------------------- Events Ends -------------------------------------------

#---------------------------- Clock Starts ----------------------------------
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(1000,tick)

clock = Label(base,font=('Times new roman',14,'bold'),relief=RIDGE,borderwidth=4,bg='linen')
clock.place(x=0,y=0)
tick()
#---------------------------- Clock Ends ----------------------------------

#-------------------------------------- Slidebar Starts -----------------------------------------------------
colors = ['red','green','black','red2','gold2','indianred1','sienna1','orange2','darkorchid1','cornflower blue','saddle brown','cornsilk3','steelblue4']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(1000,IntroLabelColorTick)

def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(300,IntroLabelTick)

ss = 'Criminal Finder Application'
count = 0
text = ''

SliderLabel = Label(base,text=ss,font=('Times new roman',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='linen')
SliderLabel.place(x=350,y=0)
IntroLabelTick()
IntroLabelColorTick()
#-------------------------------------- Slidebar Ends -----------------------------------------------------

#--------------------------- leftFrame Starts -------------------------------
leftFrame = Frame(base, width=500, height = 710)
leftFrame.grid(row=0, column=0, padx=2, pady=90)
#leftFrame.config(background = "#FF6E33")
leftFrame.config(background = "#4E78A0")
#---------------------------------- leftFrame Ends -----------------------------------------

#------------------------------- RighttFrame Starts ----------------------------------------
rightFrame = Frame(base, width=1030, height = 710)
rightFrame.grid(row=0, column=1, padx=0, pady=90)
#rightFrame.config(background = "#FFE633")
#------------------------------- RighttFrame Ends ----------------------------------------

#----------------------- Leftframe Menus Starts --------------------------------------
b1 = Button(leftFrame, width="40", height="2", bd="5", activebackground="green", text="ADD NEW CRIMINAL", command=event1)
b1.place(x=100, y=50)

b2 = Button(leftFrame, width="40", height="2", bd="5", activebackground="green", text="UPDATE CRIMINAL INFO", command=event2)
b2.place(x=100, y=150)

b3 = Button(leftFrame, width="40", height="2", bd="5", activebackground="green", text="REMOVE CRIMINAL", command=event3)
b3.place(x=100, y=250)

b4 = Button(leftFrame, width="40", height="2", bd="5", activebackground="green", text="SEARCH CRIMINAL", command=event4)
b4.place(x=100, y=350)

b5 = Button(leftFrame, width="40", height="2", bd="5", activebackground="green", text="CRIME STATASTICS", command=event5)
b5.place(x=100, y=450)

b6 = Button(leftFrame, width="40", height="2", bd="5", activebackground="green", text="DOWNLOAD RECORD PDF", command=event6)
b6.place(x=100, y=550)

b7 = Button(leftFrame, width="40", height="2", bd="5", activebackground="red", text="EXIT", command=event7)
b7.place(x=100, y=650)
#----------------------- Leftframe Menus Ends --------------------------------------

#----------------------------- Add Image To RightFrame Starts -----------------------------------
image = Image.open("C:/Users/Lenovo/Desktop/crime3.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(rightFrame,image=photo, width=1050, height=700)
label.grid(row=0, column=1, padx=0, pady=0)
#----------------------------- Add Image To RightFrame Ends -------------------------------------

base.mainloop()