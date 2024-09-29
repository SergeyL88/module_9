from random import choice
from typing import Any


# Lambda-функция

first = 'Мама мыла раму'
second = 'Рамена мало было'

lambda_result = list(map(lambda x, y: x == y, first, second))

print(lambda_result)


# Замыкание

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for line in data_set:
                file.write(str(line) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__

class MysticBall():

    def __init__(self, *words) -> None:
        self.words = [*words]

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Может быть')
print(first_ball())
print(first_ball())
print(first_ball())
