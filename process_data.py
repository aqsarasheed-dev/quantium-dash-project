import pandas as pd
import glob
import os

# 1. Define the data folder
data_folder = "data"

# 2. Find all CSV files
csv_files = glob.glob(os.path.join(data_folder, "*.csv"))

if not csv_files:
    print(f"ERROR: No CSV files found in the '{data_folder}' folder.")
    exit(1)

print(f"Found {len(csv_files)} CSV files. Starting processing...\n")

all_processed_data = []

for file_path in csv_files:
    # Read the CSV
    df = pd.read_csv(file_path)
    
    # Clean column names (just to be safe)
    df.columns = df.columns.str.strip().str.lower()
    
    # Clean the price column: remove '$' and convert to number
    df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
    
    # Convert quantity to number (just in case)
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    
    # Filter for ONLY "pink morsel" (SINGULAR - this was the bug!)
    pink_morsels = df[df['product'].str.strip().str.lower() == 'pink morsel'].copy()
    
    if len(pink_morsels) == 0:
        print(f"⚠️  No Pink Morsels found in {os.path.basename(file_path)}")
        print(f"   (Unique products: {df['product'].unique()[:3]})")
        continue
    
    # Calculate sales = quantity * price
    pink_morsels['sales'] = pink_morsels['quantity'] * pink_morsels['price']
    
    # Select only the 3 required columns
    final_columns = pink_morsels[['sales', 'date', 'region']]
    
    all_processed_data.append(final_columns)
    
    print(f"✅ Processed '{os.path.basename(file_path)}' -> Found {len(final_columns)} Pink Morsel sales.")

# Combine all processed data
if not all_processed_data:
    print("\n❌ ERROR: No Pink Morsels found in ANY file.")
    exit(1)

final_df = pd.concat(all_processed_data, ignore_index=True)

# Convert date to datetime and sort
final_df['date'] = pd.to_datetime(final_df['date'])
final_df = final_df.sort_values('date').reset_index(drop=True)

# Save to CSV
output_filename = "formatted_output.csv"
final_df.to_csv(output_filename, index=False)

print(f"\n✅ SUCCESS! Combined file saved as '{output_filename}'")
print(f"Total rows: {len(final_df)}")
print(f"Date range: {final_df['date'].min()} to {final_df['date'].max()}")
print(f"Regions: {final_df['region'].unique().tolist()}")