from Header import *

print("   Enter - end of line\n   Ctrl + S - end of file (after Ctrl + S enter Enter to finish writing the text)")
put("file1.txt")
a=input("\n   If you want to add to file press Y, else - press any other symbol and press Enter: ")
add("file1.txt", a)
print("\n   Full text of file 1:")
out("file1.txt")
qua=input("   Enter ammount of symbols:")
fil("file1.txt", "file2.txt", qua)
print("\n   Full text of file 2:")
out("file2.txt")