# Database Assignment 02
# Author(s): John Shapiro


import csv
import pymysql

# set up the credentials
server = 'localhost'
database = 'ippstest'
user = 'ipps'
password = '024680'

# connect to the database
conn = pymysql.connect(host = server, user = user, password = password, db = database)
if (conn):
    print('Connection to MySQL database', database, 'was successful!')

# open up the csv as a list of rows of the ipps dataset. Each row is a list
with open('IPPS_dataset.csv', 'r') as data:
    reader = csv.reader(data)
    ipps_file = list(reader)

# lists of DRGs, Provider IDs, HRRs, and Discharge Keys to avoid duplication
drgs = []
ids = []
hrrs = []
discharges = []
cursor = conn.cursor()

for line in ipps_file[1:]:
    # check if any data is going to be duplicated, and if not, put it in the proper table
    if line[0][:3] not in drgs:
        sql = 'INSERT INTO DRGs VALUES (%s, %s)'
        cursor.execute(sql, (line[0][:3], line[0][6:]))
        drgs.append(line[0][:3])
    if int(line[1]) not in ids:
        sql = 'INSERT INTO Providers VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(sql, (int(line[1]), line[2], line[3], line[4], line[5], line[6], line[7][:2], line[7][5:]))
        ids.append(int(line[1]))
    if line[0][:3] + line[1] not in discharges:
        sql = 'INSERT INTO DischargeStats VALUES (%s, %s, %s, %s, %s, %s)'
        cursor.execute(sql, (line[0][:3], int(line[1]), int(line[8]), float(line[9]), float(line[10]), float(line[11])))
        discharges.append(line[0][:3] + line[1])
    if line[7] not in hrrs:
        sql = 'INSERT INTO HRRs VALUES (%s, %s)'
        cursor.execute(sql, (line[7][:2], line[7][5:]))
        hrrs.append(line[7])
    
# write the changes to the database
conn.commit()

# closes the connection
print('Bye!')
conn.close()