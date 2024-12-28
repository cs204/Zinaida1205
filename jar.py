class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Ёмкость должна быть неотрицательным целым числом.")
        self._capacity=capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Нельзя добавить больше печений, чем вмещает банка.")
        self._size += n

    def withdraw(self, n):
        if self._size < n:
            raise ValueError("В банке недостаточно печений для изъятия.")
        self._size -= n

    def capacity(self):
        return self._capacity

    def size(self):
        return self._size
