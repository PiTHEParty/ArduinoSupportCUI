#path='Please write Path'

hed=['#include<Servo.h>']
setprg=['void setup(){','Serial.begin(9600);']
loopprg=['void loop(){']
paramlist=[]
outpinlist=[]
BB=0
iffrag=0
elsefrag=0
elseiffrag=0

def hedderset(hedtype):

    if hedtype=='01':
        print('int型')
        print('何を指定する?')
        intname=input()
        hed.append('int '+intname+';')

    if hedtype=='03':
        print('サーボ設定')
        print('サーボの名前は?')
        servoname=input()
        hed.append('Servo '+servoname+';')

def setset(setmode):
    if setmode=='01':
        print('ピンI/O設定')

        while BB<401:
            print('どのピンを設定しますか?')
            setpin=input()

            if setpin=='99':
                break

            print('INPUT or OUTPUT?')
            inout=input()

            if inout=='IN':
                print('設定完了')
                setprg.append('pinMode('+setpin+',INPUT);')

            if inout=='OUT':
                print('設定完了')
                setprg.append('pinMode('+setpin+',OUTPUT);')
                
    if setmode=='03':
        print('サーボセットアップ')

        while BB<401:
            print('サーボの名前は?')
            setservoname=input()

            if setservoname=='99':
                break

            print('サーボつなぐピンは?')
            setservopin=input()

            setprg.append(setservoname+'.attach('+setservopin+');')

def loopset(loopmode):
    if loopmode=='01':
        print('HIGH設定モード')
        while BB<401:
            print('どのピン?')
            ledpin=input()
            if ledpin=='99':
                break

            loopprg.append('digitalWrite('+ledpin+',HIGH);')
            outpinlist.append(ledpin)
            print('設定できたよ!')

    if loopmode=='02':
        print('Lチカモード')

        while BB<401:
            print('どのピンのLED?')
            lchikapin=input()

            if lchikapin=='99':
                break

            print('on時間は?')
            lchikaon=input()
            print('off時間は?')
            lchikaoff=input()

            loopprg.append('digitalWrite('+lchikapin+',HIGH);')
            loopprg.append('delay('+lchikaon+');')
            loopprg.append('digitalWrite('+lchikapin+',LOW);')
            loopprg.append('delay('+lchikaoff+');')

    if loopmode=='03':
        print('サーボ角度指定')
                
        while BB<401:
            print('どのサーボ?')
            loopservoname=input()
                    
            if loopservoname=='99':
                break

            print('指定角度は?')
            angle=input()

            loopprg.append(loopservoname+'.write('+angle+');')

    if loopmode=='04':
        print('delay単発')
        print('delay時間は?')
        delaytime=input()
        if delaytime.isdecimal:
            loopprg.append('delay('+delaytime+');')
        else:
            print("input error!")

    if loopmode=='05':
        print('if文アタマ')
        print('条件は?')
        conditions=input()
        loopprg.append('if('+conditions+'){')
        iffrag += 1

    if loopmode=='06':
        print('else文')
        loopprg.append('else{')
        elsefrag += 1

    if loopmode=='07':
        print('else if文アタマ')
        elseiffrag +=1
        loopprg.append('else if(){')

    if loopmode=='08':
        print('if閉じカッコ(})')
        loopprg.append('}')
        iffrag -= 1

    if loopmode=='09':
        print('else閉じカッコ')
        loopprg.append('}')
        elsefrag -= 1

    if loopmode=='10':
        print('else if閉じカッコ')
        loopprg.append('}')
        elseiffrag -= 1

    if loopmode=='11':
        print('checksum')
        print('何秒?(ms)')
        checktime=input()
        print('処理は?')
        num=input()
        print('見る条件は?')
        stopsum=input()
        loopmode=stopsum
        print('for(int i;int<='+checktime+';i++){')
        print(stopsum)
        print(num)
        print('delay(1)')
        print('}')

    if loopmode=='12':
        print('switch case')
        print('case何個用意する?')
        casecount=int(input())
        for caseprg in range(casecount):
            loopprg.append('case '+str(caseprg)+':')
            while BB<999:
                print('次のcaseを入力するには99を押してね!')
                print('case '+str(caseprg)+'のプログラムは?')
                caseprgset=input()
                if caseprgset=='99':
                    break
                loopmode=caseprgset
                loopset(loopmode)

    if loopmode=='13':
        print('スタートボタン')
        print('何番ピン?')
        start=input()
        print('ボタンのピンは?')
        motor=input()
        loopprg.append('while(digitalRead('+start+')==LOW){')
        loopprg.append('digitalWrite('+motor+',LOW);')
        loopprg.append('}')

    if loopmode=='81':
        print('最後の行削除')
        del loopprg[-1]

    if loopmode=='85':
        print('指定行削除')
        print('どこ消す?')
        deletenum=input()

        del loopprg[-int(deletenum)]

