import pandas as pd
import mysql.connector

df = pd.read_csv("sensor_log_updated.csv")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Isha@240724",
    database="smartgriddb"
)

cursor = conn.cursor()

cursor.execute("DELETE FROM sensor_logs")

insert_query = """
INSERT INTO sensor_logs
(Time_Hour, Voltage_V, Current_A, Temperature_C, Power_W, Timestamp)
VALUES (%s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():
    cursor.execute(insert_query, (
        row["Time_Hour"],
        int(row["Voltage_V"]),
        float(row["Current_A"]),
        float(row["Temperature_C"]),
        float(row["Power_W"]),
        row["Timestamp"]
    ))

conn.commit()

print("Updated data inserted successfully!")

cursor.close()
conn.close()
