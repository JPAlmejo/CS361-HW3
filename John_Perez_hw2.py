#Maker: John Perez Almejo
#Date: 1-11-2021
#Program Purpose: To tell the user if their chosen year is a leap year
#run the program using visual studio code. Enter a year when prompted by the terminal and then press enter. Once you press enter it should tell you if its a leap year or not. Can also run in a python terminal found on google.
try:
    year = int(input("enter a year: "))


    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(year, "is a leap year".format(year))
            else:
                print(year, "is not a leap year".format(year))
        else:
            print(year, "is a leap year".format(year))
    else:
        print(year, "is not a leap year".format(year))

except ValueError:
    print("only digits are allowed!")