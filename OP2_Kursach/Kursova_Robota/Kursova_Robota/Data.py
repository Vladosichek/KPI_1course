#����, �� ����������� ������� ��� � ��� ��������� ��������

#��������:

#Arr : list
#����� � ��������� ������������� �������

#num : int
#�-��� �������� � �����

#seeken : int
#�������� �������� �������� ������

#Gone : list
#����� ������� �������, �� ���� �������� � ��� ��������� ��������� ������

# ������
    
#   ********************************************************
#   ********************************************************
#    def __init__(self)
#       ����������� �����

#        ���������:
#        1) self - ��'��� �����

#        �������: None
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