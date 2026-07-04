import pandas as pd
import matplotlib.pyplot as plt

# 1. Jo dataset humne banaya tha, usko read karna
df = pd.read_csv('sensor_log.csv')

# 2. Graph (Plot) banana
plt.figure(figsize=(10, 5)) # Graph ki window ka size set karna

# Voltage ki line (Blue color, Gol marker)
plt.plot(df['Time_Hour'], df['Voltage_V'], label='Voltage (V)', color='blue', marker='o', linewidth=2)

# Current ki line (Red color, Cross marker)
plt.plot(df['Time_Hour'], df['Current_A'], label='Current (A)', color='red', marker='x', linewidth=2)

# 3. Graph ko sajana (Labels aur Title add karna)
plt.title('Smart Grid Sensor Data - Cyber-Physical Anomaly Detection')
plt.xlabel('Time (Hour)')
plt.ylabel('Sensor Readings')
plt.legend()
plt.grid(True)

# 4. Graph ko screen par pop-up karke dikhana
plt.show()
