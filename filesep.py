#Separate the data - restimulus and rerepetition
import pandas as pd
import os

# Load dataset
df = pd.read_csv("S1_E2_A1.csv")  # Update with your correct file path

# Clean column names (remove spaces, lowercase)
df.columns = df.columns.str.strip().str.lower()

# Define EMG columns (EMG_1 to EMG_12)
emg_columns = [f"emg_{i}" for i in range(1, 13)]

# Check if all required EMG columns exist
missing_columns = [col for col in emg_columns if col not in df.columns]
if missing_columns:
    print(f"Error: Missing EMG columns: {missing_columns}")
    exit()

# Ensure restimulus & rerepetition exist
if 'restimulus' not in df.columns or 'rerepetition' not in df.columns:
    print("Error: Missing required columns ('restimulus' or 'rerepetition')")
    exit()

# Create a directory for output files
output_dir = "processed_emg_data"
os.makedirs(output_dir, exist_ok=True)

# Extract & save each unique (restimulus, rerepetition) subset
unique_combinations = df[['restimulus', 'rerepetition']].drop_duplicates()

for _, row in unique_combinations.iterrows():
    restim = int(row['restimulus'])  # Convert to integer for readability
    rerep = int(row['rerepetition'])

    # Skip rest periods (restimulus = 0 means no movement)
    if restim == 0:
        continue  

    # Filter dataset for this combination
    subset = df[(df['restimulus'] == restim) & (df['rerepetition'] == rerep)]

    # Keep only EMG_1 to EMG_12
    subset = subset[emg_columns]

    # Define filename and save CSV
    filename = os.path.join(output_dir, f"resti_{restim}_rerepet_{rerep}.csv")
    subset.to_csv(filename, index=False)
    print(f"Saved: {filename}")
