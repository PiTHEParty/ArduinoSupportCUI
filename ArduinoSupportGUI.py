#path='C:/Users/asaas/desktop/KASS.ino'r

from ssl import OP_CIPHER_SERVER_PREFERENCE
import tkinter as tk
from tkinter import *
from tkinter import ttk
import time

hedprg=[]
setprg=['void setup(){']
loopprg=['void loop(){']
entrys=[]
entrys_b=[]
entrys_c=[]
combos=[]
inpin=[]
outpin=[]
buttonpin=[]

hl=["HIGH","LOW","PWM"]

dsfrag=0
casefrag=0
kass=0
mado=0
counter=0
paramnum=1

def startbuttonset():

    def startbuttonsetevent(event):
        global casefrag
        
        stbt=startbuttonsetentry.get()
        hedprg.append("int frag=0;")
        inpin.append(stbt)
        loopprg.append("switch(frag){")
        loopprg.append("case 0:")
        loopprg.append("if(digitalRead("+stbt+")==LOW){")
        loopprg.append("frag=1;}")
        loopprg.append("break;")
        loopprg.append("case 1:")
        casefrag=1

    startbuttonsetwin=tk.Toplevel()
    startbuttonsetwin.geometry("200x200")

    startbuttonsetframe=tk.Frame(startbuttonsetwin,width=200)
    startbuttonsetframe.pack()

    startbuttonsetlabel=tk.Label(startbuttonsetframe,text="何番ピンのボタン?")
    startbuttonsetlabel.pack()
    startbuttonsetentry=tk.Entry(startbuttonsetframe,width=10)
    startbuttonsetentry.pack()
    startbuttonsetbutton=tk.Button(startbuttonsetframe,text="設定")
    startbuttonsetbutton.bind("<1>",startbuttonsetevent)
    startbuttonsetbutton.bind("<1>",startbuttonsetalert,"+")
    startbuttonsetbutton.pack()

def startbuttonsetalert(event):
    startbuttonsetalertwin=tk.Toplevel()
    startbuttonsetalertwin.geometry("200x100")

    startbuttonsetalertframe=tk.Frame(startbuttonsetalertwin,width=200)
    startbuttonsetalertframe.pack()

    startbuttonsetalertlabel=tk.Label(startbuttonsetalertframe,text="設定できたよ!")
    startbuttonsetalertlabel.pack()
    startbuttonsetalertbutton=tk.Button(startbuttonsetalertframe,text="戻る",command=startbuttonsetalertwin.destroy)
    startbuttonsetalertbutton.pack()

def motortimewindow():
    global kass
    
    def getnum(event):
        global kass
        global mado
        kass=motorkazu.get()
        mado=outputsetteientry.get()

    motortimewin=tk.Toplevel()
    motortimewin.geometry("200x100")
    motortimewin.title("モーター時間制御")

    countframe=tk.Frame(motortimewin,width=200)
    countframe.pack()

    paramsitei=tk.Label(countframe,text="パラメータ何個?")
    paramsitei.pack()
    motorkazu=tk.Entry(countframe,width=10)
    motorkazu.pack()

    outputsetteilabel=tk.Label(countframe,text="how many?")
    outputsetteilabel.pack()
    outputsetteientry=tk.Entry(countframe,width=10)
    outputsetteientry.pack()

    parambutton=tk.Button(countframe,text="次へ")
    parambutton.bind("<1>",getnum)
    parambutton.bind("<1>",motorparamwin,"+")
    parambutton.pack()

def motorparamwin(event):
    global paramnum

    def getparam(event):
        outpinstack=[]
        global mado

        for i in range(int(mado)):
            pinpos=entrys_b[i].get()
            outpinstack.append(pinpos)

        for paramout in entrys:
            for j in outpinstack:
                loopprg.append("digitalWrite("+j+",HIGH);")
            loopprg.append("delay("+paramout.get()+");")

            for k in outpinstack:
                loopprg.append("digitalWrite("+k+",LOW);")
            loopprg.append("delay(500);")

        loopprg.append("}")

    motorparamwin=tk.Toplevel()
    motorparamwin.geometry("200x400")
    motorparamwin.title("パラメータ設定")

    kariframe=tk.Frame(motorparamwin,width=200)
    kariframe.pack()

    del entrys[:]
    del entrys_b[:]

    for out in range(int(mado)):
        pinlabel=tk.Label(kariframe,text=str(out+1)+"何番ピン?")
        pinlabel.pack()
        pininput=tk.Entry(kariframe,width=10)
        pininput.pack()
        entrys_b.append(pininput)

    for timeinput in range(int(kass)):
        timelabel=tk.Label(kariframe,text="パラメータ"+str(paramnum))
        timelabel.pack()
        timeinput=tk.Entry(kariframe,width=10)
        timeinput.pack()
        entrys.append(timeinput)
        paramnum += 1

    outbutton=tk.Button(kariframe,text="出力",width=10)
    outbutton.bind("<1>",getparam)
    outbutton.bind("<1>",printf,"+")
    outbutton.pack()

