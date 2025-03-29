import sqlalchemy
from sqlalchemy.orm import  DeclarativeBase
class Base(DeclarativeBase):
    pass
from sqlalchemy import create_engine, text, Column, Integer, String, Select, select
engine = create_engine('mysql://<user>:<pass>@localhost/parkinglot', echo=True)
connection = engine.connect()
number =1 
result = connection.execute(text(f"select * from parking_table where id = {number}"))

# metadataobj = MetaData()
# metadataobj.reflect(bind=engine)
# print(metadataobj.tables.keys())
print(result.fetchall())
for row in result:
    print(row)
Base.metadata
Base.registry
class ParkingTable(Base):
    __tablename__ = 'parking_table'
    id = Column(Integer, primary_key=True)
    parking_location_id = Column(Integer)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    parking_time_id = Column(String)
    parking_ammount = Column(String)
    parking_account_id = Column(Integer)
    

stmt = select(ParkingTable).where(ParkingTable.id == number)
result = connection.execute(stmt)
print(result.fetchall())