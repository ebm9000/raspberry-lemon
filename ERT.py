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
    exit()

timeinp()
