# Example Analysis Script

import pandas as pd

def analyze_data(file_path):
    data = pd.read_csv(file_path)
    # Perform analysis
    results = data.describe()
    print(results)

analyze_data("Data/RawData/sample_data.csv")

