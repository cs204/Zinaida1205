import pytest
from jar import Jar

def test_init():
     jar = Jar(10)
     assert jar.capacity() == 10, "Ёмкость не соответствует заданной."

     with pytest.raises(ValueError):
      Jar(-5)

def test_str():
    jar = Jar(10)
    assert str(jar) == "", "Пустой Jar должен печататься как ''."
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪", "Неверное строковое представление Jar после добавления печений."
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪", "Неверное строковое представление Jar после добавления еще печений."

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size() == 5, "Неверное количество печений после добавления."

    jar.deposit(3)
    assert jar.size() == 8, "Неверное количество печений после добавления еще печений."

    with pytest.raises(ValueError):
        jar.deposit(100), "Ошибка при добавлении печений, превышающих ёмкость Jar"


def test_withdraw():
    jar = Jar(10)
    jar.deposit(7)
    jar.withdraw(3)
    assert jar.size() == 4, "Неверное количество печений после изъятия."

    jar.withdraw(2)
    assert jar.size() == 2, "Неверное количество печений после изъятия еще печений."

    with pytest.raises(ValueError):
        jar.withdraw(100), "Ошибка при изъятии больше печений, чем есть в Jar"


if __name__ == '__main__':
    pytest.main([__file__])
