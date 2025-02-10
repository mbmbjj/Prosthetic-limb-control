import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset (replace with your dataset file)
df = pd.read_csv("S1_E2_A1.csv")  # Ensure the file has EMG_1 to EMG_12 columns

# Sampling frequency
Fs = 1000  # Sampling frequency in Hz

# Identify EMG columns
emg_channels = [col for col in df.columns if "EMG" in col]

# Plot FFT for all EMG channels
plt.figure(figsize=(15, 10))

for i, channel in enumerate(emg_channels):
    # Extract signal
    x = df[channel].values
    L = len(x)  # Length of the signal

    # FFT computation
    Y = np.fft.fft(x)
    P2 = np.abs(Y / L)  # Two-sided spectrum
    P1 = P2[:L // 2 + 1]  # Single-sided spectrum
    P1[1:-1] = 2 * P1[1:-1]  # Adjust amplitude
    f = Fs * np.arange(0, L // 2 + 1) / L  # Frequency axis

    # Plot each FFT
    plt.subplot(4, 3, i + 1)  # Adjust subplot grid (4 rows, 3 columns for 12 channels)
    plt.plot(f, P1)
    plt.title(f"Frequency Spectrum - {channel}")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("|P1(f)|")
    plt.grid()

# Show all plots
plt.tight_layout()
plt.show()