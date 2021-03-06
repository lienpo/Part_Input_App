import pyodbc
import csv

server = '192.168.1.21'
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

# striker Castit connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

#get cursor
castit_cursor = cnxn.cursor()

#Crate new table for input named part_cast
castit_cursor.execute("if not exists create table PART_CAST VALUES( TIME timestamp(), PARTNO char(10), LOT int(2), HANGER int(2))")

'''
Get info from Jeremy about how to input info but assume there are a list of 3 values input and the timestamp for the current time

value_1 = PARTNO
value_2 = LOT
value_3 = HANGER
'''

#castit_cursor.execute("insert into PART_CAST (TIME, PARTNO, LOT, HANGER) VALUES (NOW(), ?, ?, ?)"), value_1, value_2, value_3)
