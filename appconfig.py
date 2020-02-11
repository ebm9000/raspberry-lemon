def appconfig_xml():
    import os

    #warning: app_config.xml on your Desktop will be overwritten
    cont = str(input("Before continuing, please ensure that there is not a file called 'app_config.xml' on your desktop. It will be overwritten.\nType continue to proceed; any other input will terminate the program...\n###\n"))
    if cont.lower() != 'continue':
        print("Abort: Exiting program...\n")
        exit()

    #configuration file to be dropped (no need for a loop; exit condition above)
    #print("Enter where you would like to drop the file? (Default: Desktop)"
        #does not consider if the user changed their name (directory would not change);
        #will consider
    user = os.environ.get("USERNAME")
    cnf = open('C:\\Users\\' + user + '\\Desktop\\app_config.xml' , 'w+')
    cnf.write('<app_config>\n')

    #Line select menu
    def addLineMenu():
        appOptions = [
        ["~","~"*30,"~"*50],
        [0, "Add a new app", "(Do this first!) Defines a new appname"],
        [1, "Close the current app", "(Do this before quitting!) Writes the app-closing tag to the file"],
        [2, "max_concurrent", "Controls how many tasks from a given subproject can run at once"],
        [3, "report_results_immediately", "Immediately reports completed tasks instead of waiting for the next scheduler request"],
        [4, "fraction_done_exact", "Calculates remaining runtime soley from the percentage complete"],
        [5, "gpu_versions", "Controls how much of your GPU and CPU Graphics Card-enabled tasks can use."],      
        [58, "Exit the program (0x58 = Hex for 'X')", ""]
        ]
    
        #table formatting; to print on each return
        print('\n' + "{: <3} {: <30} {: <50}".format("#", "Flag", "Purpose"))
        for row in appOptions:
            print("{: <3} {: <30} {: <50}".format(*row))
        
        while True:
            try:
                addLine = int(input("\nSelect a flag to add: (each flag can only be added once!)\n###\n"))
                
                if addLine == int(0):
                    cont = input("\nAdd a new app name? Press 1 for yes; any other input returns to the list...\n###\n")
                    
                    if cont == '1':
                        addAppName()
                    
                    else:
                        print("Abort: Returning to menu...\n")
                        addLineMenu()

                elif addLine == int(1):
                    cont = input("\nClose the current app name? (note: run option 0 to add a new app name); Press 1 for yes; any other input returns to the list...\n###\n")
                    if cont == '1':
                        finishAppName()
                    
                    else:
                        print("Abort: Returning to menu... \n")
                        addLineMenu()

                elif addLine == int(2): 
                    cont = input("\nAdd the max_concurrent flag? Press 1 for yes; any other input returns to the list...\n###\n")
                    
                    if cont == '1':
                        max_concurrent()
                    
                    else:
                        print("Abort: Returning to menu... \n")
                        addLineMenu()
                
                elif addLine == int(3):
                    cont = input("\nAdd the report_results_immediately flag? Press 1 for yes; any other input returns to the list...\n###\n")
                    
                    if cont == '1':
                        report_results_immediately()
                    
                    else:
                        print("Abort: Returning to menu... \n")
                        addLineMenu()

                elif addLine == int(4):
                    cont = input("\nAdd the fraction_done_exact flag? Press 1 for yes; any other input returns to the list...\n###\n")
                    
                    if cont == '1':
                        fraction_done_exact()
                    
                    else:
                        print("Abort: Returning to menu... \n")
                        addLineMenu()
                
                elif addLine == int(5):
                    cont = input("\nAdd the gpu_versions flag? Press 1 for yes; any other input returns to the list...\n###\n")
                    
                    if cont == '1':
                        gpu_versions()
                    
                    else:
                        print("Abort: Returning to menu... \n")
                        addLineMenu()

                elif addLine == int(58):
                    writeEndHeader = str(input("\nWrite the ending headers? Press 1 for yes; any other input skips this step...\n###\n"))
                    if writeEndHeader == '1':
                        cnf.write('</app_config>\n')
                        print("\nEnd headers written successfully. Goodbye!\n")
                        cnf.close()
                        exit()
                    else:
                        print("End headers were NOT written. Goodbye!\n")
                        cnf.close()
                        exit()

                else:
                    print("\nError: selection not valid")
                    addLineMenu()

            except ValueError:
                print("\nError: selection not valid")
                addLineMenu()
   
    #until the next comment, the following add their respective flags:
    def addAppName():
        appName = str(input("\nEnter the app name:\n###\n"))
        cnf.write('<app>\n<name>' + str(appName) + '</name>\n')
        
        print("App name " + str(appName) + " added successfully\n")
        
        addLineMenu()

    def finishAppName():
        cnf.write("</app>\n")
        print("App closed successfully\n")
        addLineMenu()
    
    def max_concurrent():
        while True:
            try:
                x = int(input("\nEnter the maximum number of tasks you want running for this project:\n###\n"))
        
            except ValueError:
                print("Error: input must be an integer")
                max_concurrent()
            
            if x < 0:
                print("Error: value must be greater than 0")
                max_concurrent()

            elif x >= 0:
                cnf.write('<max_concurrent>' + str(x) + '</max_concurrent>\n')
                print('Added ' + str(x) + ' to max_concurrent successfully\n')
                addLineMenu()

    def report_results_immediately():
        cnf.write('<report_results_immediately/>\n')
        print('Added the report_results_immediately flag successfully\n')
        addLineMenu()

    def fraction_done_exact():
        cnf.write('<fraction_done_exact/>\n')
        print('Added fraction_done_exact successfully\n')
        addLineMenu()
    
    def gpu_versions():
        def cpu_usage():
            cpuUsage = float(input("Dedicate how much of your CPU per task?\n###\n"))
            if cpuUsage > 0 and cpuUsage <= 1:
                cnf.write('<cpu_usage>' + str(cpuUsage) + '</cpu_usage>\n')
                print('Added ' + str(cpuUsage) + ' to gpu_versions/cpu_usage successfully\n')
                gpu_usage()

            else:
                print("Error: value must be greater than 0 and less than 1")
                cpu_usage()
                                        
        def gpu_usage():
            gpuUsage = float(input("Dedicate how much of your GPU per task?\n###\n"))
            if gpuUsage > 0 and gpuUsage <= 1:
                cnf.write('<gpu_usage>' + str(gpuUsage) + '</gpu_usage>\n')
                print('Added ' + str(gpuUsage) + ' to gpu_versions/gpu_usage successfully\n')
                
                cnf.write('</gpu_versions>\n')
                print('Closed the versions flag successfully\n')
                
                addLineMenu()

            else:
                print("Error: value must be greater than 0 and less than 1")
                gpu_usage()             

        cnf.write('<gpu_versions>\n')
        cpu_usage()

    #starts the program
    addLineMenu()
            
appconfig_xml()      
