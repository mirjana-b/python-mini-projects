from complex import ComplexNumber

def main():
    a = ComplexNumber(3, 4)
    b = ComplexNumber(5, 6)

    print(f"This is the magnitude of the given complex number {a.magnitude()}")

    sum_result = ComplexNumber.add(a, b)

    print(f"{sum_result.real} + i*{sum_result.imag}")

    a.add_change(b)
    print(a+b)


if __name__ == "__main__":
    main()

