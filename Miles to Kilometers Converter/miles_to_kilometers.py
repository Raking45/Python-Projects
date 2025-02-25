#Robert King
#Assignment 6.1
#CIS245-T305
#April 22, 2023
#Description: A program that converts miles to kilometers and displays
#the output as number of miles is equivalent to number of kilometers. 
#The program will repeat until user types in "q".

# The main function that runs the program.
def main():
    # Display the introductory screen.
    intro()

    # Continue loop until the user quits.
    while True:
        # Get the number of miles (with input validation).
        while True:
            try:
                miles_driven = input("Enter the number of miles driven (q to quit): ")
                # Check if user wants to quit.
                if miles_driven.lower() == 'q':
                    # Terminate the program
                    return
                # Convert user input to a float.
                miles_driven = float(miles_driven)
                # Check if input is positive.
                if miles_driven < 0:
                    raise ValueError
                # Break out of the loop if user input is valid.
                break
            except ValueError:
                # Display an error message for invalid user input.
                print("Please enter a positive number for the number of miles driven, or q to quit.")

        # Convert the miles to kilometers.
        kilometers_driven = miles_to_kilometers(miles_driven)

        # Display the converted value.
        print(f"{miles_driven} miles is equivalent to {kilometers_driven} kilometers.")

# The intro function displays an introductory screen that displays all information to user.
def intro():
    print("This program converts measurements")
    print("from miles to kilometers. For your")
    print("reference the formula is:")
    print("1 mile = 1.60934 kilometers.")
    print()

# The miles_to_kilometers function accepts a number of
# miles and returns the equivalent number of kilometers.
def miles_to_kilometers(miles):
    # Convert miles to kilometers using formula 1 mile = 1.60934 kilometers.
    kilometers = miles * 1.60934
    # Return the converted value in kilometers.
    return kilometers

# Call the main function to continue the program until user terminates.
main()
