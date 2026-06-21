import pandas as pd
import glob
import os

# Look for CSV files in the data folder
data_folder = "data"
csv_files = glob.glob(os.path.join(data_folder, "*.csv"))

if not csv_files:
    print("No CSV files found in 'data' folder!")
    exit()

for file in csv_files:
    print(f"\n{'='*50}")
    print(f"File: {os.path.basename(file)}")
    print('='*50)
    
    # Read first file to inspect
    df = pd.read_csv(file)
    
    print("Column names:", df.columns.tolist())
    print(f"Total rows: {len(df)}")
    print("\nFirst 3 rows:")
    print(df.head(3))
    print("\nUnique product values:")
    print(df['product'].unique() if 'product' in df.columns else "'product' column NOT found!")