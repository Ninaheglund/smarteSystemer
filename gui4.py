from tkinter import*
import random
import time
import datetime
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from random import randint
#import serial


root = Tk()
root.geometry("798x447+0+0")
root.title("Godis Maskinen")
#ytterste rammen
Tops = Frame(root, width = 798,height=447,bd=5, relief="raise")
Tops.pack(side=TOP)
lblTitle = Label (Tops, font=('arial', 25, 'bold'), text="Godis Maskinen")
lblTitle.grid(row=0, column=0)
BottomMainFrame = Frame (root, width = 798 , height=422, bd=5, relief="raise")
BottomMainFrame.pack(side=BOTTOM)
#Venstre felt
f1 = Frame (BottomMainFrame, width = 266, height=50, bd=5, relief="raise")
f1.pack(side=LEFT)
#Midterste felt
f2 = Frame (BottomMainFrame, width = 266, height=65, bd=5, relief="raise")
f2.pack(side=LEFT)
#Midterste/øverste felt
f2TOP = Frame (f2, width = 45, height=50, bd=5, relief="raise")
f2TOP.pack(side=TOP)
#Midterste/nederste felt
f2BOTTOM = Frame (f2, width = 45, height=30, bd=5, relief="raise")
f2BOTTOM.pack(side=BOTTOM)
#Høyre felt
f3 = Frame (BottomMainFrame, width = 266, height=65, bd=5, relief="raise")
f3.pack(side=RIGHT)
f3BOTTOM = Frame(f3, width = 45, height=20, bd=5, relief="raise")
f3BOTTOM.pack(side=BOTTOM)

varMF=IntVar() #brukt meget fornøyd
varHF=IntVar() #brukt halvveis fornøyd
varLF=IntVar() #brukt Lite fornøyd
varF=IntVar() #brukt Første gang
varBS=IntVar() #brukt Bringebærsjokkis
varMK=IntVar() #brukt Maiskule
varCN=IntVar() #brukt Chilinøtter
varBM=IntVar() #brukt BM
varTotal=StringVar()
#varReset=IntVar()
varChk=IntVar() #checkbutton

varMF.set(0) #brukt
varHF.set(0) #brukt
varLF.set(0) #brukt
varF.set(0) #brukt
varBS.set(0) #brukt
varMK.set(0) #brukt
varCN.set(0) #brukt
varBM=IntVar(0) #brukt
varTotal.set("0")
#varReset.set("0")
varChk.set("0") #checkbutton
#Calculations
bs = int()
mk = int()
cn = int()
bm = int()

#vekt
bs = 2
mk=10
cn=5

#txtBringebarsjokkis.configure(state =DISABLED)
#txtMaisKule.configure(state = DISABLED)
#txtChiliNøtter.configure(state = DISABLED)
#txtTotal.configure(state = DISABLED)
lblOnsketPris = Label (f2BOTTOM, font=('arial', 15, 'bold'), text="Ønsket pris:\t\n")
lblOnsketPris.grid(row=0,column=0)

#kr space(total)
def reset():
    varMF.set(0) #brukt
    varHF.set(0) #brukt
    varLF.set(0) #brukt
    varF.set(0) #brukt
    varBS.set(0) #brukt
    varMK.set(0) #brukt
    varCN.set(0) #brukt
    varTotal.set("0")
   # varReset.set("0")



#Exit pop up
def iExit():
    exit = messagebox.askyesno("Exit", "Quit system?")
    if exit > 0:
       # print(var4.get())
        root.destroy()
        return


#submit pop up
def submit(varBS, varMK, varCN, varBM, txtTotal):
    total = txtTotal.get()
    total = int(total)
    listOfVariables = list()
    submit=messagebox.askyesno("Not submit", "submit")
    # 1: BS, 2: MK, 3: CK
    if 'yes' and varBS.get() is 0 and submit is True:
        listOfVariables.append(1)
        print("1.Bringebærsjokkis")
    if 'yes' and varMK.get() is 0 and submit is True:
        listOfVariables.append(2)
        print("2.Maiskule")
    if 'yes' and varCN.get() is 0 and submit is True:
        listOfVariables.append(3)
        print("3.Chilikule")
    if 'yes' and varBM.get() is 0 and submit is True:
        listOfVariables.append(4)
        print("4.Bærmiks")

    #sender med 2


    return calculations(listOfVariables, total)

#tar imot 2
def calculations(listOfVariables, tot):

    total = tot
    print('Ønsket pris:', total, 'kr')
    #for i in listOfVariables:
     #   print()

    remaining = total

    totalVariables = len(listOfVariables)
    for x in range(totalVariables):
        if x == totalVariables - 1:
            listOfVariables[x] = remaining
        else:
            listOfVariables[x] = randint(0, remaining)
        remaining = remaining - listOfVariables[x]
        #output (det du får)


    print("Fordeling:", str(listOfVariables))
    length_of_list = listOfVariables.__len__()
    print(length_of_list)
#Printer ut til ønsket pris label

    lblKvitt.configure(text=listOfVariables)
    lblKvitt.update_idletasks()
    return remaining

