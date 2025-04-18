import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Suigintou.89",
    database="personas_db"
)

cursor = personas_db.cursor()
sentencia_sql = "UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s"
valores= ("Eddy", "Gabarron", 4, 2)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print("Se ha modificado la informacion...")
cursor.close()
personas_db.close()