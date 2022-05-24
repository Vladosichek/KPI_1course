class Event:
    def __init__(self, dat, in_t, en):
        self.dat = dat 
        self.in_t = in_t 
        self.en = en 
    def Last_calc(self, dat_o):
        m = 0
        F = dat_o
        H = F[0:2]
        m+=int(H)*60
        H = F[3:5]
        m+=int(H)
        d = 0
        F = self.in_t
        H = F[0:2]
        d += int(H)*60
        H = F[3:5]
        d += int(H)
        F = self.en
        H = F[0:2]
        d += int(H)*60
        H = F[3:5]
        d += int(H)
        m -= d
        if m > 0:
            q = m // 60
            c=str(q)
            s = c
            q = m % 60
            c=str(q)
            s += ':' + c
            s += " will left to the party!"
        else:
            s = "Party will have begun!"
        return s 

class Birthday(Event):
    def __init__(self, dat, in_t, en, PIB, place, age):
        super().__init__(dat, in_t, en)
        self.PIB = PIB 
        self.place = place
        self.age = age

class Meeting(Event):
    def __init__(self, dat, in_t, en, PIB, place):
        super().__init__(dat, in_t, en)
        self.PIB = PIB 
        self.place = place

def seek(lis, amm):
    ma=-1
    pos=-1
    m=0
    for i in range(amm):
        F = lis[i].in_t
        H = F[0:2]
        m += int(H)*60
        H = F[3:5]
        m += int(H)
        if ma < m:
            ma = m
            pos = i
        m=0
    return pos