def iobutton():
    def getparam(event):
        global kass
        global mado
        kass=iobuttonentry.get()
        mado=iobuttonoutputentry.get()

    iobuttonget=tk.Toplevel()
    iobuttonget.geometry("200x100")
    iobuttonget.title("ボタン数")

    iobuttonframe=tk.Frame(iobuttonget,width=200)
    iobuttonframe.pack()

    iobuttonlabel=tk.Label(iobuttonframe,text="ボタン数は?")
    iobuttonlabel.pack()
    iobuttonentry=tk.Entry(iobuttonframe,width=10)
    iobuttonentry.pack()

    iobuttonoutputlabel=tk.Label(iobuttonframe,text="ボタン1個あたりの出力の数は?")
    iobuttonoutputlabel.pack()
    iobuttonoutputentry=tk.Entry(iobuttonframe,width=10)
    iobuttonoutputentry.insert(tk.END,"1")
    iobuttonoutputentry.pack()

    iosetbutton=tk.Button(iobuttonframe,text="次へ",width=10)
    iosetbutton.bind("<1>",getparam)
    iosetbutton.bind("<1>",ioset,"+")
    iosetbutton.pack()

def ioset(event):
    global kass
    global mado

    def getparam(event):
        outputstak=[]
        hlstak=[]
        global counter

        for kari in range(int(kass)):
            for i in range(int(mado)):
                outputstak.append(entrys_b[counter].get())
                hlstak.append(combos[counter].get())
                counter += 1

            loopprg.append("if(digitalRead("+entrys[kari].get()+")==LOW){")

            for h in range(int(mado)):
                loopprg.append("digitalWrite("+outputstak[h]+","+hlstak[h]+");")

            loopprg.append("delay("+entrys_c[kari].get()+");")
            loopprg.append("}")
            loopprg.append("else if(digitalRead("+entrys[kari].get()+")==HIGH){")

            for g in range(int(mado)):
                if hlstak[g]=="LOW":
                    loopprg.append("digitalWrite("+outputstak[g]+",HIGH);")
                else:
                    loopprg.append("digitalWrite("+outputstak[g]+",LOW);")
            
            loopprg.append("}")

            inpin.append(entrys[kari].get())
            for f in outputstak:
                outpin.append(f)

            del outputstak[:]
            del hlstak[:]
        
        loopprg.append("}")

    iosetup=tk.Toplevel()
    iosetup.geometry("200x400")
    iosetup.title("設定画面")

    iosetupframe=ttk.Frame(iosetup,width=200)
    iosetupframe.pack()

    del entrys[:]
    del entrys_b[:]
    del entrys_c[:]

    for buttoninput in range(int(kass)):
        buttonsetlabel=ttk.Label(iosetupframe,text="ボタンのピンは?")
        buttonsetlabel.pack()
        buttonsetentry=ttk.Entry(iosetupframe,width=10)
        buttonsetentry.pack()
        entrys.append(buttonsetentry)
        
        for buttonoutput in range(int(mado)):

            buttonoutlabel=ttk.Label(iosetupframe,text=str(buttonoutput+1)+"つめの対応する出力は?")
            buttonoutlabel.pack()
            buttonoutentry=ttk.Entry(iosetupframe,width=10)
            buttonoutentry.pack()
            entrys_b.append(buttonoutentry)

            v=tk.StringVar()
            keepv=v.get()

            buttonhllabel=ttk.Label(iosetupframe,text="H/L")
            buttonhllabel.pack()
            buttonhlcombo=ttk.Combobox(iosetupframe,textvariable=keepv,values=hl,width=10)
            buttonhlcombo.set(hl[0])
            buttonhlcombo.pack()
            combos.append(buttonhlcombo)

        buttondelaylabel=ttk.Label(iosetupframe,text="稼働時間は?")
        buttondelaylabel.pack()
        buttondelayentry=ttk.Entry(iosetupframe,width=10)
        buttondelayentry.insert(tk.END,"0")
        buttondelayentry.pack()
        entrys_c.append(buttondelayentry)

    finishbutton=tk.Button(iosetupframe,text="出力",width=10)
    finishbutton.bind("<1>",getparam)
    finishbutton.bind("<1>",printf,"+")
    finishbutton.pack()

