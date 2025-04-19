import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="********",
    database="personas_db"
)

cursor = personas_db.cursor()
sentencia_sql = "INSERT INTO personas(nombre, apellido, edad) VALUES(%s, %s, %s)"
valores = ("Eddy", "Gabarrón", 4)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print(f"Se ha agregado el nuevo registro a la base de datos: {valores}")
cursor.close()
personas_db.close()