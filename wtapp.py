#ECE353 Honors Course Enhancement Project - Fall 2017
#Author: Robert Norton
#Email: rkn8@njit.edu
#4x4, 6x6, and 8x8 Wallace Tree Simulator

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Wallace Tree Simulator")
root.geometry("1000x800") #window size
root.resizable(width=False, height=False) #makes window nonresizable

controlsFrame = Frame(root, width=200, height=800, bd = 1, relief=SUNKEN)
controlsFrame.grid(row=0, column=0, rowspan=4, sticky="nsew")
controlsFrame.grid_propagate(0)

titleFrame = Frame(root, width=800, height=100, bd=1, relief=SUNKEN)
titleFrame.grid(row=0, column=1, sticky="ew")
titleFrame.grid_propagate(0)

title = Label(titleFrame, font=("Helvetica", 40, "bold italic underline"), text="Wallace Tree Simulator")
title.pack(anchor=CENTER)
title.pack_propagate(0)

author = Label(titleFrame, font=("Helvetica", 10, "italic"), text="Created Fall 2017 for ECE353 - Computer Systems Organization and Architecture by John D. Carpinelli - Application by Robert K Norton")
author.pack(side=BOTTOM)
author.pack_propagate(0)


#______________________________________________________________________________________________________
# Canvas 4x4 Setup

canvas4x4 = Canvas(root, width=800, height=700)
canvas4x4.grid(row=1, column=1, sticky="nsew")

original4x4Image = Image.open(sys.path[0]+'/wallTree4x4Image.jpg')
resized4x4Image = original4x4Image.resize((800, 700), Image.ANTIALIAS)
canvas4x4Image = ImageTk.PhotoImage(resized4x4Image)
canvas4x4.create_image(0, 0, image=canvas4x4Image, anchor=NW)

#Carry and Save Values

pp0Val4 = StringVar()
pp0Val4.set("")
pp0Label4 = canvas4x4.create_text(340, 65, tag="pp0Label4", font=("Helvetica", 10, "bold"), justify=CENTER, text=" PP0 "+"("+pp0Val4.get()+")", width=60)

pp1Val4 = StringVar()
pp1Val4.set("")
pp1Label4 = canvas4x4.create_text(460, 65, tag="pp1Label4", font=("Helvetica", 10, "bold"), justify=CENTER, text=" PP1 "+"("+pp1Val4.get()+")", width=60)

pp2Val4 = StringVar()
pp2Val4.set("")
pp2Label4 = canvas4x4.create_text(610, 175, tag="pp2Label4", font=("Helvetica", 10, "bold"), justify=LEFT, text=" PP2 "+"("+pp2Val4.get()+")")

c1Val4 = StringVar()
c1Val4.set("")
c1Label4 = canvas4x4.create_text(280, 240, tag="c1Label4", font=("Helvetica", 10, "bold"), justify=LEFT, text=" C1 "+"("+c1Val4.get()+")")

s1Val4 = StringVar()
s1Val4.set("")
s1Label4 = canvas4x4.create_text(520, 240, tag="s1Label4", font=("Helvetica", 10, "bold"), justify=LEFT, text=" S1 "+"("+s1Val4.get()+")")

pp3Val4 = StringVar()
pp3Val4.set("")
pp3Label4 = canvas4x4.create_text(610, 350, tag="pp3Label4", font=("Helvetica", 10, "bold"), justify=LEFT, text=" PP3 "+"("+pp3Val4.get()+")")

c2Val4 = StringVar()
c2Val4.set("")
c2Label4 = canvas4x4.create_text(280, 415, tag="c2Label4", font=("Helvetica", 10, "bold"), justify=LEFT, text=" C2 "+"("+c2Val4.get()+")")

s2Val4 = StringVar()
s2Val4.set("")
s2Label4 = canvas4x4.create_text(520, 415, tag="s2Label4", font=("Helvetica", 10, "bold"), justify=LEFT, text=" S2 "+"("+s2Val4.get()+")")

finalP4x4Val = StringVar()
finalP4x4Val.set("")
finalP4x4Label = canvas4x4.create_text(400, 635, tag="finalP4x4Label", font=("Helvetica", 10, "bold"), justify=CENTER, text="Final Product "+"("+finalP4x4Val.get()+")", width=90)

#______________________________________________________________________________________________________
# Canvas 6x6 Setup

canvas6x6 = Canvas(root , width=800, height=700)
canvas6x6.grid(row=1, column=1, sticky="nsew")
canvas6x6.grid_forget() #removes 6x6 canvas on start up

original6x6Image = Image.open(sys.path[0]+'/wallTree6x6Image.jpg')
resized6x6Image = original6x6Image.resize((800, 700), Image.ANTIALIAS)
canvas6x6Image = ImageTk.PhotoImage(resized6x6Image)
canvas6x6.create_image(0, 0, image=canvas6x6Image, anchor=NW)

#Carry and Save Values

pp0Val6 = StringVar()
pp0Val6.set("")
pp0Label6 = canvas6x6.create_text(140, 80, tag="pp0Label6", font=("Helvetica", 9, "bold"), justify=CENTER, text=" PP0 "+"("+pp0Val6.get()+")", width=75)

pp1Val6 = StringVar()
pp1Val6.set("")
pp1Label6 = canvas6x6.create_text(240, 80, tag="pp1Label6", font=("Helvetica", 9, "bold"), justify=CENTER, text=" PP1 "+"("+pp1Val6.get()+")", width=75)

pp2Val6 = StringVar()
pp2Val6.set("")
pp2Label6 = canvas6x6.create_text(380, 175, tag="pp2Label6", font=("Helvetica", 9, "bold"), justify=LEFT, text=" PP2 "+"("+pp2Val6.get()+")")

c1Val6 = StringVar()
c1Val6.set("")
c1Label6 = canvas6x6.create_text(80, 240, tag="c1Label6", font=("Helvetica", 9, "bold"), justify=LEFT, text=" C1 "+"("+c1Val6.get()+")")

s1Val6 = StringVar()
s1Val6.set("")
s1Label6 = canvas6x6.create_text(320, 240, tag="s1Label6", font=("Helvetica", 9, "bold"), justify=LEFT, text=" S1 "+"("+s1Val6.get()+")")

pp3Val6 = StringVar()
pp3Val6.set("")
pp3Label6 = canvas6x6.create_text(500, 80, tag="pp3Label6", font=("Helvetica", 9, "bold"), justify=CENTER, text=" PP3 "+"("+pp3Val6.get()+")", width=95)

