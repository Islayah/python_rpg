class Character:
    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        enemy.health -= self.power

    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))

class Hero(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power    

class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power

    # Can this be changed?
    def print_status(self):
        print("Algus has %d health and %d power." % (self.health, self.power))

class Zombie(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def alive(self):
        return True

    def print_status(self):
        print("Zalbag has %d health and %d power." % (self.health, self.power))

ramza = Hero(10, 5)
algus = Goblin(6, 2)
zalbag = Zombie(1, 1)
        
def main():

    while algus.alive() and ramza.alive() and zalbag.alive():
        ramza.print_status()
        algus.print_status()
        zalbag.print_status()
        print()
        print("What do you want to do?")
        print("1. fight algus")
        print("2. fight zalbag")
        print("3. do nothing")
        print("4. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            ramza.attack(algus)
            print("You do %d damage to Algus." % ramza.power)
            if algus.health <= 0:
                print("Algus is dead.")
        elif user_input == "2":
            ramza.attack(zalbag)
            print("You do %d damage to Zalbag." % ramza.power)
            if zalbag.health <= 0:
                print("Zalbag is dead.")        
        elif user_input == "3":
            pass
        elif user_input == "4":
            print("Valhalla will never accept you.")
            break
        else:
            print("Invalid input %r" % user_input)

        if algus.health > 0:
            # Goblin attacks hero
            algus.attack(ramza)
            print("Algus does %d damage to you." % algus.power)
            if ramza.health <= 0:
                print("You are dead.")

        if zalbag.health > 0:
            zalbag.attack(ramza)
            print("Zalbag does %d damage to you." % zalbag.power)
            if ramza.health <= 0:
                print("You dead.")
main()