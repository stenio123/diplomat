import csv
import os

# Define the folder to save the files
folder = "constraints"

# Create the folder if it doesn't exist
if not os.path.exists(folder):
    os.makedirs(folder)

# Read the CSV file
with open("CIS_GCP_Benchmarks.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip the first row
    for row in reader:
        filename = row[0] + ".py"
        filepath = os.path.join(folder, filename)
        with open(filepath, "w") as f:
            f.write(f"# CIS_NUMBER: {row[0]}\n# TITLE: {row[1]}\n")




