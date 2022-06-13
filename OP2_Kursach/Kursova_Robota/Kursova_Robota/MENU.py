from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox


#Клас, що представляє меню програми

#Атрибути:

# Відсутні

# Методи
#    ------
#    ********************************************************
#    ********************************************************
#    def __init__(self, canvas, leng_seek, leng_en, m4, meth, GTL, ST, t1, t2)
#        Конструктор класу

#        Аргументи:
#        1) self - об'єкт класу
#        2) canvas - рамка вікна програми, у яке виводиться інтерфейс
#        3) leng_seek - поле вводу розміру масива
#        4) leng_en - поле вводу значення шуканого елементу
#        5) m4 - напис, що відображає результат пошуку шуканого елемента у масиві (Yes/No/None)
#        6) meth - варіант метода пошуку
#        7) GTL - масив індексів початкового та останього індекса елементів, що були перевірені
#        8) ST - ім'я тегу для підсвічування шуканого елемента
#        9) t1 - текстове поле для виведення згенерованого масива
#        10) t2 - текстове поле для виведення послідовності перевірки

#        Повертає: None
#    ********************************************************
#    ********************************************************
#    def ques(self, canvas)
#        Завершення програми

#        Аргументи:
#        1) self - об'єкт класу
#        2) canvas - рамка вікна програми, у яке виводиться інтерфейс

#        Повертає: None
#    ********************************************************
#    ********************************************************
#    def restart(self, leng_seek, leng_en, m4, meth, GTL, ST, t1, t2)
#        Очищення форми програми

#        Аргументи:
#        1) self - об'єкт класу
#        2) leng_seek - поле вводу розміру масива
#        3) leng_en - поле вводу значення шуканого елементу
#        4) m4 - напис, що відображає результат пошуку шуканого елемента у масиві (Yes/No/None)
#        5) meth - варіант метода пошуку
#        6) GTL - масив індексів початкового та останього індекса елементів, що були перевірені
#        7) ST - ім'я тегу для підсвічування шуканого елемента
#        8) t1 - текстове поле для виведення згенерованого масива
#        9) t2 - текстове поле для виведення послідовності перевірки

#        Повертає: None
#    ********************************************************
#    ********************************************************
#    def inf(self)
#        Вивід короткої довідки про програму

#        Аргументи:
#        1) self - об'єкт класу

#        Повертає: None
#    ********************************************************
#    ********************************************************


class MENU:
    def __init__(self, canvas, leng_seek, leng_en, m4, meth, GTL, ST, t1, t2):
        MM=Menu() 
        MM.add_cascade(label="INFO", command=lambda: self.inf(), font="14")
        MM.add_cascade(label="RESTART", command=lambda: self.restart(leng_seek, leng_en, m4, meth, GTL, ST, t1, t2), font="14")
        MM.add_cascade(label="EXIT", command=lambda: self.ques(canvas), font="14")
        canvas.config(menu=MM)


    def ques(self, canvas):
        if askyesno("Quit", "Do you want to quit the program?"):
            canvas.destroy()


    def restart(self, leng_seek, leng_en, m4, meth, GTL, ST, t1, t2):
        for i in range(len(GTL)):
            t1.tag_delete(GTL[i])          
        if ST!="":
            t1.tag_delete(ST)
        leng_seek.delete("0", "end")
        leng_en.delete("0", "end")
        m4.config(text="None", fg='black')
        meth.set(0)
        t1.delete("1.0", "end")
        t1.insert(INSERT, "None")
        t2.delete("1.0", "end")
        t2.insert(INSERT, "None")


    def inf(self):
        tline="This is program for finding numbers in arrays!\nInput integer numbers of length of an array over 1000!\nDo not forget to choose method of search!"
        messagebox.showinfo("General info about program", tline)