class Hero: # template
    # class variable
    jumlahHero = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlahHero += 1
        print("Membuat Hero dengan nama " + inputName)

    # void function, method without return
    def siapa(self):
        print("Namaku adalah " + self.name)

    # method with argument
    def healthUp(self, up):
        self.health += up

    # method with return
    def getHealth(self):
        return self.health


hero1 = Hero("Sniper", 100, 10, 4) # object / instance (instansiate)
print(Hero.jumlahHero)
hero2 = Hero("Sven", 200, 5, 10) # object / instance (instansiate)
print(Hero.jumlahHero)

print('\n')
print(hero1.__dict__)
print(hero2.__dict__)

print('\n')
hero1.siapa()

print('\n')
hero1.healthUp(10)
print(hero1.health)

print('\n')
print(hero1.getHealth())
