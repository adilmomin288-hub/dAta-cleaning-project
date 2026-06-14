import os

import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "Data", "customers-100.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "cleaned_customers.csv")

if os.path.exists(OUTPUT_DIR) and not os.path.isdir(OUTPUT_DIR):
    os.remove(OUTPUT_DIR)

os.makedirs(OUTPUT_DIR, exist_ok=True)


df = pd.read_csv(DATA_FILE)

print("Original Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

df = df.drop_duplicates()

for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()

df.to_csv(OUTPUT_FILE, index=False)

print("\nFinal Shape:", df.shape)
print("\nCleaning Completed Successfully")
