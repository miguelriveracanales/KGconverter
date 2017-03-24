from Tkinter import *


master = Tk()
#master.geometry("400x100")

def kgconv():
    #variables
    indata = e1Value.get()
    grams = 1000
    pound = 2.20462
    ounces = 35.274

    grams = float(grams) * float(indata)
    pound = float(pound) * float(indata)
    ounces = float(ounces) * float(indata)

    e1Out.insert(END,grams)
    e2Out.insert(END,pound)
    e3Out.insert(END,ounces)




#labels
l1title = Label(master,text="Kg")
l1title.grid(row=0,column=0)


#Entrys

#variable
e1Value = StringVar()

e1In = Entry(master,width=20,textvariable=e1Value)
e1In.grid(row=0,column=1)

e1Out = Entry(master,width=20)
e1Out.grid(row=1,column=0)

e2Out = Entry(master,width=20)
e2Out.grid(row=1,column=1)

e3Out = Entry(master,width=20)
e3Out.grid(row=1,column=2)
#Botton
b1Converter = Button(master,text='Convert',command=kgconv)
b1Converter.grid(row=0,column=2)

master.mainloop()
