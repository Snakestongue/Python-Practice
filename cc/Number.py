#This is a variable. The format is variable_name = value
#The variable_name can be anything you like (keep it descriptive) 
#The value can be a String (words), int (whole number) or float (decimal numbers)
number = 11

#A while loop continues until a condition is met. 
#In a while True loop the code will continue forever until "break" is used.
while True:

    #This takes input and assigns into to the guess variable
    #int is typecasting which allows for numbers to be compared or have operations done too
    guess = int(input("Enter a number: "))

    #This is a conditional statment. 
    #In this case if guess is larger then a number, it will print something and continue the while loop.
    #If guess is not larger than the number, it will not print "Your number was too large! "
    if guess>number:
        print("Your number was too large! ")
        continue
    
    #This is the same thing but only happens if the first statement is false.
    elif guess<number:
        print("Your number was too small! ")
        continue
    
    #If a number is not greater then or less then the actual number, it must be exactly the number we were trying to guess
    #You can also use elif guess==number, however it's extra code.
    else:
        print("You guessed correctly!")

        #Break will end the code
        break




    