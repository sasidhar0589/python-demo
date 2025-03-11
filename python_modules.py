# module  a  directory 
from app import Ar
addition = Ar(6,7)
from datetime import datetime,timedelta

print(addition.add())
print(addition.subtract())
print(addition.multiply())
from src import  PT

ticket = PT(123456, time_of_entry=5, time_of_exit=10)

print(ticket.calculate_fee())
