def appconfig_xml():
    import platform as plat
    import os.path
    #will os.path be in use at any point?
    
    #warning: app_config.xml on your Desktop will be overwritten
    cont = str.lower(input("Before continuing, please ensure that there is not a file called 'app_config.xml' on your desktop. It will be overwritten.\nType continue to proceed; any other input will terminate the program...\n###\n"))
    if cont.lower() != 'continue':
        print("\nAbort: Exiting program...")
        exit()

    #configuration file to be dropped
    cnf = open('C:\\Users\\Kyle\\Desktop\\app_config.xml' , 'w+')
    cnf.write('<app_config>\n<app>\n')

    #project specific options
    #implemented in the future 
    #generalOptions = [
    #    ["B", "Flags for the entire project", "~~~~~~"],
    #    [1, "project_max_concurrent", "Controls how many tasks from the entire project can run at once (useful if you run more than 1 project on a system)"],
    #    [2, "report_results_immediately", "Immediately reports completed tasks instead of waiting for the next scheduler request"],
    #]

    def addLineMenu():
        addLine = int(input("Please select a flag to add: (each flag can only be added once!)\n###\n"))

        if addLine == int(0):
            cont = input("\nDo you want to add a new App? Press 1 for yes; any other input returns to the list...\n###\n")
            if cont == '1':
                print('\n')
                appName = str(input("Enter the name of the app:\n###\n"))
                cnf.write('<name>' + str(appName) + '</name>\n')
                print("App name " + str(appName) + " added successfully\n")
                addLineMenu()
            else:
                print("Abort. Returning to menu...")
                addLineMenu()

        elif addLine == int(1):
            cont = input("\nDo you want to add the max_concurrent flag? Press 1 for yes; any other input returns to the list...\n###\n")
            if cont == '1':
                max_concurrent_line()
            else:
                print("Abort. Returning to menu... ")
                addLineMenu()
        
        elif addLine == int(2):
            cont = input("\nDo you want to add the report_results_immediately flag? Press 1 for yes; any other input returns to the list...\n###\n")
            if cont == '1':
                report_results_immediately()
            else:
                print("Abort. Returning to menu... ")
                addLineMenu()

        elif addLine == int(3):
            cont = input("\nDo you want to add fraction_done_exact flag? Press 1 for yes; any other input returns to the list...\n###\n")
            if cont == '1':
                fraction_done_exact()
            else:
                print("Abort. Returning to menu...")
                addLineMenu()
        
        elif addLine == int(4):
            cont = input("\nDo you want to add the gpu_versions flag? Press 1 for yes; any other input returns to the list...\n###\n")
            if cont == '1':
                gpu_versions()
            else:
                print("Abort. Returning to menu... ")
                addLineMenu()

        elif addLine == int(58):
            writeEndHeader = str(input("\nDo you want to write the ending headers to the file? Press 1 for yes; any other input skips this step...\n###\n"))
            if writeEndHeader == '1':
                cnf.write('</app>\n</app_config>\n')
                print("End headers written successfully. Goodbye!")
                cnf.close()
                exit()
            else:
                print("End headers were NOT written. Goodbye!")
                cnf.close()
                exit()
        
        else:
            print("Error: selection not valid\n")
            addLineMenu()
            
    def max_concurrent_line():
        while True:
            try:
                x = int(input("Enter the maximum number of tasks you want running for this project:\n###\n"))
        
            except ValueError:
                print("Error: input must be a positive integer")
                max_concurrent_line()
            
            if x < 0:
                print("Error: value must be greater than 0")
                max_concurrent_line()

            elif x >= 0:
                cnf.write('<max_concurrent>' + str(x) + '</max_concurrent>\n')
                print('Added ' + str(x) + ' to max_concurrent_line successfully ')
                addLineMenu()

    def report_results_immediately():
        cnf.write('<report_results_immediately/>\n')
        print('Added report_results_immediately successfully')
        addLineMenu()

    def fraction_done_exact():
        cnf.write('<fraction_done_exact/>\n')
        print('Added fraction_done_exact successfully')
        addLineMenu()
    
    def gpu_versions():
        def cpu_usage():
            cpuUsage = float(input("How much of your CPU do you want to dedicate per task?\n###\n"))
            if cpuUsage > 0 and cpuUsage <= 1:
                cnf.write('<cpu_usage>' + str(cpuUsage) + '</cpu_usage>\n')
                print('Added ' + str(cpuUsage) + ' to gpu_versions/cpu_usage successfully\n')
                gpu_usage()

            else:
                print("Error: value must be greater than 0 and no more than 1")
                cpu_usage()
                                        
        def gpu_usage():
            gpuUsage = float(input("How much of your GPU do you want to dedicate per task?\n###\n"))
            if gpuUsage > 0 and gpuUsage <= 1:
                cnf.write('<gpu_usage>' + str(gpuUsage) + '</gpu_usage>\n')
                print('Added ' + str(gpuUsage) + ' to gpu_versions/gpu_usage successfully\n')
                
                cnf.write('</gpu_versions>\n')
                print('Closed the versions flag successfully\n')
                
                addLineMenu()

            else:
                print("Error: value must be greater than 0 and no more than 1")
                gpu_usage()             

        cnf.write('<gpu_versions>\n')
        cpu_usage()

    appOptions = [
        ["~","~"*30,"~"*50],
        [0, "Add a new app", "Defines a new appname (do this first!)"],
        [1, "max_concurrent", "Controls how many tasks from a given subproject can run at once"],
        [2, "report_results_immediately", "Immediately reports completed tasks instead of waiting for the next scheduler request"],
        [3, "fraction_done_exact", "Calculates remaining runtime soley from the percentage complete"],
        [4, "gpu_versions", "Controls how much of your GPU and CPU Graphics Card-enabled tasks can use."],      
        [58, "Exit the program (0x58 = Hex for 'X')", ""]
        ]
    
    #table formatting; should only ever print once during the execution
    print('\n'*5, "*"*3,"*"*40,"*"*15,"*"*5)
    print("{: <3} {: <30} {: <50}".format("#", "Flag", "Purpose"))
    for row in appOptions:
        print("{: <3} {: <30} {: <50}".format(*row))
    
    #starts the program
    addLineMenu()
            
appconfig_xml()      