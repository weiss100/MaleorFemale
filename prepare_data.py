"""Convert lessR's dataBodyMeas.rda into data/body_measurements.csv.

Usage: python prepare_data.py path/to/dataBodyMeas.rda
Requires: pip install pyreadr
(.rda from https://github.com/dgerbing/lessR/blob/master/data/dataBodyMeas.rda)
"""
import csv
import sys

import pyreadr

IN_TO_CM = 2.54
LB_TO_KG = 0.45359237

# The raw "Shoe" column is a US size on a *different scale per sex* (men's vs.
# women's sizing). Used as is, it would leak the label. We map both to a common
# EU size (one US step = 1/3 inch = about 1.27 Paris points).
def shoe_eu(us_size, gender):
    offset = 30.6 if gender == "M" else 28.7
    return round(1.27 * us_size + offset)


df = list(pyreadr.read_r(sys.argv[1]).values())[0]
with open("data/body_measurements.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["height_cm", "weight_kg", "shoe_size_eu", "gender"])
    for _, r in df.iterrows():
        w.writerow([
            round(r.Height * IN_TO_CM),
            round(r.Weight * LB_TO_KG),
            shoe_eu(r.Shoe, r.Gender),
            "male" if r.Gender == "M" else "female",
        ])
