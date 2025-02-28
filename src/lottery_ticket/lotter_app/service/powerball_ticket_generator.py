from model.lottery_ticket import LotteryTicket as LT
class PowerBallTicketGenrerator(LT):
    def __init__(self, name, age, ticket_number):
        super().__init__(name, age)
        self.ticket_number = ticket_number
        
    def generate_ticket(self):
        return f"{self.get_name()} with ticket number {self.ticket_number}"
    
    def get_ticket_number(self):
        return self.ticket_number
    
    def get_name(self):
        return super().get_name()
    
    def get_age(self):
        return super().get_age()