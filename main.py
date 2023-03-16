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
engine VARCHAR(50) NOT NULL,
year integer(5) NOT NULL,
date_of_arrival VARCHAR(50) NOT NULL,
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
engine VARCHAR(50) NOT NULL,
year integer(5) NOT NULL,
date_of_arrival VARCHAR(50) NOT NULL,
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
engine VARCHAR(50) NOT NULL,
year integer(5) NOT NULL,
date_of_arrival VARCHAR(50) NOT NULL,
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
engine VARCHAR(50) NOT NULL,
year integer(5) NOT NULL,
date_of_arrival VARCHAR(50) NOT NULL,
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
phone_number VARCHAR(50) NOT NULL,
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
coupe_table = """ 
insert into COUPE_MODELS values
('V34575484','BMW','M4',300,77995,'3.0L 6 cylinder',2024, 'November 4th', 10),
('G84654544', 'Chevrolet','CameroZL1',0,69995,'6.2L V8',2023, 'August 15th', 3),
('T54698746', 'Chevrolet','Corvette',5000, 65895,'6.2L LT2 V8',2023, 'November 10th', 25),
('L21346423', 'Chevrolet','Corvette Z06',0, 109295,'LT6 5.5L',2023, 'June 5th', 1),
('P78796512', 'Ford','Mustang',5600, 29145,'2.3 4-cylinder',2023,'October 15th', 85),
('Q34575484', 'McLaren','Artura',80, 237500,'3.0L V6',2023, 'January 3rd', 10),
('R48765413', 'Mercedes','AMG E53',4000, 82450,'3.0L 6-cylinder',2023, 'November 22th', 15),
('O89756321', 'Porsche','911',300, 107550,'3.0L 6-cylinder',2023, 'December 4th',1)
 """

#populate suv table
suv_table = """
insert into SUV_MODELS values
('T37364544', 'Genesis','GV70',222, 55000,'2.5L',2023,'December 25th', 1),
('K54564544', 'BMW','X3',0, 72900,'2.0L',2023, 'November 15th', 12),
('D33887899', 'Mercedes Benz','GLC-Class',5000,66500,'4.0L V8',2022,'November 8th', 52),
('L21346423', 'Maserati','Grecale',0,102500,'2.0L',2023,'May 5th', 1),
('G26726633', 'Jaguar','F-Pace',77, 52400,'2.0L',2023,'February 15th', 5),
('S37373737', 'Audi','Q5',0, 59200,'2.0L',2023,'March 3rd',8),
('R12323434','Porsche','Macan',400, 82900,'2.0L',2023, 'November 12th',15),
('P83273837', 'BMW','X4',30, 76000,'2.0L',2023,'December 1st',1)
 """

#populate sedan table
sedan_table = """
insert into SEDAN_MODELS values
('Q54657677','Honda','Accord Hybrid EX-L',2, 29147,'2.0L',2023,'January 15th', 10),
('S68756575','Toyota','Crown',2,42658,'2.5L', 2023,'October 15th', 22),
('T38746535','Hyundai','Sonata',500,26555,'2.0L',2023, 'November 14th', 78),
('A56434852','Hyundai','Elantra',0,22452,'1.6L',2023,'May 5th', 14),
('V46567745','Honda','Civic',7855,26572,'1.5L',2023, 'April 15th',22),
('M67545521','Kia','K5',55, 27075,'1.6L',2023,'June,3rd', 10),
('J54774225','Audi','A3',40, 35534,'2.0L',2023,'November 22th', 1),
('K54675454','BMW','7 Series',30,93858,'3.0L',2023, 'March 4th', 1)
 """


#populate truck table
truck_table = """
insert into TRUCK_models values
('k78627867','Ford','F-150',300,34585,'3.5L V6',2023,'April 4th', 1),
('A21434784','Ram','1500',0,48285,'V6',2023,'August 22th',44),
('S23484844','Chevy','Silverado',50,36300,'2.7L',2023,'November 11th',24),
('M28837474','GMC','Sierra 1500','0',45200,'2.7L',2023,'June 4th',2),
('M89873737','Toyota','Tacoma',560, 27745,'V6',2023,'October 1st',5),
('B98347737','Ford','Ranger',80, 27400,'2.3L',2023,'January 3rd',1),
('Q83823744', 'GMC','Hummer V',400,110295,'Three-motor electric',2023,'November 15th',1),
('V82774744','Ford','F-150 Lightning',34,55585,'Dual Electric Motors',2023,'April 6th', 4)
 """