pp4Val6 = StringVar()
pp4Val6.set("")
pp4Label6 = canvas6x6.create_text(620, 80, tag="pp4Label6", font=("Helvetica", 9, "bold"), justify=CENTER, text=" PP4 "+"("+pp4Val6.get()+")", width=95)

pp5Val6 = StringVar()
pp5Val6.set("")
pp5Label6 = canvas6x6.create_text(730, 165, tag="pp5Label6", font=("Helvetica", 9, "bold"), justify=LEFT, text=" PP5 "+"("+pp5Val6.get()+")")

c2Val6 = StringVar()
c2Val6.set("")
c2Label6 = canvas6x6.create_text(450, 240, tag="c2Label6", font=("Helvetica", 9, "bold"), justify=LEFT, text=" C2 "+"("+c2Val6.get()+")")

s2Val6 = StringVar()
s2Val6.set("")
s2Label6 = canvas6x6.create_text(680, 240, tag="s2Label6", font=("Helvetica", 9, "bold"), justify=LEFT, text=" S2 "+"("+s2Val6.get()+")")

c3Val6 = StringVar()
c3Val6.set("")
c3Label6 = canvas6x6.create_text(80, 360, tag="c3Label6", font=("Helvetica", 9, "bold"), justify=LEFT, text=" C3 "+"("+c3Val6.get()+")")

s3Val6 = StringVar()
s3Val6.set("")
s3Label6 = canvas6x6.create_text(320, 360, tag="s3Label6", font=("Helvetica", 9, "bold"), justify=LEFT, text=" S3 "+"("+s3Val6.get()+")")

c4Val6 = StringVar()
c4Val6.set("")
c4Label6 = canvas6x6.create_text(80, 480, tag="c4Label6", font=("Helvetica", 9, "bold"), justify=LEFT, text=" C4 "+"("+c4Val6.get()+")")

s4Val6 = StringVar()
s4Val6.set("")
s4Label6 = canvas6x6.create_text(320, 480, tag="s4Label6", font=("Helvetica", 9, "bold"), justify=LEFT, text=" S4 "+"("+s4Val6.get()+")")

finalP6x6Val = StringVar()
finalP6x6Val.set("")
finalP6x6Label = canvas6x6.create_text(200, 635, tag="finalP6x6Label", font=("Helvetica", 9, "bold"), justify=CENTER, text="Final Product "+"("+finalP6x6Val.get()+")", width=95)

#______________________________________________________________________________________________________
# Canvas 8x8 Setup

canvas8x8 = Canvas(root , width=800, height=700)
canvas8x8.grid(row=1, column=1, sticky="nsew")
canvas8x8.grid_forget() #removes 8x8 canvas on start up

original8x8Image = Image.open(sys.path[0]+'/wallTree8x8Image.jpg')
resized8x8Image = original8x8Image.resize((800, 700), Image.ANTIALIAS)
canvas8x8Image = ImageTk.PhotoImage(resized8x8Image)
canvas8x8.create_image(0, 0, image=canvas8x8Image, anchor=NW)

#Carry and Save Values

#Start of first two CSA on left
pp0Val8 = StringVar()
pp0Val8.set("")
pp0Label8 = canvas8x8.create_text(130, 30, tag="pp0Label8", font=("Helvetica", 9, "bold"), justify=CENTER, text=" PP0 "+"("+pp0Val8.get()+")", width=90)

pp1Val8 = StringVar()
pp1Val8.set("")
pp1Label8 = canvas8x8.create_text(220, 30, tag="pp1Label8", font=("Helvetica", 9, "bold"), justify=CENTER, text=" PP1 "+"("+pp1Val8.get()+")", width=90)

pp2Val8 = StringVar()
pp2Val8.set("")
pp2Label8 = canvas8x8.create_text(350, 120, tag="pp2Label8", font=("Helvetica", 9, "bold"), justify=LEFT, text=" PP2 "+"("+pp2Val8.get()+")")

c1Val8 = StringVar()
c1Val8.set("")
c1Label8 = canvas8x8.create_text(65, 170, tag="c1Label8", font=("Helvetica", 9, "bold"), justify=CENTER, text=" C1 "+"("+c1Val8.get()+")", width=120)

s1Val8 = StringVar()
s1Val8.set("")
s1Label8 = canvas8x8.create_text(280, 170, tag="s1Label8", font=("Helvetica", 9, "bold"), justify=LEFT, text=" S1 "+"("+s1Val8.get()+")")

pp7Val8 = StringVar()
pp7Val8.set("")
pp7Label8 = canvas8x8.create_text(370, 230, tag="pp7Label8", font=("Helvetica", 9, "bold"), justify=LEFT, text=" PP7 "+"("+pp7Val8.get()+")")

c3Val8 = StringVar()
c3Val8.set("")
c3Label8 = canvas8x8.create_text(70, 280, tag="c3Label8", font=("Helvetica", 9, "bold"), justify=CENTER, text=" C3 "+"("+c3Val8.get()+")", width=120)

s3Val8 = StringVar()
s3Val8.set("")
s3Label8 = canvas8x8.create_text(300, 280, tag="s3Label8", font=("Helvetica", 9, "bold"), justify=LEFT, text=" S3 "+"("+s3Val8.get()+")")

#Start of first two CSA on right

pp3Val8 = StringVar()
pp3Val8.set("")
pp3Label8 = canvas8x8.create_text(485, 30, tag="pp3Label8", font=("Helvetica", 9, "bold"), justify=CENTER, text=" PP3 "+"("+pp3Val8.get()+")", width=110)

pp4Val8 = StringVar()
pp4Val8.set("")
pp4Label8 = canvas8x8.create_text(595, 30, tag="pp4Label8", font=("Helvetica", 9, "bold"), justify=CENTER, text=" PP4 "+"("+pp4Val8.get()+")", width=110)

pp5Val8 = StringVar()
pp5Val8.set("")
pp5Label8 = canvas8x8.create_text(715, 120, tag="pp5Label8", font=("Helvetica", 9, "bold"), justify=CENTER, text=" PP5 "+"("+pp5Val8.get()+")", width=120)

c2Val8 = StringVar()
c2Val8.set("")
c2Label8 = canvas8x8.create_text(420, 170, tag="c2Label8", font=("Helvetica", 9, "bold"), justify=CENTER, text=" C2 "+"("+c2Val8.get()+")", width=120)

