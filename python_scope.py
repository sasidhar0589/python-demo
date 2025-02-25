#scope 
temp_var = 10
def add(num1, num2):
    global local_var 
    local_var= 5
    return num1 + num2 + local_var
print(add(5,6))

class TempLocalVariable:
    def addition(self,num1, num2):
        local_var = 5
        return num1 + num2 + local_var + temp_var

    def subtraction(self, num1, num2):
        self.local_var = 5
        return num1 - num2 - self.local_var


print(TempLocalVariable().addition(5,6))
print(TempLocalVariable().subtraction(10, 2))