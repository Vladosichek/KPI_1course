from tkinter import *


#����, �� ����������� ������� ��� � ��� ��������� ��������

#��������:

#text : Text
#�������� ���� ��� ��������� ������������� ������ �� ����������� �������� ��������

# ������
#    ------
#    ********************************************************
#    ********************************************************
#    def __init__(self, canvas)
#        ����������� �����

#        ���������:
#        1) self - ��'��� �����
#        2) canvas - ����� ���� ��������, � ��� ���������� �������� ����

#        �������: None
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