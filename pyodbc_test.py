import pyodbc
server = '10.160.20.65,51261'
database = 'dw_motrpac'
username = 'mt_internal_user'
password = 'se@lf0n1nt3rn@l'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print (row)
    row = cursor.fetchone()


#'Driver={ODBC Driver 13 for SQL Server};Server=10.160.20.65\SSQL_2016;Database=dw_motrpac;User=mt_internal_user;Password=se@lf0n1nt3rn@l'