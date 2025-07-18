import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",        # or "127.0.0.1"
    user="your_username",    # replace with your MySQL username
    password="your_password",# replace with your MySQL password
    database="testdb"        # make sure this DB exists or create it
)

# Create a cursor object
cursor = mydb.cursor()

# Create a table (only once)
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

# Insert a record
sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
val = ("Alice", 21)
cursor.execute(sql, val)
mydb.commit()

print(cursor.rowcount, "record inserted.")

# Fetch and display all records
cursor.execute("SELECT * FROM students")
result = cursor.fetchall()

print("All Students:")
for row in result:
    print(row)

# Close the connection
cursor.close()
mydb.close()
