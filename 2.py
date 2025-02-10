#first file - mat to csv file

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

# 🔹 Define actual file path
mat_file = r"D:\TJ-SIF\ml\parn\path_to_mat_files\S1_E1_A1.mat"  # Change this to the correct path

# 🔹 Check if the file exists
if not os.path.exists(mat_file):
    print(f"❌ Error: File '{mat_file}' not found!")
    exit()  # Stop execution if file is missing

# 🔹 Load the MAT file
mat_data = loadmat(mat_file)
print("✅ MAT File Loaded Successfully!")
print("🔹 Available Keys in MAT File:", mat_data.keys())  # Shows all variables stored in the .mat file

# 🔹 Extract Data (Checking if Keys Exist)
emg_data = mat_data.get('emg', None)  # 12 columns (sEMG signals)
acc_data = mat_data.get('acc', None)  # 36 columns (Accelerometer)
glove_data = mat_data.get('glove', None)  # 22 columns (Cyberglove)
stimulus = mat_data.get('stimulus', None)  # 1 column (Movement label)
restimulus = mat_data.get('restimulus', None)  # 1 column (Refined label)
repetition = mat_data.get('repetition', None)  # 1 column (Repetitions)
rerepetition = mat_data.get('rerepetition', None)  # 1 column (Repetition refinement)
force = mat_data.get('force', None)  # 6 columns (Force signals)

# 🔹 Convert Each Data Array to DataFrame (if not None)
df_emg = pd.DataFrame(emg_data, columns=[f"EMG_{i+1}" for i in range(12)]) if emg_data is not None else None
df_acc = pd.DataFrame(acc_data, columns=[f"ACC_{i+1}" for i in range(36)]) if acc_data is not None else None
df_glove = pd.DataFrame(glove_data, columns=[f"Glove_{i+1}" for i in range(22)]) if glove_data is not None else None
df_stimulus = pd.DataFrame(stimulus, columns=["Stimulus"]) if stimulus is not None else None
df_restimulus = pd.DataFrame(restimulus, columns=["Restimulus"]) if restimulus is not None else None
df_repetition = pd.DataFrame(repetition, columns=["Repetition"]) if repetition is not None else None
df_rerepetition = pd.DataFrame(rerepetition, columns=["Rerepetition"]) if rerepetition is not None else None
df_force = pd.DataFrame(force, columns=[f"Force_{i+1}" for i in range(6)]) if force is not None else None

# 🔹 Combine All Available DataFrames into One
df_list = [df_emg, df_acc, df_glove, df_stimulus, df_restimulus, df_repetition, df_rerepetition, df_force]
df_list = [df for df in df_list if df is not None]  # Remove None values
df = pd.concat(df_list, axis=1)

# 🔹 Check Final Data Shape
print(f"✅ Final Data Shape: {df.shape}")  # Should match expected columns

# 🔹 Save to CSV
csv_file = "S1_E1_A1.csv"
df.to_csv(csv_file, index=False)
print(f"✅ Full dataset saved as '{csv_file}'")

# 🔹 Display Data Overview
print("\n🔹 First 5 Rows of Data:")
print(df.head())

# 🔹 Check Data Types
print("\n🔹 Data Types:")
print(df.dtypes)

# 🔹 Check Unique Values in Each Column (Detect Labels)
print("\n🔹 Unique Values per Column:")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

# 🔹 Plot Sample EMG Data
if df_emg is not None:
    plt.figure(figsize=(12, 5))
    plt.plot(df_emg.iloc[:, 0], label="EMG Sensor 1")  # Change index to check other sensors
    plt.title("Sample EMG Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()

print("✅ Data Processing Complete! 🚀")
