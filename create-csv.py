# Import python library for CSV Files
import csv

# Import library for navigating your file system
import os
from pathlib import Path

# Navigating your file system
# ==============================
# YOUR_CSV_FILE = os.open("FULL_PATH_TO_FILE")
# ==============================
YOUR_CSV_FILE = Path.open("/Users/drewpage/Downloads/")

with open(YOUR_CSV_FILE, newline=" ") as csv_file:
    reader = csv.reader(csv_file, delimiter=",", quotechar="|")
    for row in reader:
        print(row)
