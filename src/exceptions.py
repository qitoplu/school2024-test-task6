class ArgumentCountError(Exception):
    def __init__(self, message="Неверное количество аргументов"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"ArgumentCountError: {self.message}"


class CollisionError(Exception):
    def __init__(self, message="Два разных человека имеют одинаковый id!"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"CollisionError: {self.message}"


class HoursError(Exception):
    def __init__(self, message="Неверно указано время работы"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"HoursError: {self.message}"
