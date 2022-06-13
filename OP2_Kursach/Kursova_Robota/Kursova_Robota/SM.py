import math


#Клас, що представляє методи пошуку елементів у программі

#Атрибути:

#LG : list
#Масив індексів елментів, які були перевірені в ході виконання алгоритмів пошуку

# Методи
#    ------
#    ********************************************************
#    ********************************************************
#    def __init__(self)
#        Конструктор класу

#        Аргументи:
#        1) self - об'єкт класу

#        Повертає: None
#    ********************************************************
#    ********************************************************
#    def Linear_Search(self, Arr, num, seeken)
#        Послідовний пошук

#        Аргументи:
#        1) self - об'єкт класу
#        2) Arr - масив з унікальних цілочисленних значень
#        3) num - к-сть елементів у масиві
#        4) seeken - значення шуканого елемента масива

#        Повертає: None
#    ********************************************************
#    ********************************************************
#    def Binary_Search(self, Arr, num, seeken)
#        Бінарний пошук
        
#        Аргументи:
#        1) self - об'єкт класу
#        2) Arr - масив з унікальних цілочисленних значень
#        3) num - к-сть елементів у масиві
#        4) seeken - значення шуканого елемента масива

#        Повертає: None
#    ********************************************************
#    ********************************************************
#    def O_B_Search(self, Arr, num, seeken)
#        Однорідний бінарний пошук
        
#        Аргументи:
#        1) self - об'єкт класу
#        2) Arr - масив з унікальних цілочисленних значень
#        3) num - к-сть елементів у масиві
#        4) seeken - значення шуканого елемента масива

#        Повертає: None
#    ********************************************************
#    ********************************************************
#    def Sharrah_Search(self, Arr, num, seeken)
#        Пошук методом Шарра
        
#        Аргументи:
#        1) self - об'єкт класу
#        2) Arr - масив з унікальних цілочисленних значень
#        3) num - к-сть елементів у масиві
#        4) seeken - значення шуканого елемента масива

#        Повертає: None
#    ********************************************************
#    ********************************************************


class SM:
    def __init__(self):
        self.LG=[]


    def GetLis(self):
        return self.LG


    def Linear_Search(self, Arr, num, seeken):
        Lis=[]
        itt = 0
        flag=1
        while flag == 1:
            if itt == num :
                flag = 0
            elif Arr[itt] == seeken :
                flag = 0
                Lis.append(itt)
            else:
                Lis.append(itt)
                itt+=1
        self.LG=Lis


    def Binary_Search(self, Arr, num, seeken):
        Lis= []
        posb=0
        pose=num-1
        flag=1
        while flag==1:
            if pose>=posb:
                mid = (posb+pose)//2
                if Arr[mid]==seeken:
                    Lis.append(mid)
                    flag=0
                elif Arr[mid] > seeken:
                    Lis.append(mid)
                    pose = mid-1
                else:
                    Lis.append(mid)
                    posb = mid+1
            else:
                flag=0
        self.LG=Lis


    def O_B_Search(self, Arr, num, seeken):
        Lis=[]
        b=int(num)//2
        i =b
        flag=1
        while flag==1:
            if b>0:
                if i>=num:
                    i-=b//2+1
                    b//=2
                elif i<0:
                    i+=b//2+1
                    b//=2
                elif Arr[int(i)]==seeken:
                    Lis.append(int(i))
                    flag=0
                elif Arr[int(i)]<seeken:
                    Lis.append(int(i))
                    i+=b//2+1
                    b//=2
                else:
                    Lis.append(int(i))
                    i-=b//2+1
                    b//=2
            else:
                if i<num and i>=0:
                    Lis.append(int(i))
                flag=0
        self.LG=Lis
 
     
    def Sharrah_Search(self, Arr, num, seeken):
        Lis=[]
        flag=1
        k=(math.log2(num))//1
        i=(2**k)-1
        if seeken <= Arr[int(i)]:
            b=(i+1)
            while flag==1:
                if b>0:
                    if i>=num:
                        i-=b//2+1
                        b//=2
                    elif i<0:
                        i+=b//2+1
                        b//=2
                    elif Arr[int(i)]==seeken:
                        Lis.append(int(i))
                        flag=0
                    elif Arr[int(i)]<seeken:
                        Lis.append(int(i))
                        i+=b//2+1
                        b//=2
                    else:
                        Lis.append(int(i))
                        i-=b//2+1
                        b//=2
                else:
                    if i<num and i>=0:
                        Lis.append(int(i))
                    flag=0
        else:
            l=math.log2(num-i)
            i=num-2**l
            b=2**(l)
            while flag==1:
                if b>0:
                    if i>=num:
                        i-=b//2+1
                        b//=2
                    elif i<0:
                        i+=b//2+1
                        b//=2
                    elif Arr[int(i)]==seeken:
                        Lis.append(int(i))
                        flag=0
                    elif Arr[int(i)]<seeken:
                        Lis.append(int(i))
                        i+=b//2+1
                        b//=2
                    else:
                        Lis.append(int(i))
                        i-=b//2+1
                        b//=2
                else:
                    if i<num and i>=0:
                        Lis.append(int(i))
                    flag=0
        self.LG=Lis