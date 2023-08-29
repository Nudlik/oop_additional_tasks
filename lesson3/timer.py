"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
import time


class Timer:

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.end_time = time.time()
            self.elapsed_time = self.end_time - self.start_time


with Timer() as timer:
    res = sum(i ** 99 for i in range(1000000))

print("Execution time:", timer.elapsed_time)
