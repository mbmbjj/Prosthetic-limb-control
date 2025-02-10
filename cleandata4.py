#second file
#ONly save csv, nothing will be shown ++ bring restimulus and repetition
import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt

# Load the original dataset
df = pd.read_csv("S1_E2_A1.csv")  # Ensure this file contains EMG_1 to EMG_12 and extra columns

# Sampling frequency
Fs = 1000  # Hz

# Identify EMG columns (first 12 channels)
emg_channels = [col for col in df.columns if "EMG" in col][:12]

# Identify extra columns to retrieve
extra_columns = ["Stimulus", "Restimulus", "Repetition", "Rerepetition"]

# Ensure the extra columns exist in the dataset
extra_columns = [col for col in extra_columns if col in df.columns]  # Avoid errors if missing

# Bandpass Filter Function (5-300 Hz)
def bandpass_filter(signal, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, signal)

# Filter settings
lowcut = 5    # Hz
highcut = 300 # Hz

# Apply bandpass filtering to all EMG channels using NumPy (vectorized)
filtered_signals = np.apply_along_axis(lambda x: bandpass_filter(x, lowcut, highcut, Fs), axis=0, arr=df[emg_channels].values)

# Create a new DataFrame for filtered EMG signals
df_filtered = pd.DataFrame(filtered_signals, columns=emg_channels)

# Retrieve and add extra columns from the original dataset
for col in extra_columns:
    df_filtered[col] = df[col].values  # Ensures correct alignment

# Reorder the DataFrame to maintain the original column order
df_filtered = df_filtered[emg_channels + extra_columns]

# Save the cleaned EMG data along with the extra columns
df_filtered.to_csv("S1_E2_A1_filtered.csv", index=False)

print("✅ Filtered data successfully saved as 'S1_E2_A1_filtered.csv' with all extra columns included.")