s2Val8 = StringVar()
s2Val8.set("")
s2Label8 = canvas8x8.create_text(660, 170, tag="s2Label8", font=("Helvetica", 9, "bold"), justify=LEFT, text=" S2 "+"("+s2Val8.get()+")")

pp6Val8 = StringVar()
pp6Val8.set("")
pp6Label8 = canvas8x8.create_text(715, 230, tag="pp6Label8", font=("Helvetica", 9, "bold"), justify=CENTER, text=" PP6 "+"("+pp6Val8.get()+")", width=120)

c4Val8 = StringVar()
c4Val8.set("")
c4Label8 = canvas8x8.create_text(420, 320, tag="c4Label8", font=("Helvetica", 9, "bold"), justify=CENTER, text=" C4 "+"("+c4Val8.get()+")", width=130)

s4Val8 = StringVar()
s4Val8.set("")
s4Label8 = canvas8x8.create_text(660, 320, tag="s4Label8", font=("Helvetica", 9, "bold"), justify=LEFT, text=" S4 "+"("+s4Val8.get()+")")

c5Val8 = StringVar()
c5Val8.set("")
c5Label8 = canvas8x8.create_text(65, 390, tag="c5Label8", font=("Helvetica", 9, "bold"), justify=CENTER, text=" C5 "+"("+c5Val8.get()+")", width=120)

s5Val8 = StringVar()
s5Val8.set("")
s5Label8 = canvas8x8.create_text(300, 390, tag="s5Label8", font=("Helvetica", 9, "bold"), justify=LEFT, text=" S5 "+"("+s5Val8.get()+")")

c6Val8 = StringVar()
c6Val8.set("")
c6Label8 = canvas8x8.create_text(65, 500, tag="c6Label8", font=("Helvetica", 9, "bold"), justify=CENTER, text=" C6 "+"("+c6Val8.get()+")", width=120)

s6Val8 = StringVar()
s6Val8.set("")
s6Label8 = canvas8x8.create_text(300, 500, tag="s6Label8", font=("Helvetica", 9, "bold"), justify=LEFT, text=" S6 "+"("+s6Val8.get()+")")

finalP8x8Val = StringVar()
finalP8x8Val.set("")
finalP8x8Label = canvas8x8.create_text(180, 650, tag="finalP8x8Label", font=("Helvetica", 9, "bold"), justify=CENTER, text="Final Product "+"("+finalP8x8Val.get()+")", width=130)


#______________________________________________________________________________________________________
# General Functions for GUI interaction

def update_to_4x4(event):
    op1HexVal.set("")
    op1DecVal.set("")
    op2HexVal.set("")
    op2DecVal.set("")

    pp0Val4.set("")
    canvas4x4.itemconfig(pp0Label4, text=" PP0 " + "(" + pp0Val4.get() + ")")
    pp1Val4.set("")
    canvas4x4.itemconfig(pp1Label4, text=" PP1 " + "(" + pp1Val4.get() + ")")
    pp2Val4.set("")
    canvas4x4.itemconfig(pp2Label4, text=" PP2 " + "(" + pp2Val4.get() + ")")
    c1Val4.set("")
    canvas4x4.itemconfig(c1Label4, text=" C1 " + "(" + c1Val4.get() + ")")
    s1Val4.set("")
    canvas4x4.itemconfig(s1Label4, text=" S1 " + "(" + s1Val4.get() + ")")
    pp3Val4.set("")
    canvas4x4.itemconfig(pp3Label4, text=" PP3 " + "(" + pp3Val4.get() + ")")
    c2Val4.set("")
    canvas4x4.itemconfig(c2Label4, text=" C2 " + "(" + c2Val4.get() + ")")
    s2Val4.set("")
    canvas4x4.itemconfig(s2Label4, text=" S2 " + "(" + s2Val4.get() + ")")
    finalP4x4Val.set("")
    canvas4x4.itemconfig(finalP4x4Label, text="Final Product " + "(" + finalP4x4Val.get() + ")")

    op1BinaryValue.delete(0, END)
    op2BinaryValue.delete(0, END)
    canvas4x4.grid(row=1, column=1, sticky="nsew")
    canvas6x6.grid_forget()
    canvas8x8.grid_forget()
    root.update_idletasks()


def update_to_6x6(event):
    op1HexVal.set("")
    op1DecVal.set("")
    op2HexVal.set("")
    op2DecVal.set("")

    pp0Val6.set("")
    canvas6x6.itemconfig(pp0Label6, text=" PP0 " + "(" + pp0Val6.get() + ")")
    pp1Val6.set("")
    canvas6x6.itemconfig(pp1Label6, text=" PP1 " + "(" + pp1Val6.get() + ")")
    pp2Val6.set("")
    canvas6x6.itemconfig(pp2Label6, text=" PP2 " + "(" + pp2Val6.get() + ")")
    c1Val6.set("")
    canvas6x6.itemconfig(c1Label6, text=" C1 " + "(" + c1Val6.get() + ")")
    s1Val6.set("")
    canvas6x6.itemconfig(s1Label6, text=" S1 " + "(" + s1Val6.get() + ")")
    pp3Val6.set("")
    canvas6x6.itemconfig(pp3Label6, text=" PP3 " + "(" + pp3Val6.get() + ")")
    pp4Val6.set("")
    canvas6x6.itemconfig(pp4Label6, text=" PP4 " + "(" + pp4Val6.get() + ")")
    pp5Val6.set("")
    canvas6x6.itemconfig(pp5Label6, text=" PP5 " + "(" + pp5Val6.get() + ")")
    c2Val6.set("")
    canvas6x6.itemconfig(c2Label6, text=" C2 " + "(" + c2Val6.get() + ")")
    s2Val6.set("")
    canvas6x6.itemconfig(s2Label6, text=" S2 " + "(" + s2Val6.get() + ")")
    c3Val6.set("")
    canvas6x6.itemconfig(c3Label6, text=" C3 " + "(" + c3Val6.get() + ")")
    s3Val6.set("")
    canvas6x6.itemconfig(s3Label6, text=" S3 " + "(" + s3Val6.get() + ")")
    c4Val6.set("")
    canvas6x6.itemconfig(c4Label6, text=" C4 " + "(" + c4Val6.get() + ")")
    s4Val6.set("")
    canvas6x6.itemconfig(s4Label6, text=" S4 " + "(" + s4Val6.get() + ")")
    finalP6x6Val.set("")
    canvas6x6.itemconfig(finalP6x6Label, text="Final Product " + "(" + finalP6x6Val.get() + ")")

    op1BinaryValue.delete(0, END)
    op2BinaryValue.delete(0, END)
    canvas4x4.grid_forget()
    canvas6x6.grid(row=1, column=1, sticky="nsew")
    canvas8x8.grid_forget()


