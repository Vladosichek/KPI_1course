import math


#����, �� ����������� ������ ������ �������� � ��������

#��������:

#LG : list
#����� ������� �������, �� ���� �������� � ��� ��������� ��������� ������

# ������
#    ------
#    ********************************************************
#    ********************************************************
#    def __init__(self)
#        ����������� �����

#        ���������:
#        1) self - ��'��� �����

#        �������: None
#    ********************************************************
#    ********************************************************
#    def Linear_Search(self, Arr, num, seeken)
#        ���������� �����

#        ���������:
#        1) self - ��'��� �����
#        2) Arr - ����� � ��������� ������������� �������
#        3) num - �-��� �������� � �����
#        4) seeken - �������� �������� �������� ������

#        �������: None
#    ********************************************************
#    ********************************************************
#    def Binary_Search(self, Arr, num, seeken)
#        �������� �����
        
#        ���������:
#        1) self - ��'��� �����
#        2) Arr - ����� � ��������� ������������� �������
#        3) num - �-��� �������� � �����
#        4) seeken - �������� �������� �������� ������

#        �������: None
#    ********************************************************
#    ********************************************************
#    def O_B_Search(self, Arr, num, seeken)
#        ��������� ������� �����
        
#        ���������:
#        1) self - ��'��� �����
#        2) Arr - ����� � ��������� ������������� �������
#        3) num - �-��� �������� � �����
#        4) seeken - �������� �������� �������� ������

#        �������: None
#    ********************************************************
#    ********************************************************
#    def Sharrah_Search(self, Arr, num, seeken)
#        ����� ������� �����
        
#        ���������:
#        1) self - ��'��� �����
#        2) Arr - ����� � ��������� ������������� �������
#        3) num - �-��� �������� � �����
#        4) seeken - �������� �������� �������� ������

#        �������: None
#    ********************************************************
#    ********************************************************


class SM:
    def __init__(self):
        self.LG=[]


    def GetLis(self):
        return self.LG


    def Linear_Search(self, Arr, num, seeken):
        Lis=[]
        itt = 0
        flag=1
        while flag == 1:
            if itt == num :
                flag = 0
            elif Arr[itt] == seeken :
                flag = 0
                Lis.append(itt)
            else:
                Lis.append(itt)
                itt+=1
        self.LG=Lis


    def Binary_Search(self, Arr, num, seeken):
        Lis= []
        posb=0
        pose=num-1
        flag=1
        while flag==1:
            if pose>=posb:
                mid = (posb+pose)//2
                if Arr[mid]==seeken:
                    Lis.append(mid)
                    flag=0
                elif Arr[mid] > seeken:
                    Lis.append(mid)
                    pose = mid-1
                else:
                    Lis.append(mid)
                    posb = mid+1
            else:
                flag=0
        self.LG=Lis


    def O_B_Search(self, Arr, num, seeken):
        Lis=[]
        b=int(num)//2
        i =b
        flag=1
        while flag==1:
            if b>0:
                if i>=num:
                    i-=b//2+1
                    b//=2
                elif i<0:
                    i+=b//2+1
                    b//=2
                elif Arr[int(i)]==seeken:
                    Lis.append(int(i))
                    flag=0
                elif Arr[int(i)]<seeken:
                    Lis.append(int(i))
                    i+=b//2+1
                    b//=2
                else:
                    Lis.append(int(i))
                    i-=b//2+1
                    b//=2
            else:
                if i<num and i>=0:
                    Lis.append(int(i))
                flag=0
        self.LG=Lis
 
     
    def Sharrah_Search(self, Arr, num, seeken):
        Lis=[]
        flag=1
        k=(math.log2(num))//1
        i=(2**k)-1
        if seeken <= Arr[int(i)]:
            b=(i+1)
            while flag==1:
                if b>0:
                    if i>=num:
                        i-=b//2+1
                        b//=2
                    elif i<0:
                        i+=b//2+1
                        b//=2
                    elif Arr[int(i)]==seeken:
                        Lis.append(int(i))
                        flag=0
                    elif Arr[int(i)]<seeken:
                        Lis.append(int(i))
                        i+=b//2+1
                        b//=2
                    else:
                        Lis.append(int(i))
                        i-=b//2+1
                        b//=2
                else:
                    if i<num and i>=0:
                        Lis.append(int(i))
                    flag=0
        else:
            l=math.log2(num-i)
            i=num-2**l
            b=2**(l)
            while flag==1:
                if b>0:
                    if i>=num:
                        i-=b//2+1
                        b//=2
                    elif i<0:
                        i+=b//2+1
                        b//=2
                    elif Arr[int(i)]==seeken:
                        Lis.append(int(i))
                        flag=0
                    elif Arr[int(i)]<seeken:
                        Lis.append(int(i))
                        i+=b//2+1
                        b//=2
                    else:
                        Lis.append(int(i))
                        i-=b//2+1
                        b//=2
                else:
                    if i<num and i>=0:
                        Lis.append(int(i))
                    flag=0
        self.LG=Lis