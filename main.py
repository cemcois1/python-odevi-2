import yaml
import json
from tkinter import *

def readjson(path):
    with open (path) as f:
        data=yaml.safe_load(f)
    return data

def makeListBox():
    data=readjson('node_modules\country-json\src\country-by-name.json')
    for i in range(247):
        mylistbox.insert(END,str(data[i]["country"]))
def top10pop():
    top=Toplevel()
    top.title("Top 10 population")
    listem=readjson("node_modules\country-json\src\country-by-population.json")
    for i in range (243):
        for j in range(242):
            if(int(listem[i]["population"])<int(listem[j]["population"])):
                tmp=listem[j]
                listem[j]=listem[i]
                listem[i]=tmp
    for  k in range(11) :
        Label(top,text=str(k+1)+". Country ="+listem[242-k]["country"]+"   population = "+listem[242-k]["population"]).pack()


def printlabel(text1,side):
    labelasd=Label(rightframe,text=text1).pack(side=side)
    return labelasd
def changeLabel(event):
    mysellection=(mylistbox.curselection())
    data_c= readjson("node_modules\country-json\src\country-by-name.json")
    for i in mysellection:
        print(data_c[i]["country"])
        updateDepositLabel(text1,"Country name ="+data_c[i]["country"])
        data_cap=readjson("node_modules\country-json\src\country-by-capital-city.json")
        for j in range(243):
            if(data_c[i]["country"]==data_cap[j]["country"]):
                updateDepositLabel(text2,"Capital city ="+str(data_cap[j]["city"]))
                break
        data_lang=readjson("node_modules\country-json\src\country-by-languages.json")
        tmp=" "
        for j in range(994):
            if(data_c[i]["country"]==data_lang[j]["country"]):
                tmp+=str(data_lang[j]["language"]+" ")
        updateDepositLabel(text3,"Languages ="+tmp)
        data_lang=readjson("node_modules\country-json\src\country-by-avg-male-height.json")
        for j in range(243):
            if(data_c[i]["country"]==data_lang[j]["country"]):
                updateDepositLabel(text4,"Male height = "+str(data_lang[j]["height"]))
                break
        data_lang=readjson("node_modules\country-json\src\country-by-calling-code.json")

        for j in range(243):
            if(data_c[i]["country"]==data_lang[j]["country"]):
                updateDepositLabel(text5,"Calling code = "+str(data_lang[j]["calling_code"]))
                break

        
        data_lang=readjson("node_modules\country-json\src\country-by-population.json")
        for j in range(243):
            if(data_c[i]["country"]==data_lang[j]["country"]):
                updateDepositLabel(text6,"Calling code = "+str(data_lang[j]["population"]))
                break
        data_lang=readjson("node_modules\country-json\src\country-by-domain-tld.json")

        for j in range(243):
            if(data_c[i]["country"]==data_lang[j]["country"]):
                updateDepositLabel(text7,"Domain = "+str(data_lang[j]["tld"]))
                break
        

        data_lang=readjson("node_modules\country-json\src\country-by-government-type.json")

        for j in range(243):
            if(data_c[i]["country"]==data_lang[j]["country"]):
                updateDepositLabel(text8,"Goverment type = "+str(data_lang[j]["government"]))
                break
        data_lang=readjson("node_modules\country-json\src\country-by-abbreviation.json")

        for j in range(243):
            if(data_c[i]["country"]==data_lang[j]["country"]):
                updateDepositLabel(text9,"Abbrevation = "+str(data_lang[j]["abbreviation"]))
                break
        data_lang=readjson("node_modules\country-json\src\country-by-life-expectancy.json")

        for j in range(243):
            if(data_c[i]["country"]==data_lang[j]["country"]):
                updateDepositLabel(text10,"Life expectancy = "+str(data_lang[j]["expectancy"]))
                break
                
        data_lang=readjson("node_modules\country-json\src\country-by-surface-area.json")

        for j in range(243):
            if(data_c[i]["country"]==data_lang[j]["country"]):
                updateDepositLabel(text11,"Area = "+str(data_lang[j]["area"]))
                break
                

        
def search():
    data=readjson("node_modules\country-json\src\country-by-name.json")
    kontrol=True
    for i in range(247):#48 country
        if( str(str.upper( mystring.get()))[0]==data[i]["country"][0] and kontrol==True):#listeyi tara
            kontrol=False
            mylistbox.yview(i)
            break
 






def updateDepositLabel(textobj,txt): # you may have to use *args in some cases
    textobj.set(txt)

root=Tk()
root.title("ülkeler")
root.configure(background='#FFD0D2')

mystring =StringVar(root)
leftframe=Frame(root).pack(side="left")
top10pop=Button(leftframe,text="Top 10 Population",command=top10pop).pack(side="top")
my_entry = Entry(leftframe,textvariable = mystring,width=30,).pack(side="left")
my_buton= Button(root,text="Search",command=search).pack(side="left")
bottomframe=Frame(root).pack(side="bottom")
rightframe=Frame(root,bg="#FFD0D2").pack(side="bottom")

mylistbox=Listbox(leftframe,width=20,height=20)
makeListBox()
mylistbox.pack(side="left",fill="y")

scrool=Scrollbar(leftframe,orient=VERTICAL)
scrool.config(command=mylistbox.yview)
scrool.pack(side="left",fill="y")

text0 = StringVar()
text1 = StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()
text5 = StringVar()
text6 = StringVar()
text7 = StringVar()
text8 = StringVar()
text9 = StringVar()
text10 = StringVar()
text11 = StringVar()

label0=  Label(rightframe,textvariable=text0).pack(side="top",padx=20,pady=40)
label1= Label(rightframe,textvariable=text1).pack(padx=20,pady=40)
label2=  Label(rightframe,textvariable=text2).pack(side="bottom",padx=20,pady=40)
label3=  Label(rightframe,textvariable=text3).pack(side="bottom",padx=20,pady=40)
label4=  Label(rightframe,textvariable=text4).pack(side="left",padx=20,pady=40)
label5=  Label(rightframe,textvariable=text5).pack(side="right",padx=20,pady=40)
label6=  Label(rightframe,textvariable=text6).pack(side="left",padx=20,pady=40)
label7=  Label(rightframe,textvariable=text7).pack(side="right",padx=20,pady=40)
label8=  Label(rightframe,textvariable=text8).pack(side="left",padx=20,pady=40)
label9=  Label(rightframe,textvariable=text9).pack(side="right",padx=20,pady=40)
label11= Label(rightframe,textvariable=text10).pack(side="left",padx=20,pady=40)
updateDepositLabel(text0,"Features")
updateDepositLabel(text1,"Country name")
updateDepositLabel(text2,"capital city")
updateDepositLabel(text3,"languages ")
updateDepositLabel(text4,"male height")
updateDepositLabel(text5,"calling code")
updateDepositLabel(text6,"population")
updateDepositLabel(text7,"domain tld")
updateDepositLabel(text8,"goverment type")
updateDepositLabel(text9,"abbrevation")
updateDepositLabel(text10,"life expectancy")
updateDepositLabel(text11,"Area")



mylistbox.bind('<Double-1>',changeLabel)









root.mainloop()