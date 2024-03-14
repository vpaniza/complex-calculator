class ComplexCalculator:
    # Receives 2 numbers to perform operations: num1=(a,b) num2=(c,d) where a and c are 
    # the real part, while b and d are the imaginary part

    def __init__(self, num1, num2):
        self.real1 = num1[0]
        self.imag1 = num1[1]
        self.real2 = num2[0]
        self.imag2 = num2[1]

    def add(self):
        return (self.real1 + self.real2, self.imag1 + self.imag2)

    def subtract(self):
        return (self.real1 - self.real2, self.imag1 - self.imag2)

    def multiply(self):
        real = self.real1 * self.real2 - self.imag1 * self.imag2
        imag = self.real1 * self.imag2 + self.imag1 * self.real2
        return (real, imag)

    def divide(self):
        divisor = self.real2 ** 2 + self.imag2 ** 2
        if divisor == 0:
            return "Can't divide by 0"
        real = float(self.real1 * self.real2 + self.imag1 * self.imag2) / divisor
        imag = float(self.imag1 * self.real2 - self.real1 * self.imag2) / divisor
        return (real, imag)