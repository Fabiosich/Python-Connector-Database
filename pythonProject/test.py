from mysql.connector import MySQLConnection, errors

# Connection parameters
user = 'root'
password = '12345678'
database = 'test'

try:
    # Establish a connection
    mydb = MySQLConnection(user=user, password=password, database=database)
    cursor = mydb.cursor()

    # Create the table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS mytable (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255), idade VARCHAR(255), peso VARCHAR(255)
    )
    """
    cursor.execute(create_table_query)
    mydb.commit()

    # Insert data into the table
    insert_query = "INSERT INTO mytable (nome) VALUES (%s)"
    data = [("Alice",), ("Bob",), ("Charlie",), ("David",), ("Eve",)]
    cursor.executemany(insert_query, data)
    mydb.commit()

    insert_query1 = "INSERT INTO mytable (idade) VALUES (%s)"
    data1 =[("23",) ,("19",) ,("18",) ,("15",), ("29",)]
    cursor.executemany(insert_query, data1)
    mydb.commit()
    
    # Fetch and print data from the table
    cursor.execute("SELECT * FROM mytable")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    mydb.close()

except errors.ProgrammingError as e:
    print("Error:", e)





