# Training data

`body_measurements.csv`: 340 rows (170 men, 170 women), columns `height_cm`, `weight_kg`, `shoe_size_eu`, `gender`.

## Source

`dataBodyMeas` from the R package [lessR](https://github.com/dgerbing/lessR) (David Gerbing, GPL >= 2).
Body measurements of 170 women and 170 men who purchased motorcycle clothing.
Converted with `prepare_data.py`.

## Preprocessing

- Height in inches to cm, weight in pounds to kg (rounded to integers).
- The original shoe size is a US size on separate men's and women's scales. The same number means a
  different foot length per sex, so using it raw would leak the label. `prepare_data.py` converts both
  to an approximate EU size (rounded). This is a rule of thumb, not an exact size chart.

## Limitations

- Not a random sample of the population: motorcycle clothing buyers, presumably mostly in the US.
- Binary gender label only, and the sex split is exactly 50/50 by construction.
- Contains outliers (e.g. a man with 220 kg); they were kept.
