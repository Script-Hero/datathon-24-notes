import matplotlib.pyplot as plt
import pandas as pd
import os

# Get list of CSV files in Datasets directory
dataset_dir = 'Datasets'
csv_files = [f for f in os.listdir(dataset_dir) if f.endswith('.csv')]

# Create a figure with subplots for each column
fig, ax = plt.subplots(figsize=(12, 6))  # Single subplot for volume

# Plot volume data from each CSV file
for csv_file in csv_files:
    # Read CSV data
    df = pd.read_csv(os.path.join(dataset_dir, csv_file))
    
    # Ensure the first column is treated as datetime
    df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0])
    df.set_index(df.iloc[:, 0], inplace=True)
    
    # Plot volume data
    volume_col = [col for col in df.columns if 'volume' in col.lower()][0]  # Find volume column
    df[volume_col].plot(ax=ax, label=f'{csv_file} - {volume_col}')
    
    ax.set_title('Trading Volume Over Time')
    ax.grid(True)
    ax.legend()
    ax.set_xlabel('Date')
    ax.set_ylabel('Volume')

# Adjust layout and display
plt.tight_layout()
plt.show()



