
import pandas as pd
import matplotlib.pyplot as plt

# Data as a list of dictionaries
data = [
    {"Batch#": "Batch1-A_B-599999-539901-03-21", "Initial Number": 46648, "In-House": 6401, "Bouncer": 1636, "DeBounce": 1352},
    {"Batch#": "Batch1-C-541103-03/22", "Initial Number": 46799, "In-House": 3046, "Bouncer": 357, "DeBounce": 258},
    {"Batch#": "Batch1-D-541105-03/22-3PM", "Initial Number": 94603, "In-House": 1697, "Bouncer": 351, "DeBounce": 319}
]

# Load data into a pandas DataFrame
df = pd.DataFrame(data)

# Extract batch names from the "Batch#" column (assuming they are the first part before any numbers)
df["Batch Name"] = df["Batch#"].str.split().str[0]

# Plot the data (excluding "Initial Number")
df.drop("Initial Number", axis=1).plot(x="Batch Name", kind="bar", stacked=False)

# Customize the plot
plt.title("Batch Processing Results")
plt.xlabel("Batch Name")
plt.ylabel("Count")
plt.legend(title="Processing Stage")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

plt.show()