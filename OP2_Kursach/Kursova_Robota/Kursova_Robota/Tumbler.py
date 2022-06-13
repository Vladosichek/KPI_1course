from tkinter import *


#Клас, що представляє поле вибору метода пошука елемента у масиві

#Атрибути:

#meth : IntVar
#Варіант метода пошуку

# Методи
#    ------
#    ********************************************************
#    ********************************************************
#    def __init__(self, canvas)
#        Конструктор класу

#        Аргументи:
#        1) self - об'єкт класу
#        2) canvas - рамка вікна програми, у яке виводяться варіанти вибору методу пошука

#        Повертає: None
#    ********************************************************
#    ********************************************************


class Tumbler:
    def __init__(self, canvas):
        self.meth = IntVar()
        header = Label(canvas, text="Choose method:", padx=15, pady=10, font="14")
        header.grid(row=0, column=0, sticky=W)
        poslid_checkbutton = Radiobutton(canvas, text="Linear Search", value=1, variable=self.meth, padx=15, pady=10, font="14")
        poslid_checkbutton.grid(row=1, column=0, sticky=W) 
        binary_checkbutton = Radiobutton(canvas, text="Binar Search", value=2, variable=self.meth, padx=15, pady=10, font="14")
        binary_checkbutton.grid(row=2, column=0, sticky=W)
        odnor_binary_checkbutton = Radiobutton(canvas, text="O. B. Search", value=3, variable=self.meth, padx=15, pady=10, font="14")
        odnor_binary_checkbutton.grid(row=3, column=0, sticky=W)
        Sharra_checkbutton = Radiobutton(canvas, text="Sharrah Search", value=4, variable=self.meth, padx=15, pady=10, font="14")
        Sharra_checkbutton.grid(row=4, column=0, sticky=W)


    def GetMeth(self):
        return self.meth