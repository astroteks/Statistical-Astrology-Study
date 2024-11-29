# Advanced Analysis Script

import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(file_path):
    data = pd.read_csv(file_path)
    # Perform data preparation
    data["Outcome"] = data["Outcome"].map({"Positive": 1, "Neutral": 0, "Negative": -1})
    # Calculate basic statistics
    summary = data.groupby("Sign")["Outcome"].mean()
    print(summary)
    # Simple visualization
    summary.plot(kind="bar")
    plt.title("Average Outcomes by Sign")
    plt.xlabel("Sign")
    plt.ylabel("Average Outcome")
    plt.tight_layout()
    plt.show()

analyze_data("Data/RawData/full_sample_data.csv")

