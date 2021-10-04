import mysql.connector
from mysql.connector import cursor

db = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database="facedup",
)

if db.is_connected():
  print("Berhasil terhubung ke database")

dbCursor = db.cursor()
sql = "INSERT INTO user (namaLengkap, username, kataSandi) VALUES (%s, %s, %s)"
val = ("Iman", "admin", "123")
dbCursor.execute(sql, val)

db.commit()
print("{} Data ditambahkan".format(dbCursor.rowcount))
