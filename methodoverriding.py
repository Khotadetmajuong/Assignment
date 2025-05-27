3 #Method Overriding Employee Salary System
# Parent class
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        print(f"Calculating salary for {self.name} (generic employee).")

# Child class: Full-time employee
class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        print(f"{self.name}'s monthly salary is ${self.monthly_salary}.")

# Child class: Part-time employee
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        salary = self.hourly_rate * self.hours_worked
        print(f"{self.name}'s part-time salary is ${salary} (${self.hourly_rate}/hr for {self.hours_worked} hours).")
        print('...........................................................................')
        print('...........................................................................')
        

# Usage
e1 = FullTimeEmployee("Alice", 5000)
e2 = PartTimeEmployee("Bob", 20, 80)

e1.calculate_salary()  # Overridden method in FullTimeEmployee
e2.calculate_salary()  # Overridden method in PartTimeEmployee




#Method Overriding Example 2:  Animal Sound System
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes a generic sound.")

# Subclass: Dog
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says: Woof!")

# Subclass: Cat
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow!")

# Subclass: Cow
class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says: Moo!")

# Usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

dog.make_sound()
cat.make_sound()
cow.make_sound()
