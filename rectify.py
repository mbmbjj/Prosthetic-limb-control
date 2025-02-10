#Fourth file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the bandpass-filtered dataset
file_path = "S1_E2_A1_filtered.csv"  # Update this if needed
df_filtered = pd.read_csv(file_path)

# Identify EMG columns (first 12 channels)
emg_channels = [col for col in df_filtered.columns if "EMG" in col][:12]

# Identify the last four columns (stimulus, restimulus, repetition, rerepetition)
last_four_columns = df_filtered.columns[-4:].tolist()  # Select the last four columns dynamically

# Sampling frequency
Fs = 1000  # Hz (Assumed)
time = np.arange(len(df_filtered)) / Fs  # Generate time array in seconds

# Rectify the EMG signals (absolute value)
df_rectified = df_filtered.copy()
df_rectified[emg_channels] = np.abs(df_filtered[emg_channels])

# Keep the last four columns in the saved CSV
df_rectified = df_rectified[emg_channels + last_four_columns]

# Save rectified data to CSV
output_file = "S1_E2_A1_rectified.csv"
df_rectified.to_csv(output_file, index=False)
print(f"Rectified EMG data saved as: {output_file}")

# Plot all 12 rectified EMG signals in a single figure
fig, axes = plt.subplots(nrows=6, ncols=2, figsize=(15, 20), sharex=True)
axes = axes.flatten()  # Flatten for easy iteration

for i, emg in enumerate(emg_channels):
    axes[i].plot(time, df_rectified[emg], label=f"{emg} (Rectified)", color='b')
    axes[i].set_title(f"Rectified EMG - {emg}", fontsize=12)
    axes[i].set_xlabel("Time (seconds)", fontsize=10)
    axes[i].set_ylabel("Voltage (mV)", fontsize=10)
    axes[i].legend(loc="upper right", fontsize="small")
    axes[i].grid(True)

# Set common x-axis label
axes[-1].set_xlabel("Time (seconds)", fontsize=12)

plt.suptitle("Rectified EMG Signals for 12 Electrodes", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

