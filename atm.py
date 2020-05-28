from tkinter import *
from tkinter import ttk
import math
import csv
root=Tk()
draw=0
rem=0
rem1=0
notes=[100,200,500,2000]
patt={}
l={}
total=0
userP={}
userb={}
labelexp1=Label(text="NO USERS AS SUCH EXIXTS",fg="yellow",bg="orange")
labelexp2=Label(text="ATM OUT OF BALANCE",fg="yellow",bg="orange")
def active_all():
    global labelexp1
    global labelexp2
    global labelexp3
    global labelexp5
    buttonw['state']='normal'
    buttonre['state']='normal'
    entryname.delete(0,'end')
    entrypin.delete(0,'end')
    entrym.delete(0,'end')
    labelexp1.configure(text="",bg="white")
    labelexp1.place(x=200,y=300,relx=0.25,rely=0.25)
    buttont.destroy()
def spark1():
    global labelexp1
    global buttont
    global userb
    names=[]
    choice=int(entrym.get())
    c=choice
    name=str(entryname.get().upper()).strip()
    print(name)
    pa=entrypin.get()
    global userb
    global userP
    global total
    #print("password is",pa,userP[name]!=pa,userP[name])
    print(choice)
    print(userb,userP.keys())
    print(userP)
    for i in userP.keys():      
        names.append(i.strip())
    if name not in names:
        print("in")
        labelexp1.config(text="",fg="white",bg="white")
        labelexp1=Label(text="NO USERS AS SUCH EXISTS",fg="yellow",bg="orange")
        labelexp1.place(x=200,y=420,relx=0.25,rely=0.25)
        return
    elif(int(pa)!=int(userP[name])):
        labelexp1.config(text="",fg="white",bg="white")
        labelexp1=Label(text="Wrong Pin",fg="yellow",bg="orange")
        labelexp1.place(x=200,y=420,relx=0.25,rely=0.25)
        return
    global draw
    global l
    global rem
    global rem1
    global patt
    if(userb[name]>0):
        if((choice>total)or(choice>userb[name])):
            print(total)
            labelexp1.config(text="ATM CANT PROVIDE THIS SUM",fg="yellow",bg="orange")
            labelexp1.place(x=200,y=420,relx=0.25,rely=0.25)
        else:
            if(l[2000]!=0):
                rem=math.floor(choice/2000)
                print(rem)
                rem1=total%2000
                if((l[2000]<=rem)and(rem!=0)):
                    patt[2000]=l[2000]
                    l[2000]=0
                    draw=(2000*patt[2000])
                else:
                    patt[2000]=rem
                    draw=(2000*patt[2000])
            print(draw)
            if(choice!=0):
                choice=choice-draw
                rem=math.floor(choice/500)
                rem1=total%500
                print("choice for 500",choice,draw,rem)
                if(l[500]<rem)and(rem!=0):
                    patt[500]=l[500]
                    draw=(500*patt[500])
                    choice=abs(choice-draw)
                    print("choice for 5001",choice,draw)
                elif(l[500]>=rem)and(rem!=0):
                    patt[500]=rem
                    draw=(500*patt[500])
                    choice=abs(choice-draw)
                    print("choice for 5001",choice,draw,rem)
            else:
                patt[500]=0
            if(choice!=0):
                print("choice for 200",choice,draw)
                print("choice is ",choice)
                rem=math.floor(choice/200)
                print("rem is",rem)
                rem1=total%200
                if(l[200]<rem)and(rem!=0):
                    patt[200]=l[200]
                    draw=(200*patt[200])
                    choice=abs(choice-draw)
                if(rem==0):
                    patt[200]=0
                elif(l[200]>=rem)and(rem!=0):
                    patt[200]=rem
                    draw=(200*patt[200])
                    choice=abs(choice-draw)    
            if(choice!=0):
                rem=math.floor(choice/100)
                rem1=total%100
                if(l[100]<rem)and(rem!=0):
                    patt[100]=l[100]
                    draw=(100*patt[100])
                    choice=abs(choice-draw)
                    print("for 100 the ",rem,choice,draw,l[100])
                if(rem==0):
                    patt[100]=0
                elif(l[100]>=rem)and(rem!=0):
                    patt[100]=rem
                    draw=(100*patt[100])
                    choice=abs(choice-draw)
            if(choice!=0):
                print("not possible")
                labelexp1.config(text="Please enter correct amount",fg="yellow",bg="orange")
                labelexp1.place(x=200,y=420,relx=0.25,rely=0.25)
            else:
                print(patt)
                s=""
                for i in patt.keys():

                    s=s+" "+"Number of"+" "+str(i)+"'s"+ " "+"is"+" "+str(patt[i])
                s=s+" "+"balance is"+" "+str(userb[name]-c)
                print(s)
                labelexp1.config(text=s,font="Times 20",fg="black",bg="orange")
                labelexp1.place(x=25,y=420,relx=0.25,rely=0.25)
                buttont=Button(text="Take",font='Times 20',fg='Red',bg='yellow',command=active_all)
                buttont.place(x=100,y=300,relx=0.25,rely=0.25,height=30,width=200)
                buttonw['state']='disable'
                buttonre['state']='disable'
                print(userb)
                userb[name]=userb[name]-c
                for i in patt.keys():
                    l[i]=l[i]-patt[i]
                with open('user.csv','w') as c:
                    fieldnames=['name','pin','balance']
                    writ=csv.DictWriter(c,fieldnames=fieldnames)
                    writ.writeheader()
                    for i in userb.keys():
                        writ.writerow({'name':i,'pin':userP[i],'balance':userb[i]})
                with open('ek.csv','w') as c:
                    fieldnames=['notes','number']
                    writ=csv.DictWriter(c,fieldnames=fieldnames)
                    writ.writeheader()
                    for i in l.keys():
                        writ.writerow({'notes':i,'number':l[i]})

    else:
        labelexp1.config(text="Low Balance",fg="yellow",bg="orange")
        labelexp1.place(x=200,y=420,relx=0.25,rely=0.25)
    l={}
    patt={}
