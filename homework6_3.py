class UserManager:
    """
    Клас UserManager використовується для керування списком користувачів.
    """

    def __init__(self):
        """
        Ініціалізує порожній список користувачів.
        """
        self.users = []

    def add_user(self, name: str, age: int):
        """
        Додає користувача до списку.
        """
        self.users.append({'name': name, 'age': age})

    def remove_user(self, name: str):
        """
        Видаляє користувача зі списку за його іменем.
        """
        self.users = [user for user in self.users if user['name'] != name]

    def get_all_users(self) -> list:
        """
        Повертає список всіх користувачів.
        """
        return self.users


import pytest

@pytest.fixture
def user_manager():
    """
    Фікстура для створення екземпляра UserManager з доданими тестовими користувачами.
    """
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    return um

# Тести для UserManager
def test_add_user(user_manager):
    """
    Тестуємо метод add_user. Перевіряємо, чи додано нового користувача до списку.
    """
    user_manager.add_user("Charlie", 20)
    users = user_manager.get_all_users()
    assert len(users) == 3
    assert users[-1] == {'name': 'Charlie', 'age': 20}

def test_remove_user(user_manager):
    """
    Тестуємо метод remove_user. Перевіряємо, чи видалено користувача зі списку.
    """
    user_manager.remove_user("Alice")
    users = user_manager.get_all_users()
    assert len(users) == 1
    assert users[0] == {'name': 'Bob', 'age': 25}

def test_get_all_users(user_manager):
    """
    Тестуємо метод get_all_users. Перевіряємо, чи список користувачів коректно повертається.
    """
    users = user_manager.get_all_users()
    assert len(users) == 2
    assert users[0] == {'name': 'Alice', 'age': 30}
    assert users[1] == {'name': 'Bob', 'age': 25}

def test_remove_nonexistent_user(user_manager):
    """
    Тестуємо метод remove_user для користувача, якого немає в списку.
    Перевіряємо, що кількість користувачів не змінюється.
    """
    user_manager.remove_user("Charlie")  # Користувач не існує
    users = user_manager.get_all_users()
    assert len(users) == 2  # Кількість не повинна змінитися

def test_skip_if_less_than_three_users(user_manager):
    """
    Перевіряємо кількість користувачів. Якщо їх менше трьох, тест пропускається.
    """
    user_manager.remove_user("Alice")
    user_manager.remove_user("Bob")
    if len(user_manager.get_all_users()) < 3:
        pytest.skip("Менше трьох користувачів, пропускаємо тест.")

def test_example(user_manager):
    """
    Приклад тесту, який завжди проходить.
    """
    assert True  # Звичайний тест, який завжди проходить
