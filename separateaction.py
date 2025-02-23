#sixth separate only action 5 and 6
import pandas as pd

# Define the input and output file paths
input_file = "S3_E1_A1_rectified.csv"  # Replace with the actual file path if needed
output_file = "S3_E1_A1_separated.csv"  # New file to save the filtered data

# Load the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Check if the necessary columns exist in the DataFrame
required_columns = {'Stimulus', 'Restimulus', 'Repetition', 'Rerepetition'}
if not required_columns.issubset(df.columns):
    print(f"Error: Missing one or more required columns in {input_file}.")
else:
    # Filter rows where 'Restimulus' is either 5 or 6
    filtered_df = df[df['Restimulus'].isin([5, 6])]

    # Select EMG columns along with required metadata columns
    emg_columns = [col for col in df.columns if "EMG" in col]  # Select all EMG signal columns
    selected_columns = ['Stimulus', 'Restimulus', 'Repetition', 'Rerepetition'] + emg_columns

    # Keep only the required columns
    filtered_df = filtered_df[selected_columns]

    # Save the filtered DataFrame to a new CSV file
    filtered_df.to_csv(output_file, index=False)

    print(f"Filtered data saved to {output_file}")