def update_to_8x8(event):
    op1HexVal.set("")
    op1DecVal.set("")
    op2HexVal.set("")
    op2DecVal.set("")

    pp0Val8.set("")
    canvas8x8.itemconfig(pp0Label8, text=" PP0 " + "(" + pp0Val8.get() + ")")
    pp1Val8.set("")
    canvas8x8.itemconfig(pp1Label8, text=" PP1 " + "(" + pp1Val8.get() + ")")
    pp2Val8.set("")
    canvas8x8.itemconfig(pp2Label8, text=" PP2 " + "(" + pp2Val8.get() + ")")
    c1Val8.set("")
    canvas8x8.itemconfig(c1Label8, text=" C1 " + "(" + c1Val8.get() + ")")
    s1Val8.set("")
    canvas8x8.itemconfig(s1Label8, text=" S1 " + "(" + s1Val8.get() + ")")
    pp3Val8.set("")
    canvas8x8.itemconfig(pp3Label8, text=" PP3 " + "(" + pp3Val8.get() + ")")
    pp4Val8.set("")
    canvas8x8.itemconfig(pp4Label8, text=" PP4 " + "(" + pp4Val8.get() + ")")
    pp5Val8.set("")
    canvas8x8.itemconfig(pp5Label8, text=" PP5 " + "(" + pp5Val8.get() + ")")
    c2Val8.set("")
    canvas8x8.itemconfig(c2Label8, text=" C2 " + "(" + c2Val8.get() + ")")
    s2Val8.set("")
    canvas8x8.itemconfig(s2Label8, text=" S2 " + "(" + s2Val8.get() + ")")
    pp7Val8.set("")
    canvas8x8.itemconfig(pp7Label8, text=" PP7 " + "(" + pp7Val8.get() + ")")
    c3Val8.set("")
    canvas8x8.itemconfig(c3Label8, text=" C3 " + "(" + c3Val8.get() + ")")
    s3Val8.set("")
    canvas8x8.itemconfig(s3Label8, text=" S3 " + "(" + s3Val8.get() + ")")
    pp6Val8.set("")
    canvas8x8.itemconfig(pp6Label8, text=" PP6 " + "(" + pp6Val8.get() + ")")
    c4Val8.set("")
    canvas8x8.itemconfig(c4Label8, text=" C4 " + "(" + c4Val8.get() + ")")
    s4Val8.set("")
    canvas8x8.itemconfig(s4Label8, text=" S4 " + "(" + s4Val8.get() + ")")
    c5Val8.set("")
    canvas8x8.itemconfig(c5Label8, text=" C5 " + "(" + c5Val8.get() + ")")
    s5Val8.set("")
    canvas8x8.itemconfig(s5Label8, text=" S5 " + "(" + s5Val8.get() + ")")
    c6Val8.set("")
    canvas8x8.itemconfig(c6Label8, text=" C6 " + "(" + c6Val8.get() + ")")
    s6Val8.set("")
    canvas8x8.itemconfig(s6Label8, text=" S6 " + "(" + s6Val8.get() + ")")
    finalP8x8Val.set("")
    canvas8x8.itemconfig(finalP8x8Label, text="Final Product " + "(" + finalP8x8Val.get() + ")")

    op1BinaryValue.delete(0, END)
    op2BinaryValue.delete(0, END)
    canvas4x4.grid_forget()
    canvas6x6.grid_forget()
    canvas8x8.grid(row=1, column=1, sticky="nsew")


wtType = IntVar()
wtType.set(1)
wtWidth=7
typeLabelFrame = LabelFrame(controlsFrame, text="Please choose a type:", padx=8, pady=12)
type4x4 = Radiobutton(typeLabelFrame, text="4x4", indicatoron=0, variable=wtType, value=1, width=wtWidth, height=3)
type6x6 = Radiobutton(typeLabelFrame, text="6x6", indicatoron=0, variable=wtType, value=2, width=wtWidth, height=3)
type8x8 = Radiobutton(typeLabelFrame, text="8x8", indicatoron=0, variable=wtType, value=3, width=wtWidth, height=3)

typeLabelFrame.grid(row=0, column=0)
type4x4.grid(row=0, column=0)
type6x6.grid(row=0, column=1)
type8x8.grid(row=0, column=2)

type4x4.bind("<Button-1>", update_to_4x4)
type6x6.bind("<Button-1>", update_to_6x6)
type8x8.bind("<Button-1>", update_to_8x8)

#______________________________________________________________________________________________________
#Operand 1 Controls

def binarycheck1(event):
    new = op1BinaryValue.get()
    initial = new[0:-1]
    lastchar = new[len(new)-1]
    if wtType.get() == 1:
        if len(new) > 4:
            op1BinaryValue.delete(0, END)
            op1BinaryValue.insert(0, initial)
            root.update_idletasks()
    elif wtType.get() == 2:
        if len(new) > 6:
            op1BinaryValue.delete(0, END)
            op1BinaryValue.insert(0, initial)
            root.update_idletasks()
    elif wtType.get() == 3:
        if len(new) > 8:
            op1BinaryValue.delete(0, END)
            op1BinaryValue.insert(0, initial)
            root.update_idletasks()
    if lastchar == '0':
        op1HexVal.set(hex(int(op1BinaryValue.get(), 2))) #updates label
        op1DecVal.set(int(op1BinaryValue.get(), 2))  # updates label
        root.update_idletasks()
    elif lastchar == '1':
        op1HexVal.set(hex(int(op1BinaryValue.get(), 2))) #updates label
        op1DecVal.set(int(op1BinaryValue.get(), 2))  # updates label
        root.update_idletasks()
    else:
        op1BinaryValue.delete(0, END)
        op1BinaryValue.insert(0, initial)
        root.update_idletasks()

def entry_check(new):
    if new in '01':
        return True
    else:
        return False


op1HexVal = StringVar()
op1DecVal = StringVar()
op1HexVal.set("")
op1DecVal.set("")

op1LabelFrame = LabelFrame(controlsFrame, text="Operand 1", padx=5, pady=12)
op1LabelFrame.grid(row=1, column=0)

op1HexLabel = Label(op1LabelFrame, text="Hex: ")
op1HexValue = Label(op1LabelFrame, textvariable=op1HexVal)

