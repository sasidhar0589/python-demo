import mysql.connector
import os
print(os.getenv('OS'))
print(os.getenv("MYSQLUSER"))   

mqsqluser = os.getenv('mqsqluser')
mqsqlpass = os.getenv('mysqlpass')
print(mqsqluser)


mydb = mysql.connector.connect( host="localhost",user = mqsqluser,password = mqsqlpass,database ="parkinglot")
print(mydb)
mycursor = mydb.cursor()
# try:    
#     mycursor.execute("create database lotteryTicket")
# except Exception as e:
#     print("Database already exists.")

mycursor.execute("use parkinglot")
try:
    mycursor.execute("CREATE TABLE parking_time (id INT  PRIMARY KEY, star_time timestamp, end_time timestamp)")
except Exception as e:
    print("Table already exists.")

# mycursor.execute("INSERT INTO parking_time (id,star_time, end_time) VALUES (2, '2021-09-01 10:00:00', '2021-09-01 11:00:00')")
# mydb.commit()
# mycursor.execute("SELECT * FROM parkinglot.parking_time")
# result = mycursor.fetchall()

# mycursor.execute("Insert Into parkinglot.parking_table(id, parking_location_id,first_name,middle_name,last_name,parking_time_id,parking_ammount,parking_account_id) VALUES (2, 2, 'surya', 'kumar', 'reddy', 2, 100, 2)")
mydb.commit()

mycursor.execute("UPDATE parking_table SET parking_ammount = 200 WHERE id = 2")
mydb.commit()
mycursor.execute("""SELECT * FROM parkinglot.parking_table 
inner join parkinglot.parking_time on parking_time_id= parking_time.id""")
result = mycursor.fetchall()
print(result)


# perform delete on one record 

# def insert_into_parking_time(id, start_time, end_time,mycursor):
#     mycursor.execute(f"INSERT INTO parking_time (id,star_time, end_time) VALUES ({id}, '{start_time}', '{end_time}')")
#     mydb.commit()
#     print("Data inserted successfully")
# def 