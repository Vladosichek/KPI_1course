from Tumbler import *
from TF import *
from tkinter import *
from Data import *
from MENU import *
from Interface import *

#Основний файл, у якому створюються усі об'єкти та ініціалізуються налаштування програми

root = Tk()
root.title("Search Methods")
root.geometry("1600x750")

fram1=Frame(root, padx=15, pady=10)
fram1.grid(row=0, column=0, sticky='nsew')
fram2=Frame(root, padx=15, pady=10)
fram2.grid(row=1, column=0, sticky='nsew')
fram3=Frame(root, padx=15, pady=10)
fram3.grid(row=0, column=1, sticky='nsew')
fram4=Frame(root, padx=15, pady=10)
fram4.grid(row=1, column=1, sticky='nsew')

Dat =Data()
leng = StringVar()
snum = StringVar()
ChM=Tumbler(fram3)

text1=TF(fram2)
text2=TF(fram4)

Cons=Interface(fram1, Dat, leng, snum, ChM.GetMeth(), text1.GetText(), text2.GetText())
main_menu = MENU(root, Cons.GetLS(), Cons.GetLE(), Cons.GetM4(), ChM.GetMeth(), Cons.GetGTL(), Cons.GetST(), text1.GetText(), text2.GetText())

root.mainloop()