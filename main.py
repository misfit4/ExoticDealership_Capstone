import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MySQL Database Connection Successful")
    except Error as err:
        print(f"Error {err}")
    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: {err}")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query sucessful")
    except Error as err:
        print(f"Error: {err}")


#create coupe table
create_coupe_table = """
create table COUPE_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL,
year integer(5) NOT NULL,
date_of_arrival integer(50) NOT NULL,
days_on_lot integer(50) NOT NULL);
"""

#create sedan table
create_sedan_table = """
create table COUPE_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL,
year integer(5) NOT NULL,
date_of_arrival integer(50) NOT NULL,
days_on_lot integer(50) NOT NULL);
"""


#create suv table
create_suv_table = """
create table SUV_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL,
year integer(5) NOT NULL,
date_of_arrival integer(50) NOT NULL,
days_on_lot integer(50) NOT NULL);
"""



#create truck table
create_truck_table = """
create table TRUCK_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL,
year integer(5) NOT NULL,
date_of_arrival integer(50) NOT NULL,
days_on_lot integer(50) NOT NULL);
"""

#create staff table
create_staff_table = """
create table STAFF_MEMBERS(
employee_ID integer(50) PRIMARY KEY,
first_name VARCHAR(40) NOT NULL,
last_name VARCHAR(40)NOT NULL,
employee_position VARCHAR(50) NOT NULL,
salary integer NOT NULL,
phone_number integer NOT NULL,
years_of_experience integer NOT NULL);
"""

#Create Customer Information
create_customer_information = """
full_name VARCHAR(50) PRIMARY KEY,
address VARCHAR(50) NOT NULL,
phone_number integer(30) NOT NULL,
email VARCHAR(50) NOT NULL,
birthday VARCHAR(50) NOT NULL,
social_security_number integer(50) NOT NULL,
job title VARCHAR(50) NOT NULL, 
monthly_income integer(30) NOT NULL);
"""





#populate coupe table

#populate coupe table
coupe_vehicles = """ 
insert into COUPE_MODELS values
('V34575484','2024', 'BMW', 'M4','300', '$77,995', 'November 4th', '10')
('G84654544','2023', 'Chevrolet', 'Camero ZL1','0', '$69,995', 'August 15th', '3')
('T54698746','2023', 'Chevrolet', 'Corvette','5000', '$65,895', 'November 10th', '25')
('L21346423','2023', 'Chevrolet', 'Corvette Z06','0', '$109,295', 'June 5th', '1')
('P78796512','2023', 'Ford', 'Mustang','5600', '$29,145', 'October 15th', '85')
('Q34575484','2023', 'McLaren', 'Artura','80, '$237,500', 'January 3rd', '10')
('R48765413','2023', 'Mercedes', 'AMG E53','4000', '$82,450', 'November 22th', '15')
('O89756321','2023', 'Porsche', '911','300', '$107,550', 'December 4th', '1')
 """

#populate suv table
suv_table = """
insert into SUV_models values
('123abc324','Jeep', 'Trackhawk',700, 111555)
('asd748441', 'Lamborghini', 'URUS', 1200, 135000) """


#populate sedan table
sedan_table = """
insert into SEDAN_models values
('123abc324','Jeep', 'Trackhawk',700, 111555)
('asd748441', 'Lamborghini', 'URUS', 1200, 135000) """


#populate truck table
truck_table = """
insert into TRUCK_models values
('123abc324','Jeep', 'Trackhawk',700, 111555)
('asd748441', 'Lamborghini', 'URUS', 1200, 135000) """



#Queries
create_database_query = "create database EXOTIC_DEALERSHIP"
#calling statement
connection = create_server_connection("localhost", "root", "student")
#call create_database function to create DB in mySQL
create_database(connection, create_database_query)

connection = create_server_connection("localhost", "root", "student","exotic_dealership")

