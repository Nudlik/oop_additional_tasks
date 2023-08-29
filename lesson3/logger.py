"""
Напишите класс Logger, имеющий следующие методы:

- __init__(self, filename): конструктор, принимающий имя файла, в который будет производиться запись логов;
- __call__(self, message): магический метод, который позволяет использовать объект класса Logger как функцию,
принимающую сообщение и записывающую его в файл.
"""


class Logger:

    def __init__(self, filename: str):
        self.filename: str = filename

    def __call__(self, *args, **kwargs):
        with open(self.filename, 'a', encoding='utf-8') as file:
            print(args[0], file=file)


logger = Logger("log.txt")
logger("This is a test message.")
