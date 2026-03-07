import pandas as pd
from scipy.stats import pearsonr

# 1. Load your file (ensure the filename matches exactly)
file_path = 'MBA Masters Thesis Survey- Stock copy.csv' 
df = pd.read_csv(file_path)

# 2. Define the Mapping Function (Converts text answers to 1-5 numbers)
def map_to_numeric(val):
    val = str(val)
    if '5' in val or 'Very' in val or 'Strongly' in val or 'Expert' in val: return 5
    if '4' in val or 'Somewhat' in val or 'Agree' in val: return 4
    if '3' in val or 'Neutral' in val or 'Neither' in val: return 3
    if '2' in val or 'Not very' in val or 'Disagree' in val: return 2
    if '1' in val or 'Not at all' in val or 'Novice' in val: return 1
    return None

# 3. Create the numeric columns
# Change the column indices if your spreadsheet layout changed
df['Willingness'] = df.iloc[:, 10].apply(map_to_numeric) # Column 11
df['Familiarity'] = df.iloc[:, 9].apply(map_to_numeric)  # Column 10
df['Literacy'] = df.iloc[:, 4].apply(map_to_numeric)     # Column 5

# 4. Clean data (Remove empty rows)
df_clean = df.dropna(subset=['Willingness', 'Familiarity', 'Literacy'])

# 5. Calculate r and p for RQ4
r_fam, p_fam = pearsonr(df_clean['Familiarity'], df_clean['Willingness'])
r_lit, p_lit = pearsonr(df_clean['Literacy'], df_clean['Willingness'])

print(f"Crypto Familiarity: r = {r_fam:.3f}, p = {p_fam:.5f}")
print(f"Financial Literacy: r = {r_lit:.3f}, p = {p_lit:.5f}")