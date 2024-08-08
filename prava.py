class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    # Getters
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Setters
    def set_name(self, name):
        self._name = name

    def set_access_level(self, access_level):
        self._access_level = access_level


class Admin(User):
    def __init__(self, user_id, name, access_level='admin'):
        super().__init__(user_id, name, access_level)
        self._admin_access_level = access_level

    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f'User {user.get_name()} added successfully.')
        else:
            print('Invalid user. Cannot add to the list.')

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f'User {user.get_name()} removed successfully.')
                return
        print('User not found. Cannot remove from the list.')


# Пример использования
if __name__ == "__main__":
    # Создание списка пользователей
    users = []

    # Создание экземпляров пользователей
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")

    # Создание экземпляра администратора
    admin = Admin(3, "Charlie")

    # Администратор добавляет пользователей в систему
    admin.add_user(users, user1)
    admin.add_user(users, user2)

    # Проверка списка пользователей
    for user in users:
        print(f'User ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}')

    # Администратор удаляет пользователя из системы
    admin.remove_user(users, 1)

    # Проверка списка пользователей после удаления
    for user in users:
        print(f'User ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}')