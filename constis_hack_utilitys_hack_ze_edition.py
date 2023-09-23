import socket
import subprocess
import os
import platform    # For getting the operating system name
import time, sys
import webbrowser
import ctypes
from alive_progress import alive_bar
from datetime import datetime
from playsound import playsound


    

e = 0

os.system("taskkill /f /im  Goodbye_pc") 

print("\u001b[0m * ABOUT                   \u001b[32;1mConstis hack utilities [Hack ze world]/2.5.0")
print("\u001b[0m * LIBS                    none")
print("\u001b[0m * CPU                    \u001b[45;1m",platform.processor())
print("\u001b[0m * COMAMNDS                 bar(), ascii(), github()")
print("\u001b[0m * MULTI VERSION SELECT                        \u001b[31;1m disabled")
print("\u001b[0m * AUTO ANNOUCNMENT AND DIAGNOSTICS SYS        \u001b[31;1m disabled \n")
time.sleep(2)

input("Press enter")

print("\u001b[0m \u001b[45;1m hev \u001b[0m Hack utilites hack the world ready \u001b[34m  ver 3.0 n/a \u001b[36m Alpha 2.0")
time.sleep(0.5)
print("\u001b[0m \u001b[46;1m cpu \u001b[0m \u001b[36m use ", platform.processor() ,"implementation\u001b[32;1m AVX2")
time.sleep(0.5)
print("\u001b[0m \u001b[46;1m cpu \u001b[0m \u001b[36m use profile \u001b[44;1m hack ze world \u001b[0m \u001b[36m (7 commands)")
time.sleep(1)
print("\u001b[0m \u001b[46;1m cpu \u001b[0m \u001b[32;1m READY \u001b[0m threads \u001b[36m 3/3 (3) \u001b[0m huge pages \u001b[32;1m 100% 3/3 \u001b[0m memory \u001b[36m 12 KB")
time.sleep(1)
print("\u001b[0m \u001b[44;1m hack ze world \u001b[0m \u001b[32;1m init dataset \u001b[0m HEV (3 commands)")
time.sleep(0.5)
print("\u001b[0m \u001b[44;1m hack ze world \u001b[0m \u001b[32;1m allocated \u001b[36m 12 KB \u001b[0m ")
time.sleep(3)
print("\u001b[0m \u001b[44;1m hack ze world \u001b[0m \u001b[32;1m dataset ready")
time.sleep(1)
   
   
print("""
    \u001b[32m
     _   _            _                                         _     _ 
    | | | |          | |                                       | |   | |
    | |_| | __ _  ___| | __     _______     __      _____  _ __| | __| |
    |  _  |/ _` |/ __| |/ /    |_  / _ \    \ \ /\ / / _ \| '__| |/ _` |
    | | | | (_| | (__|   <      / /  __/     \ V  V / (_) | |  | | (_| |
    \_| |_/\__,_|\___|_|\_\    /___\___|      \_/\_/ \___/|_|  |_|\__,_|                                                                                                                                                                                             
    """)
time.sleep(1)
    
print("\u001b[35m Welcome to Constis hack utilities \n")
print("--------------------------------")
print("\033[1;37m Press 1 for a response test \n")
print("\033[1;37m Press 2 to get your ip \n")
print("\033[1;37m Press 3 to taskkill N/A \n")
print("\033[1;37m Press 4 to Network scan \n")
print("\033[1;37m Press 5 to error log (Windows only) \n")
print("\033[1;37m Press 6 for the custom error message tool (Windows only) \n")
print("\033[1;37m Press 7 to get admin access (THIS WILL RESTART THE PROGRAMM!) \n")
print("\033[1;37m Press 22 for the HEV subsystem [HEV SUBSYSTEM REMOVED] \n")
    
    
test = 0
test = int(input("""
┌──(Constis hack utilities@hack ze world)-[alpha 2.5]
└─$ """))
    
while True:
     if test == 1:
        test = 0
        print("response")
        for i in range(0, 16):
         for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
         print(u"\u001b[0m")
        test = int(input("""
┌──(Constis hack utilities@hack ze world)-[alpha 2.5]
└─$ """))
   
    
     if test == 2: 
            test = 0
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            print(s.getsockname()[0])
            test = int(input("""
┌──(Constis hack utilities@hack ze world)-[alpha 2.5]
└─$ """))
    
     if test == 3:
           test = 0
           os.system("taskkill /f /im  Your_Process_Name.exe")  
           print("Taskkilled")
           test = int(input("""
┌──(Constis hack utilities@hack ze world)-[alpha 2.5]
└─$ """))
    
    
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
           test = int(input("""
┌──(Constis hack utilities@hack ze world)-[alpha 2.5]
└─$ """))
    
     if test == 5:
         test = 0
         ctypes.windll.user32.MessageBoxW(None, u"HEllo ur system has been error logged", u"Oh uh stinky", 4)
         ctypes.windll.user32.MessageBoxW(None, u"And the worst thing is you can't escape", u"Oh uh stinky", 1)
         ctypes.windll.user32.MessageBoxW(None, u"Delete c:/Windows/System32?", u"Oh uh stinky", 3)
         ctypes.windll.user32.MessageBoxW(None, u"Ima do it anyway", u"Oh uh stinky", 1)
         ctypes.windll.user32.MessageBoxW(None, u"Goodbye", u"Oh uh stinky", 5)
         test = int(input("""
┌──(Constis hack utilities@hack ze world)-[alpha 2.5]
└─$ """))
    
     if test == 6:
        test = 0
        msgbody = "yes"
        msgtitle = "no"
        msgbody = (input('Message body>> '))
        msgtitle = (input('Message title>> '))
        ctypes.windll.user32.MessageBoxW(None, msgbody, msgtitle, 4)
        test = int(input("""
┌──(Constis hack utilities@hack ze world)-[alpha 2.5]
└─$ """))
    
     if test == 7:
         test = 0
         def is_admin():
             try:
                 return ctypes.windll.shell32.IsUserAnAdmin()
             except:
                 return False
         
         if is_admin():
             print("\u001b[0m \u001b[43m msr \u001b[0m \u001b[31;1m ADMINISRATOR ACCESS GRANTED")
         else:
             # Re-run the program with admin rights
             ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)          
         test = int(input("""
┌──(Constis hack utilities@hack ze world)-[alpha 2.5]
└─$ """))   

     if test == 22:
        print("\u001b[0m \u001b[45;1m hev \u001b[0m CRITICAL ERROR \u001b[34m  HEV LOADER FAILED \u001b[36m CODE: 22") 
     test = int(input("""
┌──(Constis hack utilities@hack ze world)-[alpha 2.5]
└─$ """))  

 
 
     def hev():
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
           hev = (input("HEV> "))
           if hev == 1:
                print("amogus")
           
           if hev == 'bar()':
            hev = 0
            for total in 100, 50, 420:
               with alive_bar(total) as bar:
                for _ in range(100):
                 time.sleep(.01)
                bar()
            hev = (input("HEV> "))
    
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
            webbrowser.open('https://github.com/McConsti/constis-phyton-things')  # Go to example.com
            hev = (input("HEV> "))          