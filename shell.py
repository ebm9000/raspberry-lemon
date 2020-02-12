from os import system as system
from os import startfile as startfile

progList = [
    [1, "Boinc Manager", "C:\\Program Files\\BOINC\\boincmgr.exe"],
    [2, "Command Prompt", "cmd"],
    [3, "Control Panel", "control"],
    [4, "Internet Explorer", "iexplore"],
    [5, "Restart", "shutdown -r -t 0"],
    [6, "Shutdown", "shutdown -s -t 0"],
    [7, "Snake!", "snake"],
    [8, "Task Manager", "taskmgr"],
    [9, "Windows Explorer", "explorer C:\\"],
    ["~","~"*10,"~"*10],
    [10, "Blackjack (WIP)", "C:\Windows\BlackJack.py"],
    [11, "ERT Calculator", "C:\Windows\ERT.py"],
    [12, "Python Editor", "C:\Program Files\Python\Lib\idlelib\idle.bat"]
    
]

def clear():
    system('cls')

def restartPy():
    clear()
    system('"C:\\Program Files\\Python\\python.exe" C:\\Users\\Administrator\\Desktop\\Script.py')
       
def launch(x):
    print("Please wait...\n")
    startfile(x)
    clear()
    select()

def launch2(x):
    print("Please wait...\n")
    system(x)
    clear()
    select()

def select():

    for row in progList:
        print(str(row[0]) + ' '*5 + str(row[1]))
        
    while True:
        try:
            select = input("\nSelect a program: ")
        
        except ValueError:
            print("Invalid argument. Try again.\n")
            select()

        except FileNotFoundError:
            print("File not found. Try again.\n")
            select()

        except (KeyboardInterrupt, SystemExit):
            restartPy()

        if select == '1':
            #os.startfile("D:\\BOINC\P\\boincmgr.exe")
            launch(progList[0][2])

        elif select == '2':
            launch(progList[1][2])
        
        elif select == '3':
            launch(progList[2][2])
        
        elif select == '4':
            launch(progList[3][2])
        
        elif select == '5':
            while True:
                try:
                    restart = int(input("Warning: This will immediately restart your computer. Type 1 to continue or any other input to abort... "))
                except ValueError:
                    print("Abort!\n")
                    restartPy()
                if restart == int(1):
                    launch2(progList[4][2])
                else:
                    print("Abort!\n")
                    restartPy()
        
        elif select == '6':
            while True:
                try:
                    shutdown = int(input("Warning: This will immediately restart your computer. Type 1 to continue or any other input to abort... "))
                except ValueError:
                    print("Abort!\n")
                    restartPy()
                if shutdown == int(1):
                    launch2(progList[5][2])
                else:
                    print("Abort!\n")
                    restartPy()
        
        elif select == '7':
            launch2(progList[6][2])
            restartPy()
        
        elif select == '8':
            launch2(progList[7][2])
            restartPy()

        elif select == '9':
            launch2(progList[8][2])
        
        elif select == '10':
            launch(progList[10][2])

        elif select == '11':
            launch(progList[11][2])

        elif select == '12':
            launch(progList[12][2])
select()
