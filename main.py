import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database=db_name
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
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
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
create table SEDAN_MODELS(
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
create table CUSTOMER_INFORMATION(
full_name VARCHAR(50) PRIMARY KEY,
address VARCHAR(50) NOT NULL,
phone_number VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
birthday VARCHAR(50) NOT NULL,
social_security_number integer(50) NOT NULL,
job_title VARCHAR(50) NOT NULL, 
monthly_income integer(30) NOT NULL);
"""

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
insert into SUV_MODELS values
('T37364544','2023', 'Genesis', 'GV70','222', '$55,000','2.5L', 'December 25th', '1')
('K54564544','2023', 'BMW', 'X3','0', '$72,900','2.0L', 'November 15th', '12')
('D33887899','2022', 'Mercedes Benz', 'GLC-Class','5000', '$66,500','4.0L V8', 'November 8th', '52')
('L21346423','2023', 'Maserati', 'Grecale','0', '$102,500','2.0L', 'May 5th', '1')
('G26726633','2023', 'Jaguar', 'F-Pace','77', '$52,400','2.0L', 'February 15th', '5')
('S37373737'','2023', 'Audi', 'Q5','0', '$59,200','2.0L', 'March 3rd', '8')
('R12323434','2023', 'Porsche', 'Macan','400', '$82,900','2.0L', 'November 12th', '15')
('P83273837','2023', 'BMW', 'X4','30', '$76,400','2.0L', 'December 1st', '1')
 """

#populate sedan table
sedan_table = """
insert into SEDAN_MODELS values
('Q54657677','2023', 'Honda', 'Accord Hybrid EX-L','0', '$29,147','2.0L', 'January 15th', '10')
('S68756575','2023', 'Toyota', 'Crown','0', '$42,658','2.5L', 'October 15th', '22')
('T38746535','2023', 'Hyundai', 'Sonata','500', '$26,555','2.0L', 'November 14th', '78')
('A56434852','2023', 'Hyundai', 'Elantra','0', '$22,452','1.6L', 'May 5th', '14')
('V46567745','2023', 'Honda', 'Civic','7855', '$26,572','1.5L', 'April 15th', '22')
('M67545521','2023', 'Kia', 'K5','55' '$27,075','1.6L', 'June 3rd', '10')
('J54774225','2023', 'Audi', 'A3','40', '$35,534','2.0L', 'November 22th', '1')
('K54675454','2023', 'BMW', '7 Series','30', '$93,858','3.0L', 'March 4th', '1')
 """


#populate truck table
truck_table = """
insert into TRUCK_models values
('k78627867','2023', 'Ford', 'F-150','300', '$34,585','3.5L V6', 'April 4th', '1')
('A21434784','2023', 'Ram', '1500','0', '$48,285','V6', 'August 22th', '44')
('S23484844','2023', 'Chevy', 'Silverado','50', '$36,300','2.7L', 'November 11th', '24')
('M28837474','2023', 'GMC', 'Sierra 1500','0', '$45,200','2.7L', 'June 4th', '2')
('M89873737','2023', 'Toyota', 'Tacoma','560', '$27,745','V6', 'October 1st', '5')
('B98347737','2023', 'Ford', 'Ranger','80', '$27,400','2.3L', 'January 3rd', '1')
('Q83823744','2023', 'GMC', 'Hummer V','400', '$110,295','Three-motor electric', 'November 15th', '1')
('V82774744','2023', 'Ford', 'F-150 Lightning','34', '$55,585','Dual Electric Motors', 'April 6th', '4')
 """

#populate staff table
staff_table = """
('546456','Kimberly','Dickerson','Corporate Manager','545-789-6545','3')
('877784','William','Dickerson','Branch Manager','875-541-6963','5')
('877784','Darrell','Simms','Branch Manager','705-698-7896','2')
('887541','Ken','Latte','Regional Manager','874-526-7841','3')
('984545','Stephon','Goldman','Regional Manager','314-789-4578','4')
('877845','Ben','Franklin','Store Manager','456-987-5874','9')
('455258','Will','Peterson','Store Manager','706-447-8766','3')
('545555','Aaliyah','Williams','Sales Representative','789-741-8521','4')
('147852','Anthony','Jets','Sales Representative','784-756-7894','1')
('789522','Daniela','Paul','Sales Representative','224-874-9654','5')
('896552','Linda','Cemile','Sales Representative','314-774-6358','3')
('258896','Márta','Lale','Sales Representative','315-852-5845','6')
('987755','Lesego','Adedayo','Mechanic','244-897-6321','10')
('963558','Simiyu','Ige','Mechanic','334-963-4896','5')
('147852','Tasha','Josephina','Mechanic','554-896-7412','6')
('897552','Adam','Shelton','Mechanic','885-987-4562','3')
('357419','Randell','Maxton','Mechanic','338-964-7898','1')
"""
#populate customer table
customer_information_table = """
('Ferdie Daniel','7785 Forest Hill Dr','784-895-7845','1/8/1997','678-556-4521','Cook','$682')
('Egbert Alonzo','5425 O'Reilly Walk','205-613-2506','4/8/1985','664-852-7894','Doctor','$3000')
('Calvin Shannon','8498 Annetta Circles','978-942-6856','11/8/1955','884-778-9654','Sales Representative','$950')
('Roy Wilmer','6601 Justine Centers','262-339-1640','1/23/1987','774-884-5258','Cashier','$700')
('Randolph Elmoy','47728 Veum Crest','615-245-9092','10/7/1997','664-852-7887','Bank Teller','$2300')
('Hilary Ronald','4803 Nina Dam','404-571-6693','1/28/1996','119-784-8752','Chef','$5000')
('Jarrett Fenton','4146 Drum Path Apt. 139','804-419-5500','11/7/1947','667-852-7894','Cook','$700')
('Kody Delroy','75630 Sigmund Burgs Apt. 005',724-722-7723','12/8/1991','645-852-7894','Welder','$2000')
('Esmé Hunter','99362 Stoltenberg Avenue','323-945-8736','1/1/1991','664-545-7894','CEO','$4000')
('Johnie Darius','776 Okuneva Run','609-865-6845','1/29/1997','664-852-7754','Mechanic','$1820')
"""

#Queries
create_database_query = "create database EXOTIC_DEALERSHIP"
#calling statement
connection = create_server_connection("localhost", "root", "student","exotic_dealership")
#call create_database function to create DB in mySQL
execute_query(connection,create_sedan_table)