def lchikasta():
    global kass
    global mado

    def ledcount(evemt):
        global kass
        global mado
        kass=lchikastaentry.get()

    lchikastatopwin=tk.Toplevel()
    lchikastatopwin.geometry("200x100")
    lchikastatopwin.title("LEDの数")

    lchikastaframe=tk.Frame(lchikastatopwin,width=200)
    lchikastaframe.pack()
    lchikastalabel=tk.Label(lchikastaframe,text="LEDの数は?")
    lchikastalabel.pack()
    lchikastaentry=tk.Entry(lchikastaframe,width=10)
    lchikastaentry.pack()
    lchikastanextbutton=tk.Button(lchikastaframe,text="次へ",width=10)
    lchikastanextbutton.bind("<1>",ledcount)
    lchikastanextbutton.bind("<1>",lchikamain,"+")
    lchikastanextbutton.pack()

def lchikamain(event):
    def lchikaprg(event):
        delaytime=dutytimeentry.get()

        for onchika in entrys:
            pinon=onchika.get()
            loopprg.append("digitalWrite("+pinon+",HIGH);")
            outpin.append(pinon)

        loopprg.append("delay("+delaytime+");")

        for offchika in entrys:
            pinoff=offchika.get()
            loopprg.append("digitalWrite("+pinoff+",LOW);")
        
        loopprg.append("delay("+delaytime+");}")

    global kass

    lchikamainwin=tk.Toplevel()
    lchikamainwin.geometry("200x300")
    lchikamainwin.title("パラメータ設定")

    lchikamainframe=tk.Frame(lchikamainwin,width=200)
    lchikamainframe.pack()

    for lchikaparam in range(int(kass)):
        setlabel=tk.Label(lchikamainframe,text="LED"+str(lchikaparam+1)+"のピンは?")
        setlabel.pack()
        ledsetentry=tk.Entry(lchikamainframe,width=10)
        ledsetentry.pack()
        entrys.append(ledsetentry)

    dutytimelabel=tk.Label(lchikamainframe,text="ON/OFF時間は?")
    dutytimelabel.pack()
    dutytimeentry=tk.Entry(lchikamainframe,width=10)
    dutytimeentry.insert(tk.END,"500")
    dutytimeentry.pack()

    lchikaendbutton=tk.Button(lchikamainframe,text="出力")
    lchikaendbutton.bind("<1>",lchikaprg)
    lchikaendbutton.bind("<1>",printf,"+")
    lchikaendbutton.pack()


def printf(event):
    global kass
    global casefrag
    global counter

    kass=0
    counter=0

    if casefrag!=0:
        del loopprg[-1]
        loopprg.append("frag=0;")
        loopprg.append("break;")
        loopprg.append("}}")
        casefrag=0

    for inpinset in inpin:    
        setprg.append("pinMode("+str(inpinset)+",INPUT);")

    for outpinset in outpin:
        setprg.append("pinMode("+str(outpinset)+",OUTPUT);")

    setprg.append("}")

    for hed in hedprg:
        print(hed)

    for set in setprg:
        print(set)

    print()

    for alloutput in loopprg:
        print(alloutput)

    del inpin[:]
    del outpin[:]
    del hedprg[:]
    del setprg[:]
    del loopprg[:]

    setprg.append("void setup(){")
    loopprg.append("void loop(){")

    finishwin=tk.Toplevel()
    finishwin.geometry("200x100")

    finishframe=tk.Frame(finishwin,width=200)
    finishframe.pack()

    finishlabel=tk.Label(finishframe,text="出力完了!")
    finishlabel.pack()

    finishbutton=tk.Button(finishframe,text="つづける",width=10,command=finishwin.destroy)
    finishbutton.pack()

    endbutton=tk.Button(finishframe,text="おわる",width=10,command=root.destroy)
    endbutton.pack()

root=tk.Tk()
root.title("メインページ")
root.geometry("500x400")

waku=tk.Frame(root)
waku.pack()

startbuttonbutton=tk.Button(waku,text="スタートボタン",command=startbuttonset)
startbuttonbutton.pack()
motortimebutton=tk.Button(waku,text="時間制御",command=motortimewindow)
motortimebutton.pack()

ioctrlbutton=tk.Button(waku,text="ボタンI/O",command=iobutton)
ioctrlbutton.pack()

lchikabutton=tk.Button(waku,text="Lチカ",command=lchikasta)
lchikabutton.pack()

root.mainloop()

print("Enterを押して終了")
finish=input()