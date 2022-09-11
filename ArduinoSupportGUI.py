#path='Output Path write'

from ssl import OP_CIPHER_SERVER_PREFERENCE
import tkinter as tk
import tkinter.font
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
bb=0
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
    startbuttonsetwin.geometry("500x8500")

    startbuttonsetframe=tk.Frame(startbuttonsetwin,width=200)
    startbuttonsetframe.pack()

    startbuttonsetlabel=tk.Label(startbuttonsetframe,text="何番ピンのボタン?",font=("Helveica","20"))
    startbuttonsetlabel.pack()
    startbuttonsetentry=tk.Entry(startbuttonsetframe,width=10,font=("Helveica","20"))
    startbuttonsetentry.pack()
    startbuttonsetbutton=tk.Button(startbuttonsetframe,text="設定",font=("Helveica","20"))
    startbuttonsetbutton.bind("<1>",startbuttonsetevent)
    startbuttonsetbutton.bind("<1>",startbuttonsetalert,"+")
    startbuttonsetbutton.pack()

def startbuttonsetalert(event):
    startbuttonsetalertwin=tk.Toplevel()
    startbuttonsetalertwin.geometry("500x500")

    startbuttonsetalertframe=tk.Frame(startbuttonsetalertwin,width=200)
    startbuttonsetalertframe.pack()

    startbuttonsetalertlabel=tk.Label(startbuttonsetalertframe,text="設定できたよ!",font=("Helveica","20"))
    startbuttonsetalertlabel.pack()
    startbuttonsetalertbutton=tk.Button(startbuttonsetalertframe,text="戻る",command=startbuttonsetalertwin.destroy,font=("Helveica","20"))
    startbuttonsetalertbutton.pack()

def motortimewindow():
    global bb
    
    def getnum(event):
        global bb
        global mado
        bb=motorkazu.get()
        mado=outputsetteientry.get()
        if bb.isdecimal() and mado.isdecimal()==True:
            motorparamwin()

        else:
            erroralt()

    motortimewin=tk.Toplevel()
    motortimewin.geometry("500x500")
    motortimewin.title("モーター時間制御")

    countframe=tk.Frame(motortimewin,width=200)
    countframe.pack()

    paramsitei=tk.Label(countframe,text="パラメータ何個?",font=("Helveica","20"))
    paramsitei.pack()
    motorkazu=tk.Entry(countframe,width=10,font=("Helveica","20"))
    motorkazu.pack()

    outputsetteilabel=tk.Label(countframe,text="出力は何個?",font=("Helveica","20"))
    outputsetteilabel.pack()
    outputsetteientry=tk.Entry(countframe,width=10,font=("Helveica","20"))
    outputsetteientry.pack()

    parambutton=tk.Button(countframe,text="次へ",font=("Helveica","20"))
    parambutton.bind("<1>",getnum)
    parambutton.pack()

def motorparamwin():
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
    motorparamwin.geometry("500x500")
    motorparamwin.title("パラメータ設定")

    kariframe=tk.Frame(motorparamwin,width=200)
    kariframe.pack()

    del entrys[:]
    del entrys_b[:]

    for out in range(int(mado)):
        pinlabel=tk.Label(kariframe,text=str(out+1)+"つめの出力は何番ピン?",font=("Helveica","20"))
        pinlabel.pack()
        pininput=tk.Entry(kariframe,width=10,font=("Helveica","20"))
        pininput.pack()
        entrys_b.append(pininput)

    for timeinput in range(int(bb)):
        timelabel=tk.Label(kariframe,text="パラメータ"+str(paramnum),font=("Helveica","20"))
        timelabel.pack()
        timeinput=tk.Entry(kariframe,width=10,font=("Helveica","20"))
        timeinput.pack()
        entrys.append(timeinput)
        paramnum += 1

    outbutton=tk.Button(kariframe,text="出力",font=("Helveica","20"))
    outbutton.bind("<1>",getparam)
    outbutton.bind("<1>",printf,"+")
    outbutton.pack()

