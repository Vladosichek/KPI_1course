#Клас, що представляє отримані дані в ході виконання програми

#Атрибути:

#Arr : list
#Масив з унікальних цілочисленних значень

#num : int
#К-сть елементів у масиві

#seeken : int
#Значення шуканого елемента масива

#Gone : list
#Масив індексів елментів, які були перевірені в ході виконання алгоритмів пошуку

# Методи
    
#   ********************************************************
#   ********************************************************
#    def __init__(self)
#       Конструктор класу

#        Аргументи:
#        1) self - об'єкт класу

#        Повертає: None
#    ********************************************************
#    ********************************************************


class Data:
    def __init__(self):
        self.Arr=[]
        self.num=0
        self.seeken=0
        self.Gone=[]


    def SetArr(self, ArrN):
        self.Arr = ArrN


    def SetNum(self, numN):
        self.num = numN


    def SetSeeken(self, seekenN):
        self.seeken = seekenN


    def SetGone(self, GoneN):
        self.Gone = GoneN


    def GetArr(self):
        return self.Arr


    def GetNum(self):
        return self.num


    def GetSeeken(self):
        return self.seeken


    def GetGone(self):
        return self.Gone