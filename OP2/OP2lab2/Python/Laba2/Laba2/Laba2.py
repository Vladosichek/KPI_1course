from Header import *
import pickle

que=input("====>If you want to clear file enter 1: ")
enter_f("file1.txt", que)
print("====>File 1:")
ou("file1.txt")
date=str(input("====>Today`s date (dd.mm.yyyy): "))
fil("file1.txt", "file2.txt", date)
print("====>File 2:")
ou("file2.txt")
print("====>Products produced in the last 10 days:")
ou_sp("file1.txt", date)