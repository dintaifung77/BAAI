import pandas as pd
from scipy.stats import pearsonr

# 1. Load the file
# Using 'utf-8-sig' handles the hidden characters Excel adds to CSVs
file_path = 'MBA Masters Thesis Survey- Stock copy.csv'
df = pd.read_csv(file_path, encoding='utf-8-sig')

# 2. Precise Mapping Function
# This function looks for keywords to ensure "1 - Novice" becomes 1 and "5 - Expert" becomes 5
def map_scale(val):
    v = str(val).strip()
    # Level 5
    if any(x in v for x in ['5', 'Expert', 'Very familiar', 'Very willing', 'Strongly agree']): return 5
    # Level 4
    if any(x in v for x in ['4', 'Somewhat familiar', 'Somewhat willing', 'Agree']): return 4
    # Level 3
    if any(x in v for x in ['3', 'Neutral', 'Neither', '中立']): return 3
    # Level 2
    if any(x in v for x in ['2', 'Not very familiar', 'Somewhat unwilling', 'Disagree']): return 2
    # Level 1
    if any(x in v for x in ['1', 'Novice', 'Not at all familiar', 'Very unwilling', 'Strongly disagree']): return 1
    return None

# 3. Create Numeric Columns
# Index 4 = Literacy, Index 9 = Familiarity, Index 10 = Willingness
df['Lit_Score'] = df.iloc[:, 4].apply(map_scale)
df['Fam_Score'] = df.iloc[:, 9].apply(map_scale)
df['Will_Score'] = df.iloc[:, 10].apply(map_scale)

# 4. Remove any rows with missing data to ensure a clean N=73
df_clean = df.dropna(subset=['Lit_Score', 'Fam_Score', 'Will_Score'])

# 5. Calculate Pearson Correlation (r) and P-Value
r_fam, p_fam = pearsonr(df_clean['Fam_Score'], df_clean['Will_Score'])
r_lit, p_lit = pearsonr(df_clean['Lit_Score'], df_clean['Will_Score'])

# 6. Print Results
print("-" * 30)
print(f"Analysis Results (Sample Size N = {len(df_clean)})")
print("-" * 30)
print(f"Crypto Familiarity vs Willingness:")
print(f"  Correlation (r): {r_fam:.3f}")
print(f"  P-value:         {p_fam:.5f}")
print("-" * 30)
print(f"Financial Literacy vs Willingness:")
print(f"  Correlation (r): {r_lit:.3f}")
print(f"  P-value:         {p_lit:.5f}")
print("-" * 30)


import pandas as pd
from scipy.stats import pearsonr

# 1. Load the file
df = pd.read_csv('MBA Masters Thesis Survey- Stock copy.csv', encoding='utf-8-sig')

# 2. Mapping Trust (Column 12)
# Logic: Yes = High Trust (3), Maybe = Neutral (2), No = Low Trust (1)
def map_trust(val):
    v = str(val).strip()
    if 'Yes' in v or '是' in v: return 3
    if 'Maybe' in v or '可能' in v: return 2
    if 'No' in v or '否' in v: return 1
    return None

# 3. Mapping Willingness (Column 10)
def map_willingness(val):
    v = str(val).strip()
    if 'Very willing' in v or '非常願意' in v: return 5
    if 'Somewhat willing' in v or '有些願意' in v: return 4
    if 'Neither' in v or '既不願意也不排斥' in v: return 3
    if 'Somewhat unwilling' in v or '有些不願意' in v: return 2
    if 'Very unwilling' in v or '非常不願意' in v: return 1
    return None

# 4. Apply mapping
df['Trust_Score'] = df.iloc[:, 12].apply(map_trust)
df['Will_Score'] = df.iloc[:, 10].apply(map_willingness)

# 5. Clean and Calculate
df_clean = df.dropna(subset=['Trust_Score', 'Will_Score'])
r_val, p_val = pearsonr(df_clean['Trust_Score'], df_clean['Will_Score'])

print(f"--- RQ3 Analysis Results (N={len(df_clean)}) ---")
print(f"Question: Trust in Banks vs. Crypto Willingness")
print(f"Correlation (r): {r_val:.3f}")
print(f"P-value:         {p_val:.5f}")
print("-" * 40)

# Interpretation logic
if p_val < 0.05:
    status = "Statistically Significant"
else:
    status = "Not Statistically Significant"

print(f"Result is {status}.")

import pandas as pd
from scipy.stats import pearsonr

# 1. Load the file
df = pd.read_csv('MBA Masters Thesis Survey- Stock copy.csv', encoding='utf-8-sig')

# 2. Mapping Stock Experience (Column 6) to 1-5 scale
def map_experience(val):
    v = str(val).strip()
    if '10 years or more' in v or '10 年或以上' in v: return 5
    if '7 to 10 years' in v or '7 至 10 年' in v: return 4
    if '4 to 6 years' in v or '4 至 6 年' in v: return 3
    if '1 to 3 years' in v or '1 至 3 年' in v: return 2
    if 'Less than 1 year' in v or '1 年以下' in v: return 1
    return None

# 3. Mapping Crypto Willingness (Column 10) to 1-5 scale
def map_willingness(val):
    v = str(val).strip()
    if 'Very willing' in v or '非常願意' in v: return 5
    if 'Somewhat willing' in v or '有些願意' in v: return 4
    if 'Neither' in v or '既不願意也不排斥' in v: return 3
    if 'Somewhat unwilling' in v or '有些不願意' in v: return 2
    if 'Very unwilling' in v or '非常不願意' in v: return 1
    return None

# 4. Apply the numeric mapping
df['Exp_Score'] = df.iloc[:, 6].apply(map_experience)
df['Will_Score'] = df.iloc[:, 10].apply(map_willingness)

# 5. Clean data (ensure we only use rows with both answers)
df_clean = df.dropna(subset=['Exp_Score', 'Will_Score'])

# 6. Calculate Pearson Correlation
r_val, p_val = pearsonr(df_clean['Exp_Score'], df_clean['Will_Score'])

print("-" * 50)
print(f"RQ2 Analysis Results (N = {len(df_clean)})")
print("-" * 50)
print(f"Stock Experience vs. Crypto Willingness:")
print(f"  Correlation (r): {r_val:.3f}")
print(f"  P-value:         {p_val:.5f}")
print("-" * 50)

# 7. Thesis Interpretation Logic
if p_val < 0.05:
    if r_val < 0:
        print("Finding: Significant negative correlation. More experience = Higher Skepticism.")
    else:
        print("Finding: Significant positive correlation. More experience = Lower Skepticism.")
else:
    print("Finding: No statistically significant relationship found.")