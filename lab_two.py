"""This program is to go through and generate a password as well as math calculations"""

#import utilities
import datetime
import string
import secrets
from ast import literal_eval
import math
import sys

#function to generate the random password with as many hexadecimal characters as needed
def password():
    """This function is used to generate a random password with the needed parameters."""
    digits = literal_eval(input("How many characters are needed?: \n"))
    lower_case = input("Enter y for the need of lower case, n if you do not need lower case: \n")
    upper_case = input("Enter y for the need of upper case, n if you do not need upper case: \n")
    special_character = input("Enter y for the need of special character, n if you do not need "
                              "special character: \n")

    if lower_case.lower == " y" and upper_case.lower == "y" and \
        special_character.lower == "y":
        password_created = secrets.token_bytes(digits)
    elif lower_case.lower == "y" and upper_case.lower == "y" and special_character.lower == "n":
        password_created = secrets.token_hex(digits)
    elif lower_case.lower == "n" and upper_case.lower == "n" and special_character.lower == "y":
        password_created = secrets.randbelow(100)
    else:
        password_created = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase
                                                  + string.ascii_lowercase) for i in range(digits))

    print("Your new password is " + password_created)


#function tp calculate and format percentage
def percentage():
    """using a numerator and denomiator, a percentage is calculated and formatted."""
    numerator = literal_eval(input("What is the numerator?: \n"))
    denominator = literal_eval(input("What is the denominator?: \n"))
    decimal_points = literal_eval(input("How many decimal points do you want?: \n"))

    calculated_percentage = (numerator/denominator) * 100
    formatted_percentage = f"{calculated_percentage:.{decimal_points}f}"

    print("The percentage is: " + formatted_percentage + "%")



#function to calculate the amount of days from today to Jul 4, 2025
def days_until():
    """This function is calculating the amount of days from the current day to July 4, 2025"""
    today = datetime.date.today()
    july_date = datetime.date(2025, 7, 4)
    current = july_date - today
    current_days = str(current.days)

    print("There are currently " + current_days + " until July 4, 2025")

#function to calculate the leg of a triangle using law of cosines
def triangle():
    """This function uses the law of cosines, broken down by steps,
    to calculate the leg of a triangle"""
    side_one = literal_eval(input("Input the first side's length: \n"))
    side_one_squared = side_one * side_one
    side_two = literal_eval(input("Input the second Side's length: \n"))
    side_two_squared = side_two * side_two
    angle = literal_eval(input("Input the angle: \n"))
    angle_radians = math.radians(angle)

    law = str(math.sqrt(side_one_squared + side_two_squared -
                        (2 * side_one * side_two * math.cos(angle_radians))))

    print("The third leg's length is " + law)


#function to calculate the volume of a right circular cylinder
def volume():
    """The steps to calculate the volume of a right circular cylinder are broken
    down and calculated."""
    radius = literal_eval(input("What is the radius of the cylinder?: \n"))
    height = literal_eval(input("What is the height of the cylinder? \n"))
    radius_square = radius * radius
    calculated_volume = str(math.pi * radius_square * height)
    print("The volume is: " + calculated_volume)

#function for exiting the program
def exit_program():
    """This function is to exit the program"""
    print("Thank you for using our program!")
    sys.exit(0)



#function for the menu and running the options
def menu():
    """This function is to display the menu associated with the functions to run"""
    print("Option 1: Generate a secure password")
    print("Option 2: Calculate and Format a Percentage")
    print("Option 3: Calculate how many days until July 4, 2025")
    print("Option 4: Calculate the leg of a triangle using the Law of Cosines")
    print("Option 5: Calculate the volume of a right circular cylinder")
    print("Option 0: Exit")




CHOICE = None
while CHOICE != 0:
    menu()

    CHOICE = input("Please select a menu choice: \n")

    if CHOICE == "1":
        password()
    elif CHOICE == "2":
        percentage()
    elif CHOICE == "3":
        days_until()
    elif CHOICE == "4":
        triangle()
    elif CHOICE == "5":
        volume()
    elif CHOICE == "0":
        exit_program()
    else:
        print("Please make a valid choice")
