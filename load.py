# -*- coding: utf-8 -*-
"""load

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zITtWnkWt498yJqZCFT0sNqnihSas2Bz
"""
import subprocess
import sys
import pandas as pd

# Check if the user provided a file path as an argument
if len(sys.argv) != 2:
    print("Usage: python load.py <file_path>")
    sys.exit(1)

# Get the file path from the command-line argument
file_path = sys.argv[1]

try:
    # Read the dataset file using Pandas
    df = pd.read_csv(file_path)  # You can adjust the format (e.g., read_excel) based on your dataset format

    # Perform operations on the DataFrame (e.g., print the first few rows)
    print(df.head())

except FileNotFoundError:
    print(f"File not found: {file_path}")

except Exception as e:
    print(f"An error occurred: {e}")
    
subprocess.run(["python3", "dpre.py", "titanic.csv"])
