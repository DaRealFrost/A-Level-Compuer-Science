#Determines Wall Count
Wall_Count = int(input("Enter the total amount of walls you will be painting: "))

#Main Variables
Temp_Wall_Count = Wall_Count
Temp_Area = 0
Temp_Liters = 0


#Calculates the area of the walls parsed in the function
def Calculate_Area(Temp_Area,Wall_Identifier,Width,Height,Tmp_Unusable_Area):
    #print("Wall ",Wall_Identifier," has a paintable area of: ",(Width*Height)-Tmp_Unusable_Area)
     return((Width*Height)-Tmp_Unusable_Area)


#Calculates the amount of buckets needed to paint room
def Calculate_Paint(Usable_Area):
    return(float(Usable_Area/11))

#Loops the amount of walls entered
for i in range(Wall_Count):    
    #Paint area
    Tmp_Width = int(input("Enter the width of wall "+str(Temp_Wall_Count)+": "))
    Tmp_Height = int(input("Enter the height of wall "+str(Temp_Wall_Count)+": "))
    #No Paint Area
    Tmp_Unusable_Area = int(input("Enter the area of wall "+str(Temp_Wall_Count)+" that is unusable: "))
    #Calculate
    Temp_Area = (Temp_Area + Calculate_Area(Temp_Area,Temp_Wall_Count,Tmp_Width,Tmp_Height,Tmp_Unusable_Area))
    #Add to the count
    Temp_Wall_Count = Temp_Wall_Count - 1

#Prints the Result
print(Calculate_Paint(Temp_Area))
