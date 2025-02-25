#A class to define the vehicle class, make, and model.
class Vehicle:
  #Define constructor for the Vehicle class with optional parameters.
  def __init__(self, make="", model=""):
    self.make = make
    self.model = model

  #Set make attribute
  def set_make(self, make):
    self.make = make

  #Set model attribute
  def set_model(self, model):
    self.model = model

  #Method to get make attribute.
  def get_make(self):
    return self.make

  #Method to get model attribute.
  def get_model(self):
    return self.model


#Child class of vehicle called car.
class Car(Vehicle):
  #Define constructor for car class with optional parameters.
  def __init__(self, make="", model="", doors=0):
    #Call vehicle class with make and model parameters.
    super().__init__(make, model)
    #Set objects door attribute to door parameter.
    self.doors = doors

  #Set door attribute.
  def set_doors(self, doors):
    self.doors = doors

  #Get door attribute.
  def get_doors(self):
    return self.doors


#Child class of vehicle called truck.
class Truck(Vehicle):
  #Define constructor for truck class with optional parameters.
  def __init__(self, make="", model="", bed_length=0):
    #Call vehicle class with make and model parameters.
    super().__init__(make, model)
    #Set bed length attribute.
    self.bed_length = bed_length

  #Set bed length attribute.
  def set_bed_length(self, bed_length):
    self.bed_length = bed_length

  #Get bed length attribute.
  def get_bed_length(self):
    return self.bed_length


#Define a function to create a new car.
def create_car():
  #Prompt user to enter a make for the car.
  make = input("Enter car make: ")
  #Prompt user to enter a model for the car.
  model = input("Enter car model: ")
  #Prompt user to enter the number of doors the car has.
  doors = int(input("Enter number of doors: "))
  car = Car(make, model, doors)
  return car


#Define a function to create a new truck.
def create_truck():
  #Prompt the user to enter a make for the truck.
  make = input("Enter truck make: ")
  #Prompt the user to enter a model for the truck.
  model = input("Enter truck model: ")
  #Prompt the user to enter the bed length of the truck.
  bed_length = int(input("Enter bed length: "))
  truck = Truck(make, model, bed_length)
  return truck


#Define a function to print a list of all vehicles inputed.
def print_vehicle_list(vehicles):
  #If no vehicles in garage print "No vehicles in garage".
  if len(vehicles) == 0:
    print("No vehicles in the garage")
  else:
    #Print garage contents that user has entered.
    print("Garage contents:")
    for i, vehicle in enumerate(vehicles):
      #Return user input for car in garage.
      if isinstance(vehicle, Car):
        vehicle_type = "Car"
        attribute = "doors"
        value = vehicle.get_doors()
      #Return user input for truck in garage.
      elif isinstance(vehicle, Truck):
        vehicle_type = "Truck"
        attribute = "bed length"
        value = vehicle.get_bed_length()
      #Print cars and trucks entered by user.
      print(
        f"{vehicle_type}: {vehicle.get_make()} {vehicle.get_model()}, {attribute}: {value}"
      )


#Define a main function to add, list, view vehicles and quit program.
def main():
  vehicles = []
  while True:
    #Prompts for user selection.
    print("1. Add a car")
    print("2. Add a truck")
    print("3. List vehicles in garage")
    print("4. Quit")
    choice = int(input("Enter your choice: "))
    #If 1 create car object.
    if choice == 1:
      car = create_car()
      vehicles.append(car)
    #If 2 create truck object.
    elif choice == 2:
      truck = create_truck()
      vehicles.append(truck)
    #If 3 print out entered vehicles or error.
    elif choice == 3:
      print_vehicle_list(vehicles)
    #If 4 quit program.
    elif choice == 4:
      break
    #If a number not listed is chosen print invalid choice.
    else:
      print("Invalid choice")
  #If number 4 is chosen print extiting program.
  print("Exiting program")


if __name__ == "__main__":
  main()
#Continue program until number 4.