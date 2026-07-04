import mysql.connector

# 1. MySQL Server se connect karna (Apna password zaroor daalna!)
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Isha@240724"  # <-- YAHAN APNA PASSWORD LIKHO
)

cursor = db_connection.cursor()

# 2. Smart Grid Database aur Table banana
cursor.execute("CREATE DATABASE IF NOT EXISTS SmartGridDB")
cursor.execute("USE SmartGridDB")

# Agar table pehle se hai toh hata do (taaki naye sire se ban sake)
cursor.execute("DROP TABLE IF EXISTS sensor_logs")

cursor.execute('''
    CREATE TABLE sensor_logs (
        Time_Hour VARCHAR(10),
        Voltage_V INT,
        Current_A FLOAT
    )
''')

# 3. Thick film sensor ka data insert karna
sql_insert = "INSERT INTO sensor_logs (Time_Hour, Voltage_V, Current_A) VALUES (%s, %s, %s)"
sensor_data = [
    ('01:00', 230, 10.5),
    ('02:00', 229, 10.2),
    ('03:00', 231, 10.6),
    ('04:00', 150, 25.0), # Yahan cyber-physical anomaly hai
    ('05:00', 228, 10.4),
    ('06:00', 230, 10.5)
]

cursor.executemany(sql_insert, sensor_data)
db_connection.commit() # Changes ko database me save karna

print(cursor.rowcount, "sensor records MySQL database me successfully load ho gaye!")

# 4. Anomaly Detection Query (SQL ke zariye Attack pakadna)
print("\n--- CYBER-PHYSICAL ANOMALY REPORT ---")

# Wo SQL Query jo automatically voltage drop ya current spike pakdegi
anomaly_query = "SELECT * FROM sensor_logs WHERE Voltage_V < 200 OR Current_A > 20"
cursor.execute(anomaly_query)

anomalies = cursor.fetchall()

for row in anomalies:
    print(f"ALERT! Gadbadi pakdi gayi -> Time: {row[0]} baje | Voltage: {row[1]}V | Current: {row[2]}A")

db_connection.close()