op1DecLabel = Label(op1LabelFrame, text="Dec: ")
op1DecValue = Label(op1LabelFrame, textvariable=op1DecVal)

op1BinaryLabel = Label(op1LabelFrame, text="Binary: 0b")
op1BinaryValue = Entry(op1LabelFrame, validatecommand=(entry_check, '%P'))

op1BinaryLabel.grid(row=0, column=0)
op1BinaryValue.grid(row=0, column=1)
op1HexLabel.grid(row=1, column=0)
op1HexValue.grid(row=1, column=1)
op1DecLabel.grid(row=2, column=0)
op1DecValue.grid(row=2, column=1)

op1BinaryValue.bind(sequence='<KeyRelease>', func=binarycheck1)

#______________________________________________________________________________________________________
#Operand 2 Controls

def binarycheck2(event):
    new = op2BinaryValue.get()
    initial = new[0:-1]
    lastchar = 0
    if len(new) > 0:
        lastchar = new[len(new)-1]
    if wtType.get() == 1:
        if len(new) > 4:
            op2BinaryValue.delete(0, END)
            op2BinaryValue.insert(0, initial)
            root.update_idletasks()
    elif wtType.get() == 2:
        if len(new) > 6:
            op2BinaryValue.delete(0, END)
            op2BinaryValue.insert(0, initial)
            root.update_idletasks()
    elif wtType.get() == 3:
        if len(new) > 8:
            op2BinaryValue.delete(0, END)
            op2BinaryValue.insert(0, initial)
            root.update_idletasks()
    if lastchar == '0':
        op2HexVal.set(hex(int(op2BinaryValue.get(), 2))) #updates label
        op2DecVal.set(int(op2BinaryValue.get(), 2))  # updates label
        root.update_idletasks()
    elif lastchar == '1':
        op2HexVal.set(hex(int(op2BinaryValue.get(), 2))) #updates label
        op2DecVal.set(int(op2BinaryValue.get(), 2))  # updates label
        root.update_idletasks()
    else:
        op2BinaryValue.delete(0, END)
        op2BinaryValue.insert(0, initial)
        root.update_idletasks()

def entry_check(new):
    if new in '01':
        return True
    else:
        return False


op2HexVal = StringVar()
op2DecVal = StringVar()
op2HexVal.set("")
op2DecVal.set("")

op2LabelFrame = LabelFrame(controlsFrame, text="Operand 2", padx=5, pady=12)
op2LabelFrame.grid(row=2, column=0)

op2HexLabel = Label(op2LabelFrame, text="Hex: ")
op2HexValue = Label(op2LabelFrame, textvariable=op2HexVal)

op2DecLabel = Label(op2LabelFrame, text="Dec: ")
op2DecValue = Label(op2LabelFrame, textvariable=op2DecVal)

op2BinaryLabel = Label(op2LabelFrame, text="Binary: 0b")
op2BinaryValue = Entry(op2LabelFrame, validatecommand=(entry_check, '%P'))

op2BinaryLabel.grid(row=0, column=0)
op2BinaryValue.grid(row=0, column=1)
op2HexLabel.grid(row=1, column=0)
op2HexValue.grid(row=1, column=1)
op2DecLabel.grid(row=2, column=0)
op2DecValue.grid(row=2, column=1)

op2BinaryValue.bind(sequence='<KeyRelease>', func=binarycheck2)

#______________________________________________________________________________________________________
#Calculate Button Controls and Logic

def calcSave(op1, op2, op3):
    maxL = len(op1)
    curSave = []

    if maxL < len(op2): maxL = len(op2) # these two if statements determine which operand is the longest
    if maxL < len(op3): maxL = len(op3)

    while len(op1) != maxL:  # these makes all operands the same length by padding zeros to the front of the short operands
        op1.insert(0, '0')
    while len(op2) != maxL:
        op2.insert(0, '0')
    while len(op3) != maxL:
        op3.insert(0, '0')
    while len(curSave) != maxL:
        curSave.append('0')

    for bit in range(maxL-1, -1, -1):  # this creates the new list for the Save result
        if op1[bit] == '1' and op2[bit] == '1' and op3[bit] == '1':
            curSave[bit] = '1'
        elif op1[bit] == '1' and op2[bit] == '0' and op3[bit] == '0':
            curSave[bit] = '1'
        elif op1[bit] == '0' and op2[bit] == '1' and op3[bit] == '0':
            curSave[bit] = '1'
        elif op1[bit] == '0' and op2[bit] == '0' and op3[bit] == '1':
            curSave[bit] = '1'
        else:
            pass # do nothing the bit stays zero

    return curSave


def calcCarry(op1, op2, op3):
    maxL = len(op1)
    carL = maxL + 1
    curCarry = ['0']

    if maxL < len(op2): maxL = len(op2)  # these two if statements determine which operand is the longest
    if maxL < len(op3): maxL = len(op3)

    while len(op1) != carL:  # these makes all operands the same length by padding zeros to the front of the short operands
        op1.insert(0, '0')
    while len(op2) != carL:
        op2.insert(0, '0')
    while len(op3) != carL:
        op3.insert(0, '0')
    while len(curCarry) != carL:
        curCarry.insert(0, '0')

    for bit in range(maxL-1, -1, -1):  # this creates the new list for the Save result
        if   op1[bit] == '0' and op2[bit] == '1' and op3[bit] == '1':
            if bit == 0: curCarry[bit] = '1'
            else: curCarry[bit-1] = '1'
        elif op1[bit] == '1' and op2[bit] == '0' and op3[bit] == '1':
            if bit == 0: curCarry[bit] = '1'
            else: curCarry[bit-1] = '1'
        elif op1[bit] == '1' and op2[bit] == '1' and op3[bit] == '0':
            if bit == 0: curCarry[bit] = '1'
            else: curCarry[bit-1] = '1'
        elif op1[bit] == '1' and op2[bit] == '1' and op3[bit] == '1':
            if bit == 0: curCarry[bit] = '1'
            else: curCarry[bit-1] = '1'
        else:
            curCarry[bit-1] = '0'

    return curCarry

