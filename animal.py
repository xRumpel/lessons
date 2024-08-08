# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def eat(self):
        print(f"{self.name} is eating.")

# Подкласс Bird, наследующий от Animal
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} chirps.")

# Подкласс Mammal, наследующий от Animal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} roars.")

# Подкласс Reptile, наследующий от Animal
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} hisses.")

# Функция демонстрирующая полиморфизм
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Класс Zoo, использующий композицию
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the zoo.")

    def add_staff(self, staff):
        self.staff.append(staff)
        print(f"Added {staff.name} to the zoo staff.")

# Классы для сотрудников
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

# Пример использования
if __name__ == "__main__":
    # Создание животных
    parrot = Bird("Parrot", 2, "Medium")
    lion = Mammal("Lion", 5, "Golden")
    snake = Reptile("Snake", 3, "Scales")

    # Создание зоопарка
    zoo = Zoo()

    # Добавление животных в зоопарк
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    # Создание сотрудников
    keeper = ZooKeeper("John")
    vet = Veterinarian("Dr. Smith")

    # Добавление сотрудников в зоопарк
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Демонстрация полиморфизма
    animal_sound([parrot, lion, snake])

    # Действия сотрудников
    keeper.feed_animal(lion)
    vet.heal_animal(snake)