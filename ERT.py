#Programs:
#1: Calculate Estimated Runtime (in hours)
    #Author: EBM9000
    #Associated function: timeimp()
#2: Create app_config.xml file (?)

def programslist():
    #Includes formatting with ~ and  * characters
    programs = [
        ["1", "Calculate Estimated Runtime (in hours)", "EBM9000", "timeimp()"],
        ["2", "Create a config file for a project", "EBM9000", "createconfig()"],
        ["~"*3,"~"*40,"~"*15,"~"*5],
        ["H", "Help Document 1", "KurzedMetal", "N/A"],
        ["E", "Exit the program", "N/A", "exit"],
        ["*"*3,"*"*40,"*"*15,"*"*5]
    ]
    #Prints the header and the first set of *'s above the table (can't be in the loop)
    print("*"*3,"*"*40,"*"*15,"*"*5)
    print("{: <3} {: <40} {: <15} {: <5}".format("#", "Program Name", "Author", "Function Call"))
    
    #prints each program in the format above
    for row in programs:
        print("{: <3} {: <40} {: <15} {: <5}".format(*row))

    #Verifies that the program selection variable is reset on each return
    progSelect = 0
    progSelect = input("\nSelect a program: ")

    #Loops to determine what to execute based on the progSelect variable
    if progSelect == str(1):
        print(progSelect)
        timeinp()
    
    elif progSelect == "H" or "h":
        print(progSelect)
        print("\nI used this link to help format my columns in the program list: \nhttps://stackoverflow.com/questions/9989334/create-nice-column-output-in-python\nThanks to KurzedMetal for the post!\n")
        programslist()

    #does not currently funciton; always executes the *above* statement if a letter is entered
    elif "E" or "e" or "exit" or "Exit" or "EXIT" in progSelect:
        print(progSelect)
        print("Goodbye!")

    else:
        print(progSelect)
        print("Error: selection not valid. Try again\n")
        programslist()
    

def timeinp():
    print("\n##############\nCalculate Estimated Runtime (in hours)\nby EBM9000\n##############\n")
    
    #Variables to be run through function "timebound", where:
    #VAR[0] is the number of Days [Will add in later], Hours, Minutes or Seconds
    #VAR[1] are their names, so the errors can output properly

    Days = [0, "Days"]
    Hours = [0, "Hours"]
    Mins = [0, "Minutes"]
    Secs = [0, "Seconds"]

    def timebound(x , y):
                    
        if "Days" in y:
            while True:
                try:
                    x = Days[0] = int(input( str(y) + " Elapsed: "))
                
                except ValueError:
                    print("Error: " + str(y) + " value must be an integer")
                    timebound(x , y)
            
                #If a negative or a value over 24 is entered, run the appropriate if statement

                if x < 0:
                    print("Error: " + str(y) + " value must be positive")
                    timebound(x , y)
                
                break

        elif "Hours" in y:
            while True:
                try:
                    x = Hours[0] = int(input( str(y) + " Elapsed: "))
                
                except ValueError:
                    print("Error: " + str(y) + " value must be an integer")
                    timebound(x , y)
            
                #If a negative or a value over 24 is entered, run the appropriate if statement

                if x < 0:
                    print("Error: " + str(y) + " value must be positive")
                    timebound(x , y)
                
                elif x >= 24:
                    print("Error: " + str(y) + " value must be less than 24")
                break
        
        elif "Minutes" in y:
            while True:
                try:
                    x = Mins[0] = int(input( str(y) + " Elapsed: "))
                
                except ValueError:
                    print("Error: " + str(y) + " value must be an integer")
                    timebound(x , y)

                #If a negative or a value over 60 is entered, run the appropriate if statement

                if x < 0:
                    print("Error: " + str(y) + " value must be positive")
                    timebound(x , y)
                
                elif x >= 60:
                    print("Error: " + str(y) +  " value cannot be greater than 59")
                    timebound(x , y)
                
                break   
        
        elif "Seconds" in y:
            while True:
                try:
                    x = Secs[0] = int(input( str(y) + " Elapsed: "))
                    
                except ValueError:
                    print("Error: " + str(y) + " value must be an integer")
                    timebound(x , y)

                #If a negative or a value over 60 is entered, run the appropriate if statement

                if x < 0:
                    print("Error: " + str(y) + " value must be positive")
                    timebound(x , y)
                
                elif x >= 60:
                    print("Error: " + str(y) +  " value cannot be greater than 59")
                    timebound(x , y)
                break

    #Incorrect results here!:       
    def statistics():
        #Defining stats variables
        percentage= 0.01 * float(input("Enter the Task Progress as a percent (enter as is and omit the o/o sign): "))
        totalinHours = float((24*Days[0] + Hours[0]) + (Mins[0] / 60) + (Secs[0] / 3600))  

        #Executing calculations
        estimatedRuntime = totalinHours / percentage
        estimatedRemaining = estimatedRuntime - totalinHours

        #Printing Results
        print("\nEstimated Remaining Runtime in hours: " + str(round(estimatedRemaining, 4)))
        print("Estimated Total Runtime in hours: " + str(round(estimatedRuntime, 4)))
        
    timebound(Days[0] , Days[1])
    timebound(Hours[0] , Hours[1])
    timebound(Mins[0] , Mins[1])
    timebound(Secs[0] , Secs[1])
    statistics()
    input("Execution complete. Press Enter to exit...")

print("##############\nBoinc Pack\nby EBM9000\n##############\n")
programslist()