def calcParallel(op1, op2):
    maxL = len(op1)
    sumL = maxL + 1
    carBit = '0'
    curSum = ['0']

    if maxL < len(op2): maxL = len(op2)  # these two if statements determine which operand is the longest

    while len(op1) != maxL:  # these makes all operands the same length by padding zeros to the front of the short operands
        op1.insert(0, '0')
    while len(op2) != maxL:
        op2.insert(0, '0')
    while len(curSum) != sumL:
        curSum.insert(0, '0')

    for bit in range(maxL - 1, -1, -1):  # this creates the new list for the Save result
        if   op1[bit] == '1' and op2[bit] == '1' and carBit == '0':
            carBit = '1'
        elif op1[bit] == '1' and op2[bit] == '1' and carBit == '1':
            curSum[bit] = '1'
        elif op1[bit] == '1' and op2[bit] == '0' and carBit == '0':
            curSum[bit] = '1'
        elif op1[bit] == '1' and op2[bit] == '0' and carBit == '1':
            carBit = '1'
        elif op1[bit] == '0' and op2[bit] == '1' and carBit == '0':
            curSum[bit] = '1'
        elif op1[bit] == '0' and op2[bit] == '1' and carBit == '1':
            carBit = '1'
        elif op1[bit] == '0' and op2[bit] == '0' and carBit == '1':
            curSum[bit] = '1'
            carBit = '0'
        elif op1[bit] == '0' and op2[bit] == '0' and carBit == '0':
            curSum[bit] = '0'
            carBit = '0'

    return curSum


