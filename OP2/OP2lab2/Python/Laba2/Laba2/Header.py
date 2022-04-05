import pickle

class data:
    def __init__(self, name, creation_date, last_date, price):
        self.name = name
        self.creation_date = creation_date
        self.last_date = last_date
        self.price=price

def enter_f(name1, qu):                    #доповнення у файл 1 з можливістю очистити попередній вміст
    a=int(input("Enter ammount of products: "))
    prod=list()
    if qu=='1':     #користувач може вибрати, чи хоче він очистити файл від попередніх данних (в main() вводимо que)
        text=open(name1, "wb")
        text.close()
    text=open(name1, "ab")   #у будь-якому випадку ми доповнюємо наш бінарний файл
    for i in range(a):
        name=str(input("Name: "))
        creation_date=str(input("Date of creation (dd.mm.yyyy): "))
        last_date=str(input("Last date (dd.mm.yyyy): "))
        price=float(input("Price: "))
        datum=data(name, creation_date, last_date, price)
        prod.append(datum)
    pickle.dump(prod, text)
    text.close()

def ou(name1):         #вивід вмісту файла
    text=open(name1, 'rb')
    prod=pickle.load(text)
    for p in prod:
        print(p.name, " - ", p.creation_date, " - ", p.last_date, " - ", p.price, " dollars")
    text.close()

def fil(name1, name2, date):            #заповнення файла 2 інформацією про товари, час придатності яких менше 1/10 від початкового
    lis=list()
    text=open(name1, 'rb')
    inp=open(name2, 'wb')
    prod=pickle.load(text)
    am_days=0
    H=date[0:2]               #підрахунок к-сті діб (у кожному місяці 30 діб, у році - 360)
    am_days=am_days+int(H)
    H=date[3:5]
    am_days=am_days+(int(H)*30)
    H=date[6:10]
    am_days=am_days+(int(H)*360)
    for p in prod:        #підрахунок к-сті діб (у кожному місяці 30 діб, у році - 360)
        am_days_c=0
        am_days_l=0
        H=p.creation_date[0:2]
        am_days_c=am_days_c+int(H)
        H=p.creation_date[3:5]
        am_days_c=am_days_c+(int(H)*30)
        H=p.creation_date[6:10]
        am_days_c=am_days_c+(int(H)*360)
        H=p.last_date[0:2]
        am_days_l=am_days_l+int(H)
        H=p.last_date[3:5]
        am_days_l=am_days_l+(int(H)*30)
        H=p.last_date[6:10]
        am_days_l=am_days_l+(int(H)*360)
        if (float((am_days_l - am_days)) / (am_days_l - am_days_c) < 0.1 and float((am_days_l - am_days)) / (am_days_l - am_days_c) >= 0):
            lis.append(p)
    pickle.dump(lis, inp)
    text.close()
    inp.close()

def ou_sp(name1, date):    #вивід товарів, виготовлених за останні 10 діб
    text=open(name1, 'rb')
    prod=pickle.load(text)
    am_days=0                      #підрахунок к-сті діб (у кожному місяці 30 діб, у році - 360)
    H=date[0:2]
    am_days=am_days+int(H)
    H=date[3:5]
    am_days=am_days+(int(H)*30)
    H=date[6:10]
    am_days=am_days+(int(H)*360)
    for p in prod:
        am_days_c=0
        H=p.creation_date[0:2]
        am_days_c=am_days_c+int(H)
        H=p.creation_date[3:5]
        am_days_c=am_days_c+(int(H)*30)
        H=p.creation_date[6:10]
        am_days_c=am_days_c+(int(H)*360)
        if ((am_days - am_days_c) < 10 and (am_days - am_days_c) >= 0):
            print(p.name, " - ", p.creation_date, " - ", p.last_date, " - ", p.price, " dollars")
    text.close()