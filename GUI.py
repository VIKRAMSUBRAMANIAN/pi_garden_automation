from Tkinter import *

import sys

#first screen
gate=0
def use_coor():#using coordinates, contains code that opens new window

    root=Tk()
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
        lbl2=Label(frame5,text="entered coordinates are-"+mtext).pack(side=TOP)

    def exit_gui():
        root.destroy()
    
        sys.exit()








    #proper format- homebut1=Button(frame1,text="go home shelf 1-linearly",command=home1 ,bg="green",fg="blue")
    root.title("AUTOMATIC IRRIGATION SYSTEM-USING COORDINATES")
    lbl = Label(frame1, text="AUTOMATIC IRRIGATION SYSTEM- COORDINATES",font=("Times New Roman", 18))

    homebut1=Button(frame2,text="START",command=get_data,bg="green",fg="blue",width=20,height=2)

    homebut2=Button(frame2,text="STOP",command=exit_gui,bg="red",fg="blue",width=20,height=2)


    mentry=Entry(frame1,textvariable=ment)
    lbl2 = Label(frame1, text="Enter the coordinates: ")


    lbl.pack(side=TOP)
    lbl2.pack(side=TOP)
    mentry.pack()
    homebut1.pack(side=LEFT,fill=BOTH)
    homebut2.pack(side=RIGHT,fill=BOTH)
               



    root.mainloop()



    root.destroy()
    
def use_add():  #using address, contains code that opens new window
    gate=2
    print gate
    root=Tk()
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
        lbl2=Label(frame5,text="entered adress is-"+mtext).pack(side=TOP) #use this format to print data on to screen, (dont forget to pack)

    def exit_gui():
        root.destroy()
        sys.exit()

    #proper format- homebut1=Button(frame1,text="go home shelf 1-linearly",command=home1 ,bg="green",fg="blue")
    root.title("AUTOMATIC IRRIGATION SYSTEM- USING ADDRESS")
    lbl = Label(frame1, text="AUTOMATIC IRRIGATION SYSTEM-USING ADDRESS",font=("Times New Roman", 18))

    homebut1=Button(frame2,text="START",command=get_data,bg="green",fg="blue",width=20,height=2)

    homebut2=Button(frame2,text="STOP",command=exit_gui,bg="red",fg="blue",width=20,height=2)


    mentry=Entry(frame1,textvariable=ment)
    lbl2 = Label(frame1, text="Enter the address: ")


    lbl.pack(side=TOP)
    lbl2.pack(side=TOP)
    mentry.pack()
    homebut1.pack(side=LEFT,fill=BOTH)
    homebut2.pack(side=RIGHT,fill=BOTH)
    root.mainloop()
    root.destroy()







root=Tk()
frame1=Frame(root)
frame1.pack(side=TOP)
root.title("AUTOMATIC IRRIGATION SYSTEM")
lbl = Label(frame1, text="1.01 AUTOMATIC IRRIGATION SYSTEM",font=("Times New Roman", 18))
coorbut=Button(frame1,text="Use coordinates",command=use_coor,bg="green",fg="blue",width=20,height=2)

addbut=Button(frame1,text="Use Address",command=use_add,bg="green",fg="blue",width=20,height=2)


lbl.pack(side=TOP)

coorbut.pack(side=LEFT,fill=BOTH)
addbut.pack(side=RIGHT,fill=BOTH)

root.mainloop()










        


    