def calcLogic(event):

    if wtType.get() == 1: #if the current wallace tree size if 4x4
        operand1 = op1BinaryValue.get()
        operand2 = op2BinaryValue.get()
        if len(operand1) != 4 or len(operand2) != 4:
            inEr4Win = Toplevel()
            inEr4Win.title("4x4 Wallace Tree Input Error")
            error4 = Message(inEr4Win, text="ERROR!" + "\n" + "Both Operand 1 and Operand 2 must be 4-bits wide.", font=("Helvetica", 12, "italic"), justify=CENTER, width=250, padx=20, pady=20)
            error4.pack()
            disButton = Button(inEr4Win, text="Dismiss", padx=10, pady=5, command=inEr4Win.destroy)
            disButton.pack(padx=10, pady=5)

        if operand2[3]== '0': pp0 = ['0', '0', '0', '0']
        else: pp0 = [operand1[3], operand1[2], operand1[1], operand1[0]]
        if operand2[2]== '0': pp1 = ['0', '0', '0', '0']
        else: pp1 = [operand1[3], operand1[2], operand1[1], operand1[0], '0']
        if operand2[1]== '0': pp2 = ['0', '0', '0', '0']
        else: pp2 = [operand1[3], operand1[2], operand1[1], operand1[0], '0', '0']
        if operand2[0]== '0': pp3 = ['0', '0', '0', '0']
        else: pp3 = [operand1[3], operand1[2], operand1[1], operand1[0], '0', '0', '0']

        s1 = calcSave(pp0, pp1, pp2)
        c1 = calcCarry(pp0, pp1, pp2)
        s2 = calcSave(s1, c1, pp3)
        c2 = calcCarry(s1, c1, pp3)
        finalP4 = calcParallel(s2, c2)

        for list in [pp0, pp1, pp2, pp3, s1, c1, s2, c2, finalP4]: # removes leading zeros on all binary values
            if list.count('1') != 0:
                while list[0] == "0":
                    list.pop(0)
            else:
                while len(list) > 1:  # puts just a single zero for all zero values
                    list.pop(0)

        pp0str = ""
        pp1str = ""
        pp2str = ""
        c1str = ""
        s1str = ""
        pp3str = ""
        c2str = ""
        s2str = ""
        finalP4str = ""
        pp0Val4.set(pp0str.join(pp0))
        canvas4x4.itemconfig(pp0Label4, text=" PP0 "+"("+pp0Val4.get()+")")
        pp1Val4.set(pp1str.join(pp1))
        canvas4x4.itemconfig(pp1Label4, text=" PP1 " + "(" + pp1Val4.get() + ")")
        pp2Val4.set(pp2str.join(pp2))
        canvas4x4.itemconfig(pp2Label4, text=" PP2 " + "(" + pp2Val4.get() + ")")
        c1Val4.set(c1str.join(c1))
        canvas4x4.itemconfig(c1Label4, text=" C1 " + "(" + c1Val4.get() + ")")
        s1Val4.set(s1str.join(s1))
        canvas4x4.itemconfig(s1Label4, text=" S1 " + "(" + s1Val4.get() + ")")
        pp3Val4.set(pp3str.join(pp3))
        canvas4x4.itemconfig(pp3Label4, text=" PP3 " + "(" + pp3Val4.get() + ")")
        c2Val4.set(c2str.join(c2))
        canvas4x4.itemconfig(c2Label4, text=" C2 " + "(" + c2Val4.get() + ")")
        s2Val4.set(s2str.join(s2))
        canvas4x4.itemconfig(s2Label4, text=" S2 " + "(" + s2Val4.get() + ")")
        finalP4x4Val.set(finalP4str.join(finalP4))
        canvas4x4.itemconfig(finalP4x4Label, text="Final Product "+"("+finalP4x4Val.get()+")")

        root.update_idletasks()

    elif wtType.get() == 2: #if the current wallace tree size if 6x6
        operand1 = op1BinaryValue.get()
        operand2 = op2BinaryValue.get()
        if len(operand1) != 6 or len(operand2) != 6:
            inEr6Win = Toplevel()
            inEr6Win.title("6x6 Wallace Tree Input Error")
            error6 = Message(inEr6Win, text="ERROR!" + "\n" + "Both Operand 1 and Operand 2 must be 6-bits wide.", font=("Helvetica", 12, "italic"), justify=CENTER, width=250, padx=20, pady=20)
            error6.pack()
            disButton = Button(inEr6Win, text="Dismiss", padx=10, pady=5, command=inEr6Win.destroy)
            disButton.pack(padx=10, pady=5)

        if operand2[5] == '0': pp0 = ['0', '0', '0', '0', '0', '0']
        else: pp0 = [operand1[0], operand1[1], operand1[2], operand1[3], operand1[4], operand1[5]]
        if operand2[4] == '0': pp1 = ['0', '0', '0', '0', '0', '0']
        else: pp1 = [operand1[0], operand1[1], operand1[2], operand1[3], operand1[4], operand1[5], '0']
        if operand2[3] == '0': pp2 = ['0', '0', '0', '0', '0', '0']
        else: pp2 = [operand1[0], operand1[1], operand1[2], operand1[3], operand1[4], operand1[5], '0', '0']
        if operand2[2] == '0': pp3 = ['0', '0', '0', '0', '0', '0']
        else: pp3 = [operand1[0], operand1[1], operand1[2], operand1[3], operand1[4], operand1[5], '0', '0', '0']
        if operand2[1] == '0': pp4 = ['0', '0', '0', '0', '0', '0']
        else: pp4 = [operand1[0], operand1[1], operand1[2], operand1[3], operand1[4], operand1[5], '0', '0', '0', '0']
        if operand2[0] == '0': pp5 = ['0', '0', '0', '0', '0', '0']
        else: pp5 = [operand1[0], operand1[1], operand1[2], operand1[3], operand1[4], operand1[5], '0', '0', '0', '0', '0']

        s1 = calcSave(pp0, pp1, pp2)
        c1 = calcCarry(pp0, pp1, pp2)
        s2 = calcSave(pp3, pp4, pp5)
        c2 = calcCarry(pp3, pp4, pp5)
        s3 = calcSave(s1, c1, c2)
        c3 = calcCarry(s1, c1, c2)
        s4 = calcSave(s3, c3, s2)
        c4 = calcCarry(s3, c3, s2)
        finalP6 = calcParallel(s4, c4)

        for list in [pp0, pp1, pp2, pp3, pp4, pp5, s1, c1, s2, c2, s3, c3, s4, c4, finalP6]: # removes leading zeros on all binary values
            if list.count('1') != 0:
                while list[0] == "0":
                    list.pop(0)
            else:
                while len(list) > 1:  # puts just a single zero for all zero values
                    list.pop(0)


        pp0str = ""
        pp1str = ""
        pp2str = ""
        c1str = ""
        s1str = ""
        pp3str = ""
        pp4str = ""
        pp5str = ""
        c2str = ""
        s2str = ""
        c3str = ""
        s3str = ""
        c4str = ""
        s4str = ""
        finalP6str = ""
        pp0Val6.set(pp0str.join(pp0))
        canvas6x6.itemconfig(pp0Label6, text=" PP0 " + "(" + pp0Val6.get() + ")")
        pp1Val6.set(pp1str.join(pp1))
        canvas6x6.itemconfig(pp1Label6, text=" PP1 " + "(" + pp1Val6.get() + ")")
        pp2Val6.set(pp2str.join(pp2))
        canvas6x6.itemconfig(pp2Label6, text=" PP2 " + "(" + pp2Val6.get() + ")")
        c1Val6.set(c1str.join(c1))
        canvas6x6.itemconfig(c1Label6, text=" C1 " + "(" + c1Val6.get() + ")")
        s1Val6.set(s1str.join(s1))
        canvas6x6.itemconfig(s1Label6, text=" S1 " + "(" + s1Val6.get() + ")")
        pp3Val6.set(pp3str.join(pp3))
        canvas6x6.itemconfig(pp3Label6, text=" PP3 " + "(" + pp3Val6.get() + ")")
        pp4Val6.set(pp4str.join(pp4))
        canvas6x6.itemconfig(pp4Label6, text=" PP4 " + "(" + pp4Val6.get() + ")")
        pp5Val6.set(pp5str.join(pp5))
        canvas6x6.itemconfig(pp5Label6, text=" PP5 " + "(" + pp5Val6.get() + ")")
        c2Val6.set(c2str.join(c2))
        canvas6x6.itemconfig(c2Label6, text=" C2 " + "(" + c2Val6.get() + ")")
        s2Val6.set(s2str.join(s2))
        canvas6x6.itemconfig(s2Label6, text=" S2 " + "(" + s2Val6.get() + ")")
        c3Val6.set(c3str.join(c3))
        canvas6x6.itemconfig(c3Label6, text=" C3 " + "(" + c3Val6.get() + ")")
        s3Val6.set(s3str.join(s3))
        canvas6x6.itemconfig(s3Label6, text=" S3 " + "(" + s3Val6.get() + ")")
        c4Val6.set(c4str.join(c4))
        canvas6x6.itemconfig(c4Label6, text=" C4 " + "(" + c4Val6.get() + ")")
        s4Val6.set(s4str.join(s4))
        canvas6x6.itemconfig(s4Label6, text=" S4 " + "(" + s4Val6.get() + ")")
        finalP6x6Val.set(finalP6str.join(finalP6))
        canvas6x6.itemconfig(finalP6x6Label, text="Final Product " + "(" + finalP6x6Val.get() + ")")

        root.update_idletasks()

    elif wtType.get() == 3: #if the current wallace tree size if 8x8
        operand1 = op1BinaryValue.get()
        operand2 = op2BinaryValue.get()
        if len(operand1) != 8 or len(operand2) != 8:
            inEr8Win = Toplevel()
            inEr8Win.title("8x8 Wallace Tree Input Error")
            error8 = Message(inEr8Win, text="ERROR!" + "\n" + "Both Operand 1 and Operand 2 must be 8-bits wide.", font=("Helvetica", 12, "italic"), justify=CENTER, width=250, padx=20, pady=20)
            error8.pack()
            disButton = Button(inEr8Win, text="Dismiss", padx=10, pady=5, command=inEr8Win.destroy)
            disButton.pack(padx=10, pady=5)

        if operand2[7] == '0': pp0 = ['0', '0', '0', '0', '0', '0', '0', '0']
        else: pp0 = [operand1[0], operand1[1], operand1[2], operand1[3], operand1[4], operand1[5], operand1[6], operand1[7]]
        if operand2[6] == '0': pp1 = ['0', '0', '0', '0', '0', '0', '0', '0']
        else: pp1 = [operand1[0], operand1[1], operand1[2], operand1[3], operand1[4], operand1[5], operand1[6], operand1[7], '0']
        if operand2[5] == '0': pp2 = ['0', '0', '0', '0', '0', '0', '0', '0']
        else: pp2 = [operand1[0], operand1[1], operand1[2], operand1[3], operand1[4], operand1[5], operand1[6], operand1[7], '0', '0']
        if operand2[4] == '0': pp3 = ['0', '0', '0', '0', '0', '0', '0', '0']
        else: pp3 = [operand1[0], operand1[1], operand1[2], operand1[3], operand1[4], operand1[5], operand1[6], operand1[7], '0', '0', '0']
        if operand2[3] == '0': pp4 = ['0', '0', '0', '0', '0', '0', '0', '0']
        else: pp4 = [operand1[0], operand1[1], operand1[2], operand1[3], operand1[4], operand1[5], operand1[6], operand1[7], '0', '0', '0', '0']
        if operand2[2] == '0': pp5 = ['0', '0', '0', '0', '0', '0', '0', '0']
        else: pp5 = [operand1[0], operand1[1], operand1[2], operand1[3], operand1[4], operand1[5], operand1[6], operand1[7], '0', '0', '0', '0', '0']
        if operand2[1] == '0': pp6 = ['0', '0', '0', '0', '0', '0', '0', '0']
        else: pp6 = [operand1[0], operand1[1], operand1[2], operand1[3], operand1[4], operand1[5], operand1[6], operand1[7], '0', '0', '0', '0', '0', '0']
        if operand2[0] == '0': pp7 = ['0', '0', '0', '0', '0', '0', '0', '0']
        else: pp7 = [operand1[0], operand1[1], operand1[2], operand1[3], operand1[4], operand1[5], operand1[6], operand1[7], '0', '0', '0', '0', '0', '0', '0']

        s1 = calcSave(pp0, pp1, pp2)
        c1 = calcCarry(pp0, pp1, pp2)
        s2 = calcSave(pp3, pp4, pp5)
        c2 = calcCarry(pp3, pp4, pp5)
        s3 = calcSave(s1, c1, pp7)
        c3 = calcCarry(s1, c1, pp7)
        s4 = calcSave(s2, c2, pp6)
        c4 = calcCarry(s2, c2, pp6)
        s5 = calcSave(s3, c3, c4)
        c5 = calcCarry(s3, c3, c4)
        s6 = calcSave(s5, c5, s4)
        c6 = calcCarry(s5, c5, s4)
        finalP8 = calcParallel(s6, c6)

        for list in [pp0, pp1, pp2, pp3, pp4, pp5, pp6, pp7, s1, c1, s2, c2, s3, c3, s4, c4, s5, c5, s6, c6, finalP8]:  # removes leading zeros on all binary values
            if list.count('1') != 0:
                while list[0] == "0":
                    list.pop(0)
            else:
                while len(list) > 1:  # puts just a single zero for all zero values
                    list.pop(0)

        pp0str = ""
        pp1str = ""
        pp2str = ""
        c1str = ""
        s1str = ""
        pp3str = ""
        pp4str = ""
        pp5str = ""
        c2str = ""
        s2str = ""
        pp7str = ""
        c3str = ""
        s3str = ""
        pp6str = ""
        c4str = ""
        s4str = ""
        c5str = ""
        s5str = ""
        c6str = ""
        s6str = ""
        finalP8str = ""
        pp0Val8.set(pp0str.join(pp0))
        canvas8x8.itemconfig(pp0Label8, text=" PP0 " + "(" + pp0Val8.get() + ")")
        pp1Val8.set(pp1str.join(pp1))
        canvas8x8.itemconfig(pp1Label8, text=" PP1 " + "(" + pp1Val8.get() + ")")
        pp2Val8.set(pp2str.join(pp2))
        canvas8x8.itemconfig(pp2Label8, text=" PP2 " + "(" + pp2Val8.get() + ")")
        c1Val8.set(c1str.join(c1))
        canvas8x8.itemconfig(c1Label8, text=" C1 " + "(" + c1Val8.get() + ")")
        s1Val8.set(s1str.join(s1))
        canvas8x8.itemconfig(s1Label8, text=" S1 " + "(" + s1Val8.get() + ")")
        pp3Val8.set(pp3str.join(pp3))
        canvas8x8.itemconfig(pp3Label8, text=" PP3 " + "(" + pp3Val8.get() + ")")
        pp4Val8.set(pp4str.join(pp4))
        canvas8x8.itemconfig(pp4Label8, text=" PP4 " + "(" + pp4Val8.get() + ")")
        pp5Val8.set(pp5str.join(pp5))
        canvas8x8.itemconfig(pp5Label8, text=" PP5 " + "(" + pp5Val8.get() + ")")
        c2Val8.set(c2str.join(c2))
        canvas8x8.itemconfig(c2Label8, text=" C2 " + "(" + c2Val8.get() + ")")
        s2Val8.set(s2str.join(s2))
        canvas8x8.itemconfig(s2Label8, text=" S2 " + "(" + s2Val8.get() + ")")
        pp7Val8.set(pp7str.join(pp7))
        canvas8x8.itemconfig(pp7Label8, text=" PP7 " + "(" + pp7Val8.get() + ")")
        c3Val8.set(c3str.join(c3))
        canvas8x8.itemconfig(c3Label8, text=" C3 " + "(" + c3Val8.get() + ")")
        s3Val8.set(s3str.join(s3))
        canvas8x8.itemconfig(s3Label8, text=" S3 " + "(" + s3Val8.get() + ")")
        pp6Val8.set(pp6str.join(pp6))
        canvas8x8.itemconfig(pp6Label8, text=" PP6 " + "(" + pp6Val8.get() + ")")
        c4Val8.set(c4str.join(c4))
        canvas8x8.itemconfig(c4Label8, text=" C4 " + "(" + c4Val8.get() + ")")
        s4Val8.set(s4str.join(s4))
        canvas8x8.itemconfig(s4Label8, text=" S4 " + "(" + s4Val8.get() + ")")
        c5Val8.set(c5str.join(c5))
        canvas8x8.itemconfig(c5Label8, text=" C5 " + "(" + c5Val8.get() + ")")
        s5Val8.set(s5str.join(s5))
        canvas8x8.itemconfig(s5Label8, text=" S5 " + "(" + s5Val8.get() + ")")
        c6Val8.set(c6str.join(c6))
        canvas8x8.itemconfig(c6Label8, text=" C6 " + "(" + c6Val8.get() + ")")
        s6Val8.set(s6str.join(s6))
        canvas8x8.itemconfig(s6Label8, text=" S6 " + "(" + s6Val8.get() + ")")
        finalP8x8Val.set(finalP8str.join(finalP8))
        canvas8x8.itemconfig(finalP8x8Label, text="Final Product " + "(" + finalP8x8Val.get() + ")")

        root.update_idletasks()


#______________________________________________________________________________________________________
# Calculate Button

calcLabelFrame = LabelFrame(controlsFrame, text="Click button to calculate:", padx=8, pady=12)

calcButton = Button(calcLabelFrame, text="Calculate", width=wtWidth*3, height=3)

calcLabelFrame.grid(row=3, column=0)
calcButton.grid(row=0, column=0)

calcButton.bind(sequence='<Button-1>', func=calcLogic)


#______________________________________________________________________________________________________


root.mainloop()
