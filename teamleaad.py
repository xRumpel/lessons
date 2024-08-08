import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")
        print(f"У {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра началась!")
        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)
            turn += 1

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    player = Hero(name=player_name)
    computer = Hero(name="Компьютер", attack_power=random.randint(15, 25))

    game = Game(player=player, computer=computer)
    game.start()
