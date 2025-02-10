#fifth
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the rectified dataset
file_path = "S1_E2_A1_rectified.csv"  # Replace with your actual path
df_filtered = pd.read_csv(file_path)

# Identify EMG columns (first 12 channels)
emg_channels = [col for col in df_filtered.columns if "EMG" in col][:12]

# Sampling frequency
Fs = 1000  # Hz (assumed)
window_size_ms = 50  # Window size in milliseconds
window_size_samples = int(Fs * (window_size_ms / 1000))  # Convert window size to samples

# Function to compute RMS envelope with a moving average window
def rms_envelope(signal, window_size):
    squared_signal = np.power(signal, 2)  # Square the signal
    window = np.ones(window_size) / window_size
    rms_signal = np.sqrt(np.convolve(squared_signal, window, mode='same'))  # Compute moving RMS
    return rms_signal

# Generate time array for plotting
time = np.arange(len(df_filtered)) / Fs  # Time in seconds

# Plot all 12 EMG signals in a single figure (6x2 grid layout)
fig, axes = plt.subplots(nrows=6, ncols=2, figsize=(15, 20), sharex=True)
axes = axes.flatten()

for i, emg in enumerate(emg_channels):
    rectified_signal = df_filtered[emg]  # Rectified signal
    rms_signal = rms_envelope(rectified_signal, window_size_samples)  # Compute RMS envelope
    
    # Plot Rectified Signal (Red)
    axes[i].plot(time, rectified_signal, label="Rectified sEMG", color='red', linewidth=0.5)
    
    # Plot RMS Envelope (Blue, Dashed)
    axes[i].plot(time, rms_signal, label="RMS Feature", color='blue', linestyle='--', linewidth=1.5)
    
    # Formatting
    axes[i].set_title(f"{emg} - Rectified sEMG & RMS Feature", fontsize=12)
    axes[i].set_ylabel("sEMG (mV)", fontsize=10)
    axes[i].legend(loc="upper right", fontsize="small")
    axes[i].grid(True)

# Set common x-axis label
axes[-1].set_xlabel("Time (seconds)", fontsize=12)

# Plot title
plt.suptitle("Rectified sEMG and RMS Feature for 12 Electrodes", fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()
