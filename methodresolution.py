#Example 1: Multi-role Employee System
class Employee:
    def work(self):
        print("Employee is working.")

class Manager(Employee):
    def work(self):
        print("Manager is planning the project.")

class Engineer(Employee):
    def work(self):
        print("Engineer is writing code.")

class TechLead(Manager, Engineer):
    pass

lead = TechLead()
lead.work()  # Which work() is used?

# Show MRO
print("\nMethod Resolution Order:")
for cls in TechLead.__mro__:
    print(cls)




print('...........................................................................')
print('...........................................................................')


#Example 2: Vehicle System
class Vehicle:
    def fuel_type(self):
        print("General vehicle fuel.")

class ElectricVehicle(Vehicle):
    def fuel_type(self):
        print("Electricity powered.")

class GasolineVehicle(Vehicle):
    def fuel_type(self):
        print("Gasoline powered.")

class HybridCar(ElectricVehicle, GasolineVehicle):
    pass

car = HybridCar()
car.fuel_type()  # Which method is used?

# Show MRO
print("\nMethod Resolution Order:")
for cls in HybridCar.__mro__:
    print(cls)
