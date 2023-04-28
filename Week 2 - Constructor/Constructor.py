class Hero: # template
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
    
hero1 = Hero("Sniper", 100, 10, 4) # object / instance (instansiate)
hero2 = Hero("Sven", 200, 5, 10) # object / instance (instansiate)
hero3 = Hero("Superman", 1000, 100, 0) # object / instance (instansiate)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
print('\n')
print("hero1 name:", hero1.name)
print("hero1 health:", hero1.health)
print("hero1 power:", hero1.power)
print("hero1 armor:", hero1.armor)
print('\n')
print("hero2 name:", hero2.name)
print("hero2 health:", hero2.health)
print("hero2 power:", hero2.power)
print("hero2 armor:", hero2.armor)
print('\n')
print("hero3 name:", hero3.name)
print("hero3 health:", hero3.health)
print("hero3 power:", hero3.power)
print("hero3 armor:", hero3.armor)
print('\n')

# __init__ is a constructor
# __init__ is a method that is automatically called when creating an object
# __init__ is a method to initialize the value of the object's properties
# __init__ is a method that is called when the object is created
