
from Tkinter import *
root=Tk()
import sys
frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
frame4=Frame(root)
frame5=Frame(root)
frame1.pack(side=TOP)
frame2.pack(side=TOP)
frame3.pack(side=BOTTOM)
frame4.pack(side=BOTTOM)
frame5.pack(side=BOTTOM)
ment=StringVar()
def get_data():
    mtext=ment.get()
    lbl2=Label(frame5,text="entered values are-"+mtext).pack(side=TOP)
     
#proper format- homebut1=Button(frame1,text="go home shelf 1-linearly",command=home1 ,bg="green",fg="blue")
root.title("AUTOMATIC GARDEN IRRIGATION SYSTEM")
lbl = Label(frame1, text="1.0.1 AUTOMATIC GARDEN IRRIGATION SYSTEM",font=("Times New Roman", 18))
homebut1=Button(frame2,text="START",command=get_data,bg="green",fg="blue",width=20,height=2)
homebut2=Button(frame2,text="STOP",command=get_data,bg="green",fg="blue",width=20,height=2)
mentry=Entry(frame1,textvariable=ment)
lbl2 = Label(frame1, text="Enter coordinates-")
helplf = LabelFrame(frame1, text=" Quick Help ")
helplf.pack()
lbl.pack(side=TOP)
lbl2.pack(side=TOP)
mentry.pack()
homebut1.pack(side=LEFT,fill=BOTH)
homebut2.pack(side=RIGHT,fill=BOTH)
           
root.mainloop()

