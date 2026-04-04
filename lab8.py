import csv
import math

# 1. Setup Personalized Values & Filenames

d1 = 0
d2 = 7
k = 5
shift = -7
rows_keep = 2

osc_file = "oscillatory_2585070.csv"
stand_file = "standing_2585070.csv"
new_osc_file = "oscillatory_personalized_2585070.csv"
new_stand_file = "standing_personalized_2585070.csv"



# 2. Read and Calculate: Oscillatory Data

print("--- Processing Oscillatory Data ---")
amplitudes = []

with open(osc_file, 'r') as file:
    reader = csv.reader(file)
    next(reader) # Skip the header row
    
    for row in reader:
        amp = float(row[1]) # Column 2 is amplitude
        amplitudes.append(amp)

mean_amp = sum(amplitudes) / len(amplitudes)
max_amp = max(amplitudes)
print(f"Mean Amplitude: {mean_amp}")
print(f"Max Amplitude: {max_amp}\n")



# 3. Read and Calculate: Standing Wave Data

print("--- Processing Standing Wave Data ---")
speeds = []

with open(stand_file, 'r') as file:
    reader = csv.reader(file)
    next(reader) # Skip the header row
    
    for row in reader:
        tension = float(row[1]) # Column 2 is tension
        v = math.sqrt(tension / 1)
        speeds.append(v)

print(f"Wave Speeds: {speeds}\n")



# 4. Create Personalized Oscillatory File

print("--- Creating Personalized Files ---")
new_osc_data = []
row_limit = 5 + d2  # Keep 12 rows

with open(osc_file, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    new_osc_data.append(header) # Save header for the new file
    
    row_count = 0
    for row in reader:
        if row_count < row_limit:
            length = float(row[0])
            new_amplitude = float(row[1]) + shift  # Add the shift
            
            new_osc_data.append([length, new_amplitude])
            row_count += 1

# Write the new data to a file
with open(new_osc_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_osc_data)
print(f"Saved: {new_osc_file}")



# 5. Create Personalized Standing File

new_stand_data = []
row_limit = 4 + rows_keep # Keep 6 rows

with open(stand_file, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    new_stand_data.append(header) # Save header for the new file
    
    row_count = 0
    for row in reader:
        if row_count < row_limit:
            length = float(row[0])
            new_tension = float(row[1]) * k  # Multiply by k
            
            new_stand_data.append([length, new_tension])
            row_count += 1

# Write the new data to a file
with open(new_stand_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_stand_data)
print(f"Saved: {new_stand_file}")