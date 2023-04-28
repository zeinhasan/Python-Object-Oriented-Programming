class Hero: # template
    pass

hero1 = Hero() # object / instance (instansiate)
hero2 = Hero() # object / instance (instansiate)
hero3 = Hero() # object / instance (instansiate)

hero1.name = "Sniper"   # add attribute
hero1.health = 100      # add attribute

hero2.name = "Sven"     # add attribute
hero2.health = 200      # add attribute

hero3.name = "Superman" # add attribute
hero3.health = 1000     # add attribute


print(hero1)
print(hero1.__dict__)
print("hero1 name:", hero1.name)
print("hero1 health:", hero1.health)
print('\n')
print(hero2)
print(hero2.__dict__)
print("hero2 name:", hero2.name)
print("hero2 health:", hero2.health)
