class AdditionTwoNumbers:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def __str__(self):
        return f"{str(self.number1)} + {str(self.number2)}"
        
    def add(self):
        return self.number1 + self.number2
    
    def multiply(self):
        print(self.add())
        return self.number1 * self.number2
    
    def subtract(self):
        return self.number1 - self.number2
    
    def divide(self):
        return self.number1 / self.number2
    
addition_two_numbers = AdditionTwoNumbers(6, 3)
print(addition_two_numbers)
print(addition_two_numbers.add())
print(addition_two_numbers.multiply())
print(addition_two_numbers.subtract())
print(addition_two_numbers.divide())