def chkButton():
    if (varChk.get() ==1):
        varChk.configure(state = NORMAL)
    elif(varChk.get() == 1):
        varChk.configure(state = DISABLED)

def iKvittering():

    return
#==================================================FRAME 1===============================
#Overskrift "Fornøyd sist?" (som vises til venstre)
lblIkkef = Label (f1, font=('arial', 20, 'bold'), text=" Fornøyd sist? ")
lblIkkef.grid(row=0, column=0)

#Meget fornøyd + check button
MegetFornoyd =Checkbutton (f1, text= "Meget fornøyd", variable=varMF, onvalue=1, offvalue=0, font=('arial', 13, 'bold')).grid(row=1, column=0, sticky=W)

#Halvveis fornøyd + check button
HalvveisFornoyd =Checkbutton (f1, text= "Halvveis fornøyd", variable=varHF, onvalue=1, offvalue=0, font=('arial', 13, 'bold')).grid(row=2, column=0, sticky=W)

#Lite fornøyd + check button
LiteFornoyd =Checkbutton (f1, text= "Lite fornøyd", variable=varLF, onvalue=1, offvalue=0, font=('arial', 13, 'bold')).grid(row=3, column=0, sticky=W)

#Første gang + check button
ForsteGang =Checkbutton (f1, text= "Første gang?", variable=varF, onvalue=1, offvalue=0, font=('arial', 13, 'bold')).grid(row=4, column=0, sticky=W)
#==================================================FRAME 2===============================

#Overskrift "Liker ikke:" (som vises til venstre)
lblIkke = Label (f2TOP, font=('arial', 20, 'bold'), text=" Liker ikke:\t    ")
lblIkke.grid(row=0, column=0)

#vare: Bringebær sjokkis + check button
Bringebarsjokkis =Checkbutton (f2TOP, text= "Bringebær sjokkis", variable=varBS, onvalue=1, offvalue=0, font=('arial', 13, 'bold')).grid(row=1, column=0, sticky=W)

#vare: Maiskule + check button
Maiskule =Checkbutton (f2TOP, text= "Maiskule ", variable=varMK, onvalue=1, offvalue=0, font=('arial', 13, 'bold')).grid(row=2, column=0, sticky=W)

#vare: Chilinøtter + check button
Chilinotter =Checkbutton (f2TOP, text= "Chilinøtter ", variable=varCN, onvalue=1, offvalue=0, font=('arial', 13, 'bold')).grid(row=3, column=0, sticky=W)

#vare: Bærmiks + check button
Barmiks =Checkbutton (f2TOP, text= "Bærmiks ", variable=varBM, onvalue=1, offvalue=0, font=('arial', 13, 'bold')).grid(row=4, column=0, sticky=W)

lblspace= Label(f2BOTTOM, text= "\n\n\n\n\n\n\n\n\n\n\n")
lblspace.grid(row=6, column =1)

#=============================================== Frame bottom 2=======================================

#Overskrift "Pris"
lblOnsketPris = Label (f2BOTTOM, font=('arial', 20, 'bold'), text="  Ønsket pris:  \n")
lblOnsketPris.grid(row=0,column=0)


#"KR:"
lblKr =Label(f2BOTTOM, text= "Kr:", font=('arial',15,'bold'))
lblKr.grid(row=2 , column = 0,sticky=W)

#Input sted
txtTotal= Entry(f2BOTTOM,font=('arial',15,'bold'), textvariable = varTotal, widt =6, justify='left', state =NORMAL)
txtTotal.grid(row =2 , column =0)

#space Quickfix
lblspace= Label(f2BOTTOM, text= "\n\n\n")
lblspace.grid(row=3, column =0)

#Kjøp knapp
btnSubmit=Button(f2BOTTOM,padx=16, pady=1, bd=4, fg="black", font=('arial', 12, 'bold'), width=4,
        text="Kjøp", command=lambda: submit(varBS,varMK,varCN,varBM,txtTotal)).grid(row=3, column=0)
#reset knapp
#btnTotal=Button(f2BOTTOM,padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
 #       text="Reset ", command=chkButton).grid(row=6, column=0)

#Exit knapp
btnExit=Button(f2BOTTOM,padx=16, pady=1, bd=4, fg="black", font=('arial', 12, 'bold'), width=4,
        text="Exit ", command=lambda: iExit()).grid(row=3, column=1)

#================================================= Frame 3 ================================

#Kvitterings knapp
btnKvittering=Button(f3BOTTOM, fg="black",bd=1, font=('arial', 20, 'bold'), width=12,
     text="Kvittering", command=lambda: iKvittering()).grid(row=2, column=0)

lblKvitt = Label (f3BOTTOM, font=('arial', 15, 'bold'), text="\t\n")
lblKvitt.grid(row=3,column=0)
#=============================================== Annet ======================================

#ser = serial.Serial('/dev/ttyACM0', 9600)
#while True:
#    ser.write(b"")
#    print(ser.readline())



#print((listOfVariables[0])ms(listOfVariables[1])ck(listOfVariables[2])bm(listOfVariables[3])"
#b"a100 b50 c10 d23"





root. mainloop()

