class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        sumR = self.real + other.real
        sumI = self.imag + other.imag
        return Complex(sumR, sumI)

    def __str__(self):
        return f"{self.real} + i{self.imag}"

num1_real = float(input("Enter the real part of num1: "))
num1_imag = float(input("Enter the imaginary part of num1: "))
num1 = Complex(num1_real, num1_imag)
num2_real = float(input("Enter the real part of num2: "))
num2_imag = float(input("Enter the imaginary part of num2: "))
num2 = Complex(num2_real, num2_imag)
result = num1 + num2
print(f"Addition of two complex numbers \n{num1} \n {num2} \nis {result}")
