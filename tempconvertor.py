#input temprature 
temp = int(input("What is the Temprature : "))

#unit input 
unit = str(input("What is the Unit (C) or (F) : "))

#condition 
if unit == "C" : 
    converted = temp*2
    print("Temp in F : ", str(converted))
else:
    converted = temp*3
    print("Temp in C : ",str(converted))



        