#populate staff table
staff_table = """
insert into STAFF_MEMBERS values
(546456,'Kimberly','Dickerson','Corporate Manager',200000,54578965,3),
(877784,'William','Dickerson','Branch Manager',150000,8755416963,5),
(877785,'Darrell','Simms','Branch Manager',150000,7056987896,2),
(887541,'Ken','Latte','Regional Manager',90000,8745267844,3),
(984545,'Stephon','Goldman','Regional Manager',90000,3147894578,4),
(877845,'Ben','Franklin','Store Manager',60000,4569875874,9),
(455258,'Will','Peterson','Store Manager',60000,7064478766,3),
(545555,'Aaliyah','Williams','Sales Representative',45000,7897418521,4),
(147853,'Anthony','Jets','Sales Representative',45000,7847567894,1),
(789522,'Daniela','Paul','Sales Representative',45000,2248749654,5),
(896552,'Linda','Cemile','Sales Representative',45000,3147746358,3),
(258896,'Márta','Lale','Sales Representative',45000,3158525845,6),
(987755,'Lesego','Adedayo','Mechanic',42000,2448976321,10),
(963558,'Simiyu','Ige','Mechanic',42000,3349634896,5),
(147852,'Tasha','Josephina','Mechanic',42000,5548967412,6),
(897552,'Adam','Shelton','Mechanic',42000,8859874562,3),
(357419,'Randell','Maxton','Mechanic',42000,3389647898,1)
"""
#populate customer table
customer_information_table = """
insert into CUSTOMER_INFORMATION values
('Ferdie Daniel','7785 Forest Hill Dr','784-895-7845','ferdie33d@yahoo.com','1/8/1997',67855645,'Cook',682),
('Egbert Alonzo','5425 Reilly Walk','205-613-2506','EA1@yahoo.com','4/8/1985',66485278,'Doctor',3000),
('Calvin Shannon','8498 Annetta Circles','978-942-6856','CShann22@yahoo.com','11/8/1955',88477896,'Sales Representative',950),
('Roy Wilmer','6601 Justine Centers','262-339-1640','Roy004@yahoo.com','1/23/1987',77488452,'Cashier',700),
('Randolph Elmoy','47728 Veum Crest','615-245-9092','RandoEl2@yahoo.com','10/7/1997',66485278,'Bank Teller',2300),
('Hilary Ronald','4803 Nina Dam','404-571-6693','HilaryRon4@yahoo.com','1/28/1996',11978487,'Chef',5000),
('Jarrett Fenton','4146 Drum Path Apt139','804-419-5500','JFen55@yahoo.com','11/7/1947',66785278,'Cook',700),
('Kody Delroy','75630 Sigmund Burgs Apt005','724-722-7723','KodyD33@yahoo.com','12/8/1991',64585278,'Welder',2000),
('Esme Hunter','99362 Stoltenberg Avenue','323-945-8736','EsmeH22@yahoo.com','1/1/1991',66454578,'CEO',4000),
('Johnie Darius','776 Okuneva Run','609-865-6845','1/29/1997','JD99@yahoo.com',66485277,'Mechanic',1820)
"""

#read values from coupe table
display_coupe_models_table = """
SELECT * FROM COUPE_MODELS;
"""

#read values from sedan table
display_sedan_models_table = """
SELECT * FROM SEDAN_MODELS;
"""

#read values from suv table
display_suv_models_table = """
SELECT * FROM SUV_MODELS;
"""


#read values from truck table
display_truck_models_table = """
SELECT * FROM TRUCK_MODELS;
"""


#read values from staff table
display_staff_models = """
SELECT * FROM STAFF_MEMBERS;
"""
#read values from customer table
display_customer_information = """
SELECT * FROM CUSTOMER_INFORMATION;
"""

update_secondcoupe_mileage = """
update coupe_models 
SET mileage = 8888
where vin_number = 'G84654544'
"""
remove_second_staff_member = """
DELETE FROM STAFF_MEMBERS
where employee_ID = 897552
"""

#Queries

#calling statement
connection = create_server_connection("localhost", "root", "student","exotic_dealership")
#call create_database function to create DB in mySQL
execute_query(connection,remove_second_staff_member)
#call read query function to fetch information from MySQL
results = read_query(connection,display_staff_models)
#iterate through the table to display all information
for result in results:
     print(result)
