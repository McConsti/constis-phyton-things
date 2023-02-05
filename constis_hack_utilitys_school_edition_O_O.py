import socket
import subprocess
import os
import platform    # For getting the operating system name
import sys


print("\033[1;32m Welcome to Constis hack utilities \n")

print("--------------------------------")
print("\033[1;37m Press 1 for a response and colour test \n")
print("\033[1;37m Press 2 for a complete network scan \n")
print("\033[1;37m Press 3 [not implemeted] \n")
print("\033[1;37m Press 4 to disable net support school -_- \n")
print("\033[1;37m Press 5 for System shutdown \n")



test = int(input("INPUT>> "))
while True:
 if test == 1:
    test = 0
    print("response")
    for i in range(0, 16):
     for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
     print(u"\u001b[0m")
    test = int(input("INPUT>> "))

 if test == 2:  #Contains no 3 too
  for ping in range(1,10):
    address = "127.0.0." + str(ping)
    res = subprocess.call(['ping','-c','3', address])
    if res == 0:
        print( "ping to", address, "OK")
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")
    test = 0
    test = int(input("INPUT>> "))

    if test == 3:
     test = 0
     test = int(input("INPUT>> "))


    if test == 4:
      os.system("taskkill /f /im  Your_Process_Name.exe")
      print("what have you done..")
      test = 0
      test = int(input("INPUT>> "))

      if test == 5:
        os.system("shutdown /s /t 60 -c")