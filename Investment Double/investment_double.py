#Name: Robert King
#Assignment: Week 5
#Date: April 15, 2023
#Description: Program determines how long it will take for an 
#initial investment to double with a give interest rate that is
#compounded annually.

#Prompt user for initial investment amount in decimal format of US Dollars and Cents.
initial_investment = float(input("Enter initial amount of investment (Dollars and Cents): "))

#Promt user to enter the interest rate percentage in decimal format.
interest_rate = float(input("Enter annual interest rate (as a decimal): "))

#Initialize the variables for years and balance.
years = 0
balance = initial_investment

#Print the header for the output table. 
print("Year\tBalance")
print("----\t-------")

#Continue compounding interest annually until the balance is at least double initial investment.
while balance < 2 * initial_investment:
  
    #Increment the years counter by 1.
    years += 1
  
    #Calculate interest of current year as balance * interest rate.
    interest = balance * interest_rate
  
    #Add the calculated interest earned to the balance.
    balance += interest
  
    #Print the current year and balance with two decimal places and a dollar sign.
    print("{}\t${:.2f}".format(years, balance))
  
#Print message indication how many years it will take for the initial investment to double.
print("It will take {} years for the initial investment to double.".format(years))
#Terminate Program