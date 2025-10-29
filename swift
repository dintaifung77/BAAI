import matplotlib.pyplot as plt

# Assumptions
swift_volume = 150_000_000_000_000  # $150 trillion annual SWIFT volume
prefunding_ratio = 0.02  # assume 2% of transaction value is locked in nostro accounts

# XRP market share scenarios (% of SWIFT payments)
shares = [5, 10, 14, 20]  # in percent
freed_capital = [(swift_volume * (s / 100) * prefunding_ratio) / 1e12 for s in shares]  # in trillion USD

# Create bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar([f"{s}%" for s in shares], freed_capital, color=['#0080FF', '#33A1FF', '#66C2FF', '#99DFFF'])
plt.title("Estimated Capital Freed from Nostro Accounts\nif XRP Processes Part of SWIFT Payment Volume")
plt.xlabel("XRP Share of SWIFT Payment Volume")
plt.ylabel("Capital Freed (Trillions of USD)")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate values
for bar, val in zip(bars, freed_capital):
    plt.text(bar.get_x() + bar.get_width()/2, val + 0.05, f"{val:.2f}", ha='center', fontsize=10)

plt.tight_layout()
plt.show()
