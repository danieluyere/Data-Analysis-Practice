#Gemini v3 Pro created this to help me create a dummy IAQ file. 
#One day I will understand the whole logic here 100%

import random, datetime

filename = "nigeria_iaq_log.txt"
print("Generating sensor data...")

with open(filename, 'w') as f: # 'w' stands for WRITE
    f.write("Sensor_ID, Timestamp, CO2_ppm, Temp_C, Humidity_%\n")
    
    # Create 100 fake readings
    for i in range(100):
        # Fake Time
        t = (datetime.datetime.now() + datetime.timedelta(minutes=i*5)).strftime("%Y-%m-%d %H:%M:%S")
        # Fake CO2 (Random number between 350 and 1200)
        co2 = random.randint(350, 1200)
        # Fake Temp (Random number between 25.0 and 32.0)
        temp = round(random.uniform(25.0, 32.0), 1)
        # Fake Humidity
        hum = random.randint(40, 90)
        
        f.write(f"IAQ-001, {t}, {co2}, {temp}, {hum}\n")

print(f"✅ Success! Created {filename} with 100 readings.")