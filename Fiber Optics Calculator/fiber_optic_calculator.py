#Display welcome message
print("Welcome to the Fiber Optic Cable cost calculator.")

#Prompt user for company name
company_name = input("Please enter your Company Name: ")

#Prompt user for the amount of cable needed in feet & change feet_of_cable to float variable
feet_of_cable = float(input("Please enter the amount of cable needed in feet: "))

#Calculate the total cost based on amount of cable needed
#If amount of cable needed is 100 feet or less then $0.87/foot
if feet_of_cable <= 100:
  total_cost = feet_of_cable * .87

#If amount of cable needed is between 101 feet and 250 feet then $0.80/foot
elif feet_of_cable > 100 and feet_of_cable <= 250:
  total_cost = feet_of_cable * .80

#If amount of cable needed is between 251 feet and 500 feet then $0.70/foot
elif feet_of_cable > 250 and feet_of_cable <= 500:
  total_cost = feet_of_cable * .70

#If amount of cable need is more than 500 feet then $0.50/foot
else: 
  total_cost = feet_of_cable * .50
  
#Format the total cost as a string with two decimal places
total_cost_formatted = "{:.2f}".format(total_cost)

#Set message with total_cost_formatted float to a string variable and retrieve company_name
message = "The total cost is $" + str(total_cost_formatted) + " for " + (company_name)

#Print message with total_cost and company_name
print(message)
#Program terminates