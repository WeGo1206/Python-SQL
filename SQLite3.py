import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#             first text,
#             last text,
#             pay interger
#             )""")

# c.execute("INSERT INTO employees VALUES ('Mary','Schafer',50000)")
# conn.commit()
c.execute("SELECT * FROM employees WHERE last='Schafer'")
print(c.fetchall())

conn.commit()

conn.close()

