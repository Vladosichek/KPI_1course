from tkinter import *


#Клас, що представляє отримані дані в ході виконання програми

#Атрибути:

#text : Text
#Текстове поле для виведення згенерованого масива чи послідовності перевірки елементів

# Методи
#    ------
#    ********************************************************
#    ********************************************************
#    def __init__(self, canvas)
#        Конструктор класу

#        Аргументи:
#        1) self - об'єкт класу
#        2) canvas - рамка вікна програми, у яке виводиться текстове поле

#        Повертає: None
#    ********************************************************
#    ********************************************************


class TF:
    def __init__(self, canvas):
        self.text=Text(canvas, padx=15, pady=10, font="14")
        self.text.grid(row=0, column=0)
        scroll=Scrollbar(canvas, command=self.text.yview())
        scroll.grid(row=0, column=1, rowspan=2, sticky='ns')
        scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=scroll.set)
        self.text.insert(INSERT, "None")


    def GetText(self):
        return self.text