def spark():
    global l,userP,userb,total
    global labelexp2
    l={}
    userP={}
    userb={}
    total=0
    with open('ek.csv','r') as csv_file:
        csv_reader=csv.reader(csv_file)
        for line in csv_reader:
            try:
                if((line[0]!='notes')and(line[1]!='number')):
                    line[0]=int(line[0])
                    l[line[0]]=int(line[1])
            except:
                print("line is empty")
    for i in l.keys():
        total=total+(l[i]*i);
    if(total<100):
        labelexp2.config(text="Low Balance ATM has no money",fg="yellow",bg="orange")
        labelexp2.place(x=80,y=40,relx=0.25,rely=0.25)
        buttonw['state']='disable'
        buttonre['state']='disable'
    else:
        with open('user.csv','r') as csv_file:
            csv_reader=csv.reader(csv_file)
            for line in csv_reader:
                try:
                    if((line[0]!='name')and(line[0]!='pin')and(line[1]!='balance')):
                        userP[line[0].strip()]=int(line[1])
                        userb[line[0].strip()]=int(line[2])
                except:
                    print("line is empty")
        spark1()
label=Label(root,text="WELCOME TO THE ATM")
labeln=Label(text="Name:",font='Times 15',fg='Red')
lablepin=Label(text="Pin :",font='Times 15',fg='Red')
labelcash=Label(text="Cash:",font='Times 15',fg='Red')
buttonw=Button(text="Withdraw",font='Times 20',fg='Red',bg='yellow',command=spark)
buttonre=Button(text="Reset",font='Times 20',fg='Red',bg='yellow',command=active_all)
buttont=Button(text="Take",font='Times 20',fg='Red',bg='yellow',command=active_all)
label.config(font='Times 45',fg='Red',bg='Yellow')
label.place(relx=0.25,y=0.25)
labeln.place(x=80,y=80,relx=0.25,rely=0.25)
lablepin.place(x=80,y=120,relx=0.25,rely=0.25)
labelcash.place(x=80,y=160,relx=0.25,rely=0.25)
root.geometry('1000x1000+650+350')
entryname=Entry(font='Times 15')
entrypin=Entry(show='#',font='Times 15')
entrym=Entry(font='Times 15')
entryname.place(x=140,y=80,height=30,width=200,relx=0.25,rely=0.25)
entrypin.place(x=140,y=120,relx=0.25,rely=0.25,height=30,width=200)
entrym.place(x=140,y=160,relx=0.25,rely=0.25,height=30,width=200)
buttonw.place(x=200,y=200,relx=0.25,rely=0.25,height=30,width=200)
buttonre.place(x=200,y=240,relx=0.25,rely=0.25,height=30,width=200)
root.mainloop()
