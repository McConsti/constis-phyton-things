import socket
import subprocess
import os
import platform    # For getting the operating system name
import time, sys
import webbrowser
from alive_progress import alive_bar
from datetime import datetime

print("""
\u001b[36;1m

███████╗ ██████╗██████╗ ██╗██████╗ ████████╗
██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝
███████╗██║     ██████╔╝██║██████╔╝   ██║   
╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   
███████║╚██████╗██║  ██║██║██║        ██║   
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   

~ The script edition ~

""")

print("\033[1;32m Welcome to Constis hack utilities \n")
print("--------------------------------")
print("\033[1;37m Press 1 for a response test \n")
print("\033[1;37m Press 2 to get your ip \n")
print("\033[1;37m Press 3 to taskkill N/A \n")
print("\033[1;37m Press 4 to Network scan \n")
print("\033[1;37m Press 5 for the HEV subsystem \n")


test = 0
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
        test = 0
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print(s.getsockname()[0])
        test = int(input("INPUT>> "))

 if test == 3:
       test = 0
       os.system("taskkill /f /im  Your_Process_Name.exe")  
       print("Taskkilled")
       test = int(input("INPUT>> "))


 if test == 4:
       test = 0
       net = input("Enter the IP address: ")
       net1 = net.split('.')
       a = '.'
       
       net2 = net1[0] + a + net1[1] + a + net1[2] + a
       st1 = int(input("Enter the Starting Number: "))
       en1 = int(input("Enter the Last Number: "))
       en1 = en1 + 1
       t1 = datetime.now()
       
       def scan(addr):
          s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          socket.setdefaulttimeout(1)
          result = s.connect_ex((addr,135))
          if result == 0:
             return 1
          else :
             return 0
       
       def run1():
          for ip in range(st1,en1):
             addr = net2 + str(ip)
             if (scan(addr)):
                print (addr , "is live")
                
       run1()
       t2 = datetime.now()
       total = t2 - t1
       print ("Scanning completed in: " , total)
       test = int(input("INPUT>> "))

 if test == 5:
      for total in 100, 100, 420:
          with alive_bar(total) as bar:
           for _ in range(100):
            time.sleep(.01)
            bar()
      hev = 0
      print("""
\u001b[31;1m    
██████████████████████████████████████████████
█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀▄▀░░▄▀▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░░░▄▀▄▀▄▀░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░░░▄▀░░░░███
█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█████░░░░░░█████
██████████████████████████████████████████████
\n                                                                             
""")
      print("Welcome to the HEV MK.VI")
      print("\033[1;37m")
      while True:
       hev = int(input("HEV> "))
       if hev == 1:
            print("amogus")
       
       if hev == 1:
        hev = 0
      #  for total in 100, 50, 420:
       #     with alive_bar(total) as bar:
       #      for _ in range(100):
        #      time.sleep(.01)
        #     bar()
        hev = int(input("HEV> "))

       if hev == 2:
            hev= 0
            print("""
 █████╗ ███████╗ ██████╗██╗██╗                      
██╔══██╗██╔════╝██╔════╝██║██║                      
███████║███████╗██║     ██║██║                      
██╔══██║╚════██║██║     ██║██║                      
██║  ██║███████║╚██████╗██║██║                      
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝                      
                                                    
██████╗  █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔══██╗██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
""")

       if hev == 3:
        hev = 0
        webbrowser.open('https://github.com/McConsti/test')  # Go to example.com
        hev = int(input("HEV> "))