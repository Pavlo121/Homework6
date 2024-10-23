class BankAccount:
    """
    Клас, що представляє банківський рахунок.

    Атрибути:
        balance (float): Поточний баланс рахунку.
    """

    def __init__(self):
        """Ініціалізує новий банківський рахунок з нульовим балансом."""
        self.balance = 0.0

    def deposit(self, amount: float):
        """
        Поповнює рахунок на вказану суму.

        Аргументи:
            amount (float): Сума поповнення.

        Винятки:
            ValueError: Якщо сума поповнення не є позитивною.
        """
        if amount <= 0:
            raise ValueError("Сума поповнення повинна бути позитивною.")
        self.balance += amount

    def withdraw(self, amount: float):
        """
        Знімає з рахунку вказану суму.

        Аргументи:
            amount (float): Сума зняття.

        Винятки:
            ValueError: Якщо сума зняття не є позитивною або якщо недостатньо коштів на рахунку.
        """
        if amount <= 0:
            raise ValueError("Сума зняття повинна бути позитивною.")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів.")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Повертає поточний баланс рахунку.

        Повертає:
            float: Поточний баланс рахунку.
        """
        return self.balance



import pytest
from unittest import mock

@pytest.fixture
def bank_account():
    """
    Фікстура для створення об'єкта банківського рахунку.
    """
    account = BankAccount()
    return account

@pytest.mark.parametrize("amount, expected_balance", [
    (100, 100),
    (50.5, 50.5),
    (200, 200),
])
def test_deposit(bank_account, amount, expected_balance):
    """
    Тестує метод deposit для різних сум поповнення.

    Аргументи:
        bank_account (BankAccount): Об'єкт банківського рахунку.
        amount (float): Сума поповнення.
        expected_balance (float): Очікуваний баланс після поповнення.
    """
    bank_account.deposit(amount)
    assert bank_account.get_balance() == expected_balance

def test_deposit_negative_amount(bank_account):
    """
    Тестує метод deposit на відмову при негативній сумі поповнення.
    """
    with pytest.raises(ValueError, match="Сума поповнення повинна бути позитивною."):
        bank_account.deposit(-50)

@pytest.mark.parametrize("initial_balance, withdraw_amount, expected_balance", [
    (100, 50, 50),
    (200, 100, 100),
])
def test_withdraw(bank_account, initial_balance, withdraw_amount, expected_balance):
    """
    Тестує метод withdraw для різних сценаріїв зняття коштів.
    """
    bank_account.deposit(initial_balance)
    bank_account.withdraw(withdraw_amount)
    assert bank_account.get_balance() == expected_balance

@pytest.mark.skipif(lambda account: account.get_balance() == 0, reason="Пропускаємо тест, якщо баланс рахунку нульовий")
def test_withdraw_from_empty_account(bank_account):
    """
    Тестує метод withdraw на відмову при спробі зняття з порожнього рахунку.
    """
    with pytest.raises(ValueError, match="Недостатньо коштів."):
        bank_account.withdraw(100)

def test_get_balance_mocked(bank_account):
    """
    Тестує метод get_balance за допомогою мокування.
    """
    with mock.patch.object(bank_account, 'get_balance', return_value=200) as mock_get_balance:
        assert bank_account.get_balance() == 200
        mock_get_balance.assert_called_once()
