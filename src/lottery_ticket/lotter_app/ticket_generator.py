from area.ticket_location import TicketLocation as TL
from model.lottery_ticket import LotteryTicket as LT
from service.powerball_ticket_generator import PowerBallTicketGenrerator as PTG


class TicketGenerator:
    def __init__(self, name, age, ticket_number, location):
        self.name = name
        self.age = age
        self.ticket_number = ticket_number
        self.location = location
        self.ptg = PTG(self.name, self.age, self.ticket_number)
        
    def generate_ticket(self):
        ticket = PTG(self.name, self.age, self.ticket_number)
        location = TL(self.location)
        return f"{ticket.generate_ticket()} at {location.get_location()}"
    
    def get_ticket_number(self):
        return self.ticket_number
    
    def get_name(self):
        return self.ptg.get_name()
    
    def get_age(self):
        return self.ptg.get_age()
    
ticket_generator = TicketGenerator("Surya", 25, 123456, "Hyderabad")

ticket = ticket_generator.generate_ticket()

print(ticket)

ticket_number = ticket_generator.get_ticket_number()

print(f"Ticket Number: {ticket_number}")
name = ticket_generator.get_name()

print(f"Name: {name}")