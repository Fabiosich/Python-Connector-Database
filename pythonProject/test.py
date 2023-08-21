from mysql.connector import MySQLConnection, errors

""" Connection parameters """
user = 'root'
password = '12345678'
database = 'test'

try:
    """Establish a connection"""
    mydb = MySQLConnection(user=user, password=password, database=database)

except errors.ProgrammingError as e:
    print("Error:", e)

"""Inicialize cursor"""
mycursor = mydb.cursor()

"""Create a Table in Database"""
# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

"""Insert data in Database Table"""
# sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# students = [('João', 32),
#            ('Fábio', 31),
#           ('André', 28),
#            ("Maria", 58),
#            ("Ana", 35)]

#mycursor.executemany(sqlFormula, students)

"""Save all the changes"""
# mydb.commit()

"""See tables"""
# mycursor.execute("SHOW TABLES")

"""Update data (ex: Change João age)"""
# sql = "UPDATE students SET age = 34 WHERE name = 'João'"

# mycursor.execute(sql)
# mydb.commit()

"""Select data with limit chose"""
# mycursor.execute("SELECT * FROM students LIMIT 5")
# myresult = mycursor.fetchall()

# for result in myresult:
#     print(result)

"""Ordering by name"""
# mycursor.execute("SELECT * FROM students ORDER BY name")
# mycursor.execute("SELECT * FROM students ORDER BY name DESC ")
# myresult = mycursor.fetchall()

# for r in myresult:
#    print(r)

"""Delete entrys"""
# mycursor.execute("DELETE FROM students WHERE name ='João'")
# mydb.commit()

"""Drop/Delete Tables"""
mycursor.execute("DROP TABLE students")
mydb.commit()
