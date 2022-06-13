from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox


#����, �� ����������� ���� ��������

#��������:

# ³�����

# ������
#    ------
#    ********************************************************
#    ********************************************************
#    def __init__(self, canvas, leng_seek, leng_en, m4, meth, GTL, ST, t1, t2)
#        ����������� �����

#        ���������:
#        1) self - ��'��� �����
#        2) canvas - ����� ���� ��������, � ��� ���������� ���������
#        3) leng_seek - ���� ����� ������ ������
#        4) leng_en - ���� ����� �������� �������� ��������
#        5) m4 - �����, �� �������� ��������� ������ �������� �������� � ����� (Yes/No/None)
#        6) meth - ������ ������ ������
#        7) GTL - ����� ������� ����������� �� ��������� ������� ��������, �� ���� ��������
#        8) ST - ��'� ���� ��� ����������� �������� ��������
#        9) t1 - �������� ���� ��� ��������� ������������� ������
#        10) t2 - �������� ���� ��� ��������� ����������� ��������

#        �������: None
#    ********************************************************
#    ********************************************************
#    def ques(self, canvas)
#        ���������� ��������

#        ���������:
#        1) self - ��'��� �����
#        2) canvas - ����� ���� ��������, � ��� ���������� ���������

#        �������: None
#    ********************************************************
#    ********************************************************
#    def restart(self, leng_seek, leng_en, m4, meth, GTL, ST, t1, t2)
#        �������� ����� ��������

#        ���������:
#        1) self - ��'��� �����
#        2) leng_seek - ���� ����� ������ ������
#        3) leng_en - ���� ����� �������� �������� ��������
#        4) m4 - �����, �� �������� ��������� ������ �������� �������� � ����� (Yes/No/None)
#        5) meth - ������ ������ ������
#        6) GTL - ����� ������� ����������� �� ��������� ������� ��������, �� ���� ��������
#        7) ST - ��'� ���� ��� ����������� �������� ��������
#        8) t1 - �������� ���� ��� ��������� ������������� ������
#        9) t2 - �������� ���� ��� ��������� ����������� ��������

#        �������: None
#    ********************************************************
#    ********************************************************
#    def inf(self)
#        ���� ������� ������ ��� ��������

#        ���������:
#        1) self - ��'��� �����

#        �������: None
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