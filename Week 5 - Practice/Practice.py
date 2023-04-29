# Practice 1 make simple game hero
# class Hero:
class Hero :
    def __init__(self, name, health, attackPower, armorNumber): # constructor
        self.name = name # instance variable
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan): # method
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackPower)
    
    def diserang(self, lawan, attackPowerLawan): # method
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPowerLawan/self.armorNumber
        print('serangan terasa : ' + str(attack_diterima))
        self.health -= attack_diterima  
        print('darah ' + self.name + ' tersisa ' + str(self.health))

sniper = Hero('sniper', 100, 10, 5)
rikimaru = Hero('rikimaru', 100, 20, 10)

sniper.serang(rikimaru)
print('\n')
rikimaru.serang(sniper)
