
class LotteryTicket:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eligibility_check(self):
        if self.age >= 18:
            return f"{self.name} is eligible for lottery ticket"
        else:
            return f"{self.name} is not eligible for lottery ticket"
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    