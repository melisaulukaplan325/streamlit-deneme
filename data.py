import pandas as pd
import random
from datetime import datetime, timedelta

# Generate synthetic data for 50 bins
num_bins = 50
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 1, 31)

bin_ids = [f'bin_{i}' for i in range(1, num_bins + 1)]
# Coordinates for Odunpazarı and Tepebaşı districts
odunpazari_base_lat = 39.7628
odunpazari_base_lon = 30.5257
tepebasi_base_lat = 39.7767
tepebasi_base_lon = 30.5206

data = []

for i, bin_id in enumerate(bin_ids):
    if i % 2 == 0:  # Assign to Odunpazarı
        latitude = odunpazari_base_lat + (random.random() - 0.5) / 50  # Smaller variation to spread bins out
        longitude = odunpazari_base_lon + (random.random() - 0.5) / 50  # Smaller variation to spread bins out
    else:  # Assign to Tepebaşı
        latitude = tepebasi_base_lat + (random.random() - 0.5) / 50  # Smaller variation to spread bins out
        longitude = tepebasi_base_lon + (random.random() - 0.5) / 50  # Smaller variation to spread bins out
    
    fill_level = random.randint(0, 100)
    # Calculate expected full time based on fill level
    if fill_level == 0:
        expected_full_minutes = 500
    elif fill_level == 100:
        expected_full_minutes = 0
    else:
        expected_full_minutes = int(500 - (fill_level * 5))  # More linear interpolation
    
    # Calculate material fill levels based on fill_level
    if fill_level <= 10:
        cardboard = random.randint(5,15)
        glass = random.randint(5,15)
        metal = random.randint(5,15)
        paper = random.randint(5,15)
        plastic = random.randint(5,15)
        trash = random.randint(5,15)
    elif fill_level <= 50:
        cardboard = random.randint(15, 50)
        glass = random.randint(15, 50)
        metal = random.randint(15, 50)
        paper = random.randint(15, 50)
        plastic = random.randint(15, 50)
        trash = random.randint(15, 50)
    else:
        cardboard = random.randint(50,100)
        glass = random.randint(50,100)
        metal = random.randint(50,100)
        paper = random.randint(50,100)
        plastic = random.randint(50,100)
        trash = random.randint(50,100)

    timestamp = start_date + (end_date - start_date) * random.random()
    
    data.append([bin_id, latitude, longitude, fill_level, expected_full_minutes, timestamp, cardboard, glass, metal, paper, plastic, trash])

df = pd.DataFrame(data, columns=['bin_id', 'latitude', 'longitude', 'fill_level', 'expected_full', 'timestamp', 'cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash'])
df = df.sort_values(by=['bin_id'])
df.to_csv('synthetic_trashbin_data_eskisehir.csv',index=False)