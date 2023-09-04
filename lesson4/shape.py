"""
Напишите класс Shape, представляющий геометрическую фигуру, имеющий следующие методы:

- __init__(self, name): конструктор, принимающий имя геометрической фигуры;
- area(self): метод, который вычисляет площадь геометрической фигуры.

Напишите класс Rectangle, наследующийся от класса Shape, представляющий прямоугольник, имеющий следующие методы:

- __init__(self, name, width, height): конструктор, принимающий имя прямоугольника, ширину и высоту;
- area(self): метод, который вычисляет площадь прямоугольника.

Напишите класс Triangle, наследующийся от класса Shape, представляющий треугольник, имеющий следующие методы:

- __init__(self, name, base, height): конструктор, принимающий имя треугольника, основание и высоту;
- area(self): метод, который вычисляет площадь треугольника.
"""


class Shape:
    def __init__(self, name: str):
        self.name: str = name

    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, name: str, width: int, height: int):
        super().__init__(name)
        self.width: int = width
        self.height: int = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, name: str, base: int, height: int):
        super().__init__(name)
        self.base: int = base
        self.height: int = height

    def area(self):
        return (self.base * self.height) / 2


shape = Shape("Shape")
print(shape.area())  # 0

rect = Rectangle("Rectangle", 5, 10)
print(rect.area())  # 50

tri = Triangle("Triangle", 6, 4)
print(tri.area())  # 12
