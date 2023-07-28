class AddNumbers:
    def add(self, a, b):
        return a + b

class Calculator(AddNumbers):
    def display_result(self, a, b):
        result = self.add(a, b)
        print(f"The result of {a} + {b} is {result}")
        
calculator = Calculator()
calculator.display_result(10, 20) 
calculator.display_result(5, -3)  