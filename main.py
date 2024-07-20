from abc import ABC, abstractmethod

class Fighter():
    def __init__(self, weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon):
        self.weapon = weapon
        print(f"Боец выбирает {self.weapon}")

    def fight(self):
        print(self.weapon.attack())
        print("Монстр побежден!")


class Monster():
    pass

class Weapon(ABC):
    @abstractmethod
    def attack(self, weapon):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец делает выстрел из лука."

s = Sword()
b = Bow()

fighter = Fighter(s)
monster = Monster()

fighter.changeWeapon(s)
fighter.fight()

fighter.changeWeapon(b)
fighter.fight()

