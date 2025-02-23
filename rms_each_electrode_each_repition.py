#calculate rms for each repitition per action
import pandas as pd
import numpy as np

# Load the CSV file
input_file = "S1_E1_A1_action_5.csv"  # Replace with your actual filename
df = pd.read_csv(input_file)

# Define column indices
repetition_column = df.columns[2]  # Column 3 (Repetition Identifier)
emg_columns = df.columns[4:16]  # Columns 5 to 16 (12 electrodes)

# Group by repetition and compute RMS for each electrode separately
rms_per_repetition = df.groupby(repetition_column)[emg_columns].apply(lambda x: x.apply(lambda y: np.sqrt(np.mean(y**2))))

# Reset index for better structure
rms_per_repetition = rms_per_repetition.reset_index()

# Save RMS values to CSV (Optional)
rms_per_repetition.to_csv("rms_values_action5_by_repitition.csv", index=False)

print("RMS values calculated and saved as 'rms_values_action5_by_repitition.csv'.")
