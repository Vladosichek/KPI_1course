from tkinter import *
import random
from SM import *


#Клас, що представляє інтерфейс програми

#Атрибути:

#GTL : list
#Масив індексів початкового та останього індекса елементів, що були перевірені

#ST : str
#Ім'я тегу для підсвічування шуканого елемента

#length_entry : Entry
#Поле вводу розміру масива

#length_seeken : Entry
#Поле вводу значення шуканого елементу

#mes4 : Label
#Напис, що відображає результат пошуку шуканого елемента у масиві (Yes/No/None)

#Методи
#    ------
#    ********************************************************
#    ********************************************************
#    def __init__(self, canvas, D, leng, snum, meth, t1, t2)
#        Конструктор класу

#        Аргументи:
#        1) self - об'єкт класу
#        2) canvas - рамка вікна програми, у яке виводиться інтерфейс
#        3) D - об'єкт класу Data, що зберігає введені дані
#        4) leng - розмір генерованого масиву
#        5) snum - шуканий елемент
#       6) meth - варіант метода пошуку
#       7) t1 - текстове поле для виведення згенерованого масива
#       8) t2 - текстове поле для виведення послідовності перевірки

#        Повертає: None
#    ********************************************************
#    ********************************************************
#    def gen(self, D, leng, t1, t2)
#       Генерація масива унікальних елементів

#        Аргументи:
#        1) self - об'єкт класу
#        2) D - об'єкт класу Data, що зберігає введені дані
#        3) leng - розмір генерованого масиву
#        4) t1 - текстове поле для виведення згенерованого масива
#        5) t2 - текстове поле для виведення послідовності перевірки

#        Повертає: None
#    ********************************************************
#    ********************************************************
#    def sek(self, D, snum, meth, t1, t2)
#        Пошук шуканого елемента масива

#        Аргументи:
#        1) self - об'єкт класу
#        2) D - об'єкт класу Data, що зберігає введені дані
#        3) snum - шуканий елемент
#        4) meth - варіант метода пошуку
#        5) t1 - текстове поле для виведення згенерованого масива
#        6) t2 - текстове поле для виведення послідовності перевірки

#        Повертає: None
#    ********************************************************
#    ********************************************************


class Interface:
    def __init__(self, canvas, D, leng, snum, meth, t1, t2):
        self.GTL=[] 
        self.ST=""
        mes1 = Label(canvas, text = "Enter ammount of elements:", padx=15, pady=10, font="14")
        mes1.grid(row=0, column=0, sticky=W)
        self.length_entry=Entry(canvas, textvariable=leng, font="14")
        self.length_entry.grid(row=0, column=1, sticky='ew')
        mes2 = Label(canvas, text = "Enter seeken element:", padx=15, pady=10, font="14")
        mes2.grid(row=1, column=0, sticky=W)
        self.length_seeken=Entry(canvas, textvariable=snum, font="14")
        self.length_seeken.grid(row=1, column=1, sticky='ew')
        mes3 = Label(canvas, text = "Is the seeken in the array:", padx=15, pady=10, font="14")
        mes3.grid(row=2, column=0, sticky=W)
        self.mes4 = Label(canvas, text = "None", fg='black',  padx=15, pady=10, font="14")
        self.mes4.grid(row=2, column=1, sticky='nsew')
        but1=Button(canvas, text = "Generate", command=lambda: self.gen(D, leng, t1, t2), font="14")
        but1.grid(row=0, column=2, sticky='nsew')
        but2=Button(canvas, text = "Search", command=lambda: self.sek(D, snum, meth, t1, t2), font="14")
        but2.grid(row=1, column=2, sticky='nsew')


    def gen(self, D, leng, t1, t2):
        quanstr=leng.get()
        if quanstr.isnumeric():
            quan=int(quanstr)
            for i in range(len(self.GTL)):
                t1.tag_delete(self.GTL[i])
            if self.ST!="":
                t1.tag_delete(self.ST)
            self.GTL=[] 
            self.ST=""
            if quan < 1000:
                quan=1000
                self.length_entry.delete("0", "end")
                self.length_entry.insert(INSERT, "1000")
            Array=random.sample(range(quan*5), quan)
            Array.sort()
            Str1=str(Array)
            Str1=Str1[1:len(Str1)-1]
            t1.delete("1.0", "end")
            t1.insert(INSERT, Str1)
            t2.delete("1.0", "end")
            t2.insert(INSERT, "None")
            self.mes4.config(text="None")
            D.SetArr(Array)
            D.SetNum(quan)
        else:
            self.length_entry.delete("0", "end")
            self.length_entry.insert(INSERT, "Wrong input!")


    def sek(self, D, snum, meth, t1, t2):
        sknstr=snum.get()
        if sknstr.isnumeric():
            skn=int(sknstr)
            quan=D.GetNum()
            arr=D.GetArr()
            var=meth.get()
            D.SetSeeken(skn)
            Liss=SM()
            for i in range(len(self.GTL)):
                t1.tag_delete(self.GTL[i])
            if self.ST!="":
                t1.tag_delete(self.ST)
            self.GTL=[] 
            self.ST=""
            if var==1:
                Liss.Linear_Search(arr, quan, skn)
            elif var==2:
                Liss.Binary_Search(arr, quan, skn)
            elif var==3:
                Liss.O_B_Search(arr, quan, skn)
            elif var==4:
                Liss.Sharrah_Search(arr, quan, skn)
            D.SetGone(Liss.GetLis())
            Str1="" 
            Str2=""
            LT = [] 
            a1 = int(-1)
            a2 = int(-1)
            for i in range(len(arr)):
                if Liss.GetLis().count(i)>0:
                    if(arr[i]==skn):
                        a1=len(Str1)
                        Str1+=str(arr[i])+", "
                        a2=len(Str1)-3
                    else:
                        LT.append(len(Str1))
                        Str1+=str(arr[i])+", "
                        LT.append(len(Str1)-3)
                else:
                    Str1+=str(arr[i])+", "
            Str1=Str1[:len(Str1)-2]
            for i in range(len(Liss.GetLis())):
                Str2+=str(i+1)+".["+str(Liss.GetLis()[i])+"]("+str(arr[Liss.GetLis()[i]])+")\n"
            Str2=Str2[:len(Str2)-1]
            if Str2=="":
                Str2="Choose method!"
            t1.delete("1.0", "end")
            t1.insert(INSERT, Str1)
            t2.delete("1.0", "end")
            t2.insert(INSERT, Str2)
            i=0
            while i < len(LT):
                C1="1."+str(LT[i])
                C2="1."+str(LT[i+1]+1)
                Name="Gone"+str(i//2+1)
                t1.tag_add(Name, C1, C2)
                t1.tag_config(Name, background="red", foreground="white")
                self.GTL.append(Name)
                i+=2
            if a1 !=-1:
                C1="1."+str(a1)
                C2="1."+str(a2+1)
                self.ST="Seeken"
                t1.tag_add(self.ST, C1, C2)
                t1.tag_config(self.ST, background="green", foreground="white")
            if len(Liss.GetLis())>0 and arr[Liss.GetLis()[len(Liss.GetLis())-1]]==skn:
                self.mes4.config(text="Yes", fg='green')
            else:
                self.mes4.config(text="No", fg='red')
        else:
            self.length_seeken.delete("0", "end")
            self.length_seeken.insert(INSERT, "Wrong input!")


    def GetLS(self):
        return self.length_seeken


    def GetLE(self):
        return self.length_entry


    def GetM4(self):
        return self.mes4


    def GetGTL(self):
        return self.GTL


    def GetST(self):
        return self.ST