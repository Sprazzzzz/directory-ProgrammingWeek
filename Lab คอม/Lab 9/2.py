class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def show_status(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack Power: {self.attack_power}")

class Warrior(Character):
    def __init__(self, name, health, attack_power, weapon):
        super().__init__(name, health, attack_power)
        self.weapon = weapon

    def show_status(self):
        super().show_status()
        print(f"Weapon: {self.weapon}")

class Mage(Character):
    def __init__(self, name, health, attack_power, mana, spell):
        super().__init__(name, health, attack_power)
        self.mana = mana
        self.spell = spell

    def show_status(self):
        super().show_status()
        print(f"Mana: {self.mana}")
        print(f"Spell: {self.spell}")

person1 = Warrior("Beam", 150, 30, "sword")
person2 = Mage("John", 100, 20, 80, "Fireball")

person1.show_status()
person2.show_status()