def iobutton():
    def getparam(event):
        global bb
        global mado
        bb=iobuttonentry.get()
        mado=iobuttonoutputentry.get()

        if bb.isdecimal() and mado.isdecimal()==True:
            ioset()

        else:
            erroralt()

    iobuttonget=tk.Toplevel()
    iobuttonget.geometry("500x500")
    iobuttonget.title("ボタン数")

    iobuttonframe=tk.Frame(iobuttonget,width=200)
    iobuttonframe.pack()

    iobuttonlabel=tk.Label(iobuttonframe,text="ボタン数は?",font=("Helveica","20"))
    iobuttonlabel.pack()
    iobuttonentry=tk.Entry(iobuttonframe,width=10,font=("Helveica","20"))
    iobuttonentry.pack()

    iobuttonoutputlabel=tk.Label(iobuttonframe,text="ボタン1個あたりの出力の数は?",font=("Helveica","20"))
    iobuttonoutputlabel.pack()
    iobuttonoutputentry=tk.Entry(iobuttonframe,width=10,font=("Helveica","20"))
    iobuttonoutputentry.insert(tk.END,"1")
    iobuttonoutputentry.pack()

    iosetbutton=tk.Button(iobuttonframe,text="次へ",width=10,font=("Helveica","20"))
    iosetbutton.bind("<1>",getparam)
    iosetbutton.pack()

def ioset():
    global bb
    global mado

    def getparam(event):
        outputstak=[]
        hlstak=[]
        global counter

        for kari in range(int(bb)):
            for i in range(int(mado)):
                outputstak.append(entrys_b[counter].get())
                hlstak.append(combos[counter].get())
                counter += 1

            loopprg.append("if(digitalRead("+entrys[kari].get()+")==LOW){")

            for h in range(int(mado)):
                syutu=hlstak[h]
                if syutu.isdecimal():
                    loopprg.append("analogWrite("+outputstak[h]+","+syutu+");")

                else:
                    loopprg.append("digitalWrite("+outputstak[h]+","+hlstak[h]+");")

            loopprg.append("delay("+entrys_c[kari].get()+");")
            loopprg.append("}")
            loopprg.append("else if(digitalRead("+entrys[kari].get()+")==HIGH){")

            for g in range(int(mado)):
                if hlstak[g]=="LOW":
                    loopprg.append("digitalWrite("+outputstak[g]+",HIGH);")
                elif hlstak[g]=="HIGH" or hlstak[g].isdecimal():
                    loopprg.append("digitalWrite("+outputstak[g]+",LOW);")
            
            loopprg.append("}")

            inpin.append(entrys[kari].get())
            for f in outputstak:
                outpin.append(f)

            del outputstak[:]
            del hlstak[:]
        
        loopprg.append("}")

        printf()

    iosetup=tk.Toplevel()
    iosetup.geometry("500x500")
    iosetup.title("設定画面")

    iosetupframe=ttk.Frame(iosetup,width=200)
    iosetupframe.pack()

    del entrys[:]
    del entrys_b[:]
    del entrys_c[:]

    for buttoninput in range(int(bb)):
        buttonsetlabel=ttk.Label(iosetupframe,text="ボタンのピンは?",font=("Helveica","20"))
        buttonsetlabel.pack()
        buttonsetentry=ttk.Entry(iosetupframe,width=10,font=("Helveica","20"))
        buttonsetentry.pack()
        entrys.append(buttonsetentry)
        
        for buttonoutput in range(int(mado)):

            buttonoutlabel=ttk.Label(iosetupframe,text=str(buttonoutput+1)+"つめの対応する出力は?",font=("Helveica","20"))
            buttonoutlabel.pack()
            buttonoutentry=ttk.Entry(iosetupframe,width=10,font=("Helveica","20"))
            buttonoutentry.pack()
            entrys_b.append(buttonoutentry)

            v=tk.StringVar()
            keepv=v.get()

            buttonhllabel=ttk.Label(iosetupframe,text="押したときの出力は?",font=("Helveica","20"))
            buttonhllabel.pack()
            buttonhlcombo=ttk.Combobox(iosetupframe,textvariable=keepv,values=hl,width=10,font=("Helveica","20"))
            buttonhlcombo.set(hl[0])
            buttonhlcombo.pack()
            combos.append(buttonhlcombo)

        buttondelaylabel=ttk.Label(iosetupframe,text="稼働時間は?",font=("Helveica","20"))
        buttondelaylabel.pack()
        buttondelayentry=ttk.Entry(iosetupframe,width=10,font=("Helveica","20"))
        buttondelayentry.insert(tk.END,"0")
        buttondelayentry.pack()
        entrys_c.append(buttondelayentry)

    finishbutton=tk.Button(iosetupframe,text="出力",width=10,font=("Helveica","20"))
    finishbutton.bind("<1>",getparam)
    finishbutton.pack()

