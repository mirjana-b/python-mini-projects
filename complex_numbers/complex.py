from math import sqrt


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def magnitude(self):
        return sqrt(self.real * self.real + self.imag * self.imag)

    def add(number1, number2):
        result = ComplexNumber(number1.real + number2.real, number1.imag + number2.imag)
        return result

    def add_change(self, b):
        self.real = self.real + b.real
        self.imag = self.imag + b.imag

    def __add__(self, b):
        return ComplexNumber.add(self, b)

    def __str__(self):
        return f"{self.real} + i*{self.imag}"
