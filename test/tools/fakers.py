from faker import Faker

class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """
    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных.
        """
        self.faker = faker


    def bet(self) -> int:
        """
        Генерирует случайный размер ставки в интервале от 100 до 200 с шагом 10.

        :return: Случайное число.
        """
        return self.faker.random_int(min=100,
                                     max=200,
                                     step=10)
    def text(self) -> str:
        """
        Генерирует случайный текст.

        :return: Случайный текст.
        """
        return self.faker.text()


    def username(self) -> str:
        """
        Генерирует случайное имя пользователя.

        :return: Случайный никнейм.
        """
        return self.faker.user_name()


    def password(self) -> str:
        """
        Генерирует случайный пароль пользователя.

        :return: Случайный пароль.
        """
        return self.faker.password()



# Создаем экземпляр класса Fake с использованием Faker
fake = Fake(faker=Faker())