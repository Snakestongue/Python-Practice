#This is a comment. Comments are ignored by the interperter. They are simply notes for you or others to understand your code.

#This is an input line. This prompts the user to type something into the terminal.
# In this case we want the user to input in, cm, mi or km. Whatever they input will be assigned to the unit variable
#.lower() is a method in which whatever the user types in will be converted to lowercase letters for the rest of the code. 

unit = input("Enter your unit of measurment (in, cm, mi, km): ").lower() 

#This is a while loop. 
#This code is basically saying if unit is not one of the four accepted values (in, cm, mi or km) it will state Invalid and prompt you to try again
while unit != "in" and unit != "cm" and unit != "mi" and unit != "km":
    print("Invalid. Try again.")
    unit = input("Enter your unit of measurment (in, cm, mi, km)").lower()

#Once your input passes the check you will be prompted to state how much of your desired unit you have.
amount = float(input("Enter amount: "))

#These are measurements for each unit conversion
inToCm = 2.54
cmToIn = 0.39
milesToKm = 1.61
kmToMiles = 0.62

#Factor is the variable used for out function(def). This will be set to one of the four measurments above in the if statements below.
factor = 0

#This is a function. A function is used to make code readable and more organized. 
def convert(amount, factor): #amount, factor are parameters. A Parameter is a variable that is needed for the function to perform a task using these values.
    return amount * factor #Return, returns or sends back the amount * factor. We DO NOT use print because we don't want anything on the console just yet. We need the values later.


#This is an if statement. This checks if out unit (in, cm, mi or km) is selected then it will perform a series of actions.
if unit == "in":
    #This sets factor to inToCm so now factor is equal to 2.54(declared above at inToCm). We use factor in out function therefore it must be equal to one of the conversion values
    factor = inToCm
    print(f"{amount} inches is equal to {convert(amount, factor)} centimeters") 
    #This is when we print out answer(above). An f string is basically an easy way to combine variables and words together. Any variables or function used is placed in curly braces!
    #The rest of the code repeats this layout. An elif statement is if the if statement is false it moves down into the code and checks each unit.
elif unit == "cm":
    factor = cmToIn
    print(f"{amount} centimeters is equal to {convert(amount, factor)} inches")
elif unit == "mi":
    factor = milesToKm
    print(f"{amount} miles is equal to {convert(amount, factor)} kilometers")
elif unit == "km":
    factor = kmToMiles
    print(f"{amount} kilometers is equal to {convert(amount, factor)} miles")
#This is an else statement. If none of the if/elif statements worked something is wrong with the input and we will say Invalid Input. 
# This piece of code IS NO LONGER NEEDED because we have a while loop in place already to check units.
else:
    print("Invalid unit. Try Again.")