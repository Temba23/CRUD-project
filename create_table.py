from estd_connection import estd_connection

cursor = estd_connection()

cursor.execute("DROP TABLE IF EXISTS STUDENT")

sql = """
CREATE TABLE STUDENT(
ID CHAR(20),
NAME CHAR(100),
DEPARTMENT CHAR(100)
);
"""

cursor.execute(sql)
print("Table created successful")
