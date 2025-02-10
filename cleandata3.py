import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Load the dataset
df = pd.read_csv("S1_E2_A1.csv")  # Ensure this file contains EMG_1 to EMG_12 columns

# Sampling frequency
Fs = 1000  # Hz

# Identify EMG columns (first 12 channels)
emg_channels = [col for col in df.columns if "EMG" in col][:12]

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

# Create a DataFrame to store only the filtered EMG signals
df_filtered = pd.DataFrame()

# Initialize a figure for plotting
plt.figure(figsize=(18, 20))

# Loop through each EMG channel for filtering, visualization, and saving
for i, channel in enumerate(emg_channels):
    # Extract raw signal
    raw_signal = df[channel].values

    # Apply bandpass filter
    filtered_signal = bandpass_filter(raw_signal, lowcut, highcut, Fs)

    # Store only the filtered signal in the new DataFrame
    df_filtered[channel] = filtered_signal

    # FFT computation for raw signal
    L = len(raw_signal)
    Y_raw = np.fft.fft(raw_signal)
    P2_raw = np.abs(Y_raw / L)
    P1_raw = P2_raw[:L // 2 + 1]
    P1_raw[1:-1] = 2 * P1_raw[1:-1]
    f = Fs * np.arange(0, L // 2 + 1) / L

    # FFT computation for filtered signal
    Y_filt = np.fft.fft(filtered_signal)
    P2_filt = np.abs(Y_filt / L)
    P1_filt = P2_filt[:L // 2 + 1]
    P1_filt[1:-1] = 2 * P1_filt[1:-1]

    # Plot raw signal FFT
    #plt.subplot(12, 2, 2 * i + 1)
    #plt.plot(f, P1_raw, color='r')
    #plt.title(f"Raw FFT - {channel}")
    #plt.xlabel("Frequency (Hz)")
    #plt.ylabel("|P1(f)|")
    #plt.grid(True)

    # Plot filtered signal FFT
    #plt.subplot(12, 2, 2 * i + 2)
    #plt.plot(f, P1_filt, color='b')
    #plt.title(f"Filtered FFT (5-300 Hz) - {channel}")
    #plt.xlabel("Frequency (Hz)")
    #plt.ylabel("|P1(f)|")
    #plt.grid(True)

# Adjust layout to prevent overlap
#plt.tight_layout()
#plt.show()

# Save ONLY the filtered data
print("!")
df_filtered.to_csv("S1_E2_A1_filtered.csv", index=False)
print("sfkl")
print("Filtered data saved successfully as 'S1_E2_A1_filtered.csv'.")
