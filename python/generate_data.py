import pandas as pd

# Smart grid power consumption aur thick film sensors ka dummy data
sensor_data = {
    'Time_Hour': ['01:00', '02:00', '03:00', '04:00', '05:00', '06:00'],
    'Voltage_V': [230, 229, 231, 150, 228, 230],  # 150 par ek sudden drop (anomaly) hai
    'Current_A': [10.5, 10.2, 10.6, 25.0, 10.4, 10.5] # 25.0 par cyber-physical disruption (abnormal load) hai
}

# Data ko table format (DataFrame) me convert karna
df = pd.DataFrame(sensor_data)

# Table ko CSV file me save karna
df.to_csv('sensor_log.csv', index=False)

print("Badhai ho! Smart Grid dataset successfully create ho gaya hai.")
