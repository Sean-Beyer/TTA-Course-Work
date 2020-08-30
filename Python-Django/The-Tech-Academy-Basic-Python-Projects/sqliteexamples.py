

import sqlite3
sqlite3.connect("test_database.db")
c = connection.cursor()

c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

c.execute("INSERT INTO Peaple VALUES('Ron', 'Obvious', 42)")
connection.commit()
connection.close()

# Temp DB

connection = sqlite3.connect(':memory:')

c.execute("DROP TABLE IF EXISTS People")


# single line
import sqlite3
with sqlite3.connect("test_database.db") as connection:
    c = connection.cursor()
    c.execute("""DROP TABLE IF EXISTS People;
              CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
              INSERT INTO Peaple VALUES('Ron', 'Obvious', '42');
              """)
    connection.commit()
connection.close()

peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)


# user entered
import sqlite3

# get data
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

# execute insert
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
    c.connection(line)


# user defined data
import sqlite3
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)
with sqlite3.connect('test_database.db') as connection:
	c = connection.cursor()
	c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)

c.execute("UPDATE People SET Age=? WHERE firstName=? and lastName=?", (45, 'Luigi', 'Vercotti'))



# readlines
import sqlite3

peopleVALUES = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(firstName TEXT, lastName TEXT, age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleVALUES)

#select all first and last names from people over age 30
    c.execute("SELECT firstName, lastName FROM People WHERE age > 30")
    for row in c.fetchall():
        print(row)

# loop
    c.execute("SELECT firstName, lastName FROM People WHERE age > 30")
    while True:
            row = c.fetchone()
            if row is None:
                    break
            print(row)