def lchikasta():

    def ledcount(evemt):
        global bb
        bb=lchikastaentry.get()
        if bb.isdecimal():
            lchikamain()

        else:
            erroralt()

    lchikastatopwin=tk.Toplevel()
    lchikastatopwin.geometry("500x500")
    lchikastatopwin.title("LEDの数")

    lchikastaframe=tk.Frame(lchikastatopwin,width=200)
    lchikastaframe.pack()
    lchikastalabel=tk.Label(lchikastaframe,text="LEDの数は?",font=("Helveica","20"))
    lchikastalabel.pack()
    lchikastaentry=tk.Entry(lchikastaframe,width=10,font=("Helveica","20"))
    lchikastaentry.pack()
    lchikastanextbutton=tk.Button(lchikastaframe,text="次へ",width=10,font=("Helveica","20"))
    lchikastanextbutton.bind("<1>",ledcount)
    lchikastanextbutton.pack()

def lchikamain():
    def lchikaprg(event):
        delaytime=dutytimeentry.get()

        if delaytime.isdecimal():
            for onchika in entrys:
                pinon=onchika.get()
                loopprg.append("digitalWrite("+pinon+",HIGH);")
                outpin.append(pinon)

            loopprg.append("delay("+delaytime+");")

            for offchika in entrys:
                pinoff=offchika.get()
                loopprg.append("digitalWrite("+pinoff+",LOW);")
        
            loopprg.append("delay("+delaytime+");}")

            printf()

        else:
            erroralt()

    global bb

    lchikamainwin=tk.Toplevel()
    lchikamainwin.geometry("500x500")
    lchikamainwin.title("パラメータ設定")

    lchikamainframe=tk.Frame(lchikamainwin,width=200)
    lchikamainframe.pack()

    for lchikaparam in range(int(bb)):
        setlabel=tk.Label(lchikamainframe,text="LED"+str(lchikaparam+1)+"のピンは?",font=("Helveica","20"))
        setlabel.pack()
        ledsetentry=tk.Entry(lchikamainframe,width=10,font=("Helveica","20"))
        ledsetentry.pack()
        entrys.append(ledsetentry)

    dutytimelabel=tk.Label(lchikamainframe,text="ON/OFF時間は?",font=("Helveica","20"))
    dutytimelabel.pack()
    dutytimeentry=tk.Entry(lchikamainframe,width=10,font=("Helveica","20"))
    dutytimeentry.insert(tk.END,"500")
    dutytimeentry.pack()

    lchikaendbutton=tk.Button(lchikamainframe,text="出力",font=("Helveica","20"))
    lchikaendbutton.bind("<1>",lchikaprg)
    lchikaendbutton.pack()


def printf():
    global bb
    global casefrag
    global counter

    bb=0
    counter=0

    #code=open(path,'w')

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
        #code.write(hed+'\n')

    for set in setprg:
        print(set)
        #code.write(set+'\n')

    print()

    for alloutput in loopprg:
        print(alloutput)
        #code.write(alloutput+'\n')

    del inpin[:]
    del outpin[:]
    del hedprg[:]
    del setprg[:]
    del loopprg[:]

    setprg.append("void setup(){")
    loopprg.append("void loop(){")

    finishwin=tk.Toplevel()
    finishwin.geometry("500x500")

    finishframe=tk.Frame(finishwin,width=200)
    finishframe.pack()

    finishlabel=tk.Label(finishframe,text="出力完了!",font=("Helveica","20"))
    finishlabel.pack()

    finishbutton=tk.Button(finishframe,text="つづける",width=10,command=finishwin.destroy,font=("Helveica","20"))
    finishbutton.pack()

    endbutton=tk.Button(finishframe,text="おわる",width=10,command=root.destroy,font=("Helveica","20"))
    endbutton.pack()

def erroralt():
    errorwin=tk.Toplevel()
    errorwin.geometry("500x500")

    errorframe=tk.Frame(errorwin,width=200)
    errorframe.pack()

    errormsg=tk.Label(errorframe,text="入力ミスがあります",font=("Helveica","20"))
    errormsg.pack()

root=tk.Tk()
root.title("メインページ")
root.geometry("500x500")

waku=tk.Frame(root)
waku.pack()

startbuttonbutton=tk.Button(waku,text="スタートボタン",command=startbuttonset,font=("Helveica","50"))
startbuttonbutton.pack()
motortimebutton=tk.Button(waku,text="時間制御",command=motortimewindow,font=("Helveica","50"))
motortimebutton.pack()

ioctrlbutton=tk.Button(waku,text="ボタンI/O",command=iobutton,font=("Helveica","50"))
ioctrlbutton.pack()

lchikabutton=tk.Button(waku,text="Lチカ",command=lchikasta,font=("Helveica","50"))
lchikabutton.pack()

root.mainloop()
