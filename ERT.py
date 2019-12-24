#######
#Estimated Time (in hours) Calculator
#######

#Variables to be run through function "timebound", where:
    #VAR[0] is the number of Days, Hours, Minutes or Seconds
    #VAR[1] are their names, so the errors can output properly
Days = [0, "Days"]
Hours = [0, "Hours"]
Mins = [0, "Minutes"]
Secs = [0, "Seconds"]

def timeinp():

    def timebound(x , y):
        if "Days" in y:
            while True:
                try:
                    x = Days[0] = int(input( str(y) + " Elapsed: "))
                
                #If a float, string etc is entered, print an error message and rerun the script
                except ValueError:
                    print("Error: " + str(y) + " value must be an integer")
                    timebound(x , y)
                
                #Explained in the elif statements (better explained w/ logic)
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
                    print("Error: " + str(y) +  " value cannot be greater than 24")
                    timebound(x , y) 
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
            

    timebound(Days[0] , Days[1])
    print(Days[0])
   
    timebound(Hours[0] , Hours[1])
    print(Hours[0])
    
    timebound(Mins[0] , Mins[1])
    print(Mins[0])
    
    timebound(Secs[0] , Secs[1])
    print(Secs[0])
timeinp()
 


#   elapsedTotal = float(elapsedHours + (elapsedMins / 60) + (elapsedSecs / 3600))
#    percentage= float(input("Enter the Task Progress as a percent: (i.e: type 23.401% as '23.401'; 0.159% as '0.159', etc) ")) / 100

#   estimatedRuntime = elapsedTotal / percentage
#    estimatedRemaining = estimatedRuntime - elapsedTotal
#    print("\n")

#    print("Estimated Total Runtime in hours: " + str(round(estimatedRuntime, 4)))
#    print("Estimated Remaining Runtime in hours: " + str(round(estimatedRemaining, 4)))



