from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "slashes with the sword"

class Bow(Weapon):
    def attack(self):
        return "shoots an arrow from the bow"

class Axe(Weapon):
    def attack(self):
        return "chops with the axe"

# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} chooses {weapon.__class__.__name__}.")

    def attack(self, monster):
        if self.weapon:
            attack_result = self.weapon.attack()
            print(f"{self.name} {attack_result}.")
            monster.take_damage()
        else:
            print(f"{self.name} has no weapon to attack with.")

# Класс Monster
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            print(f"{self.name} is defeated!")
        else:
            print(f"{self.name} has {self.health} health left.")

# Шаг 4: Реализация боя
if __name__ == "__main__":
    # Создание бойца и монстра
    fighter = Fighter("Hero")
    monster = Monster("Orc", 2)

    # Боец выбирает меч и атакует
    sword = Sword()
    fighter.change_weapon(sword)
    fighter.attack(monster)

    # Боец выбирает лук и атакует
    bow = Bow()
    fighter.change_weapon(bow)
    fighter.attack(monster)

    # Добавление нового типа оружия (топор) и атака
    axe = Axe()
    fighter.change_weapon(axe)
    fighter.attack(monster)