def preset(presetmode):
    if presetmode=='01':
        print('Lチカセット')

    if presetmode=='02':
        timelist=['int timelist[]={']
        delaylist=['int delaylist[]={']
        print('時間制御セット')
        hed.append('int i;')
        print('何パターン用意する?')
        pattern=int(input())
        print('出力は何番ピン?')
        pin=input()
        for patternnum in range(pattern):
            print(str(patternnum+1)+'こめのパラメータだよ!')
            print('何秒回す?')
            param=input()
            timelist.append(param+',')
            print('何秒止める?')
            dt=input()
            delaylist.append(dt+',') 
        timelist.append('};')
        delaylist.append('};')
        
        for ape in timelist:
            hed.append(ape)

        for epa in delaylist:
            hed.append(epa)

        loopprg.append('for(i=0;i<=sizeof(timelist)/sizeof(int);i++){')
        loopprg.append('digitalWrite('+pin+',HIGH);')
        loopprg.append('delay(timelist[i]);')
        loopprg.append('digitalWrite('+pin+',LOW);')
        loopprg.append('delay(delayist[i]);')
        loopprg.append('}')
    
    if presetmode=='03':
        btpinlist=[]
        counter=1
        hed.append('int frag=0;')
        loopprg.append('switch(frag){')
        print('ボタンで処理変えるアレ')
        print('ボタン何個?')
        buttoncount=int(input())
        
        for buttonsyori in range(buttoncount):
            print(str(buttonsyori+1)+'つめのボタンのピンは?')
            changebuttonpin=input()
            btpinlist.append(changebuttonpin)

        loopprg.append('case 0:')

        for standby in btpinlist:
            loopprg.append('if(digitalRead('+standby+')==LOW){')
            loopprg.append('frag='+str(counter)+';')
            loopprg.append('}')
            counter += 1

        loopprg.append('break;')
        counter=1
        
        for changesyori in btpinlist:
            loopprg.append('case '+str(counter)+':')

            while BB<401:
                print('次に進めたいときは99を押してね!')
                print(changesyori+'ピンのボタンを押したときの処理は?')
                loopmode=input()
                if loopmode=='99':
                    break
                loopset(loopmode)
            
            counter += 1
            loopprg.append('frag='+str(buttoncount+1)+';')
            loopprg.append('break;')
        
        loopprg.append('case '+str(buttoncount+1)+':')

        for resetsyori in outpinlist:
            loopprg.append('digitalWrite('+resetsyori+',LOW);')

        loopprg.append('frag=0;')
        loopprg.append('break;')
        loopprg.append('}')

while BB<401:
    for hedhed in hed:
        print(hedhed)

    for hedset in setprg:
        print(hedset)

    print('}')

    for hedloop in loopprg:
        print(hedloop)

    print('}')

    print('メインメニュー')
    mode=input()

    if mode=='00':
        print('ヘッダーとか')
        while BB<401:
            print('ヘッダーに何を入れる?')
            hedtype=input()

            if hedtype=='99':
                break
            
            hedderset(hedtype)

    if mode=='01':
        print('setup内プログラム')

        while BB<401:
            print('何を設定する?')
            setmode=input()

            if setmode=='99':
                break

            setset(setmode)

    if mode=='02':

        print('loop内プログラム')

        while BB<401:

            print(str(iffrag)+str(elsefrag)+str(elseiffrag))

            for menuloop in loopprg:
                print(menuloop)
            
            print('}')

            if iffrag!=0:
                print(str(iffrag)+'こめのif文のプログラムだよ!終わったら閉じてね!!')

            print('どのモードを使う?')
            loopmode=input()

            if loopmode=='99':
                break

            loopset(loopmode)

    if mode=='03':
        print('プリセットモード')
        print('どのモードを使う?')
        presetmode=input()
        preset(presetmode)
    
    if mode=='99':
        break
    
    print(hed)
    print(setprg)
    print(loopprg)

print()

#code=open(path,'w')

for hedoutput in hed:
    #code.write(hedoutput+'\n')
    print(hedoutput)

print()

for setoutput in setprg:
    #code.write(setoutput+'\n')
    print(setoutput)

#code.write('}')
print('}')
print()

for loopoutput in loopprg:
    #code.write(loopoutput+'\n')
    print(loopoutput)

#code.write('}')
print('}')

#code.close()
finish=input('Enterを押して終了')