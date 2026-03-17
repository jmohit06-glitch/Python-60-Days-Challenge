transactions = [1200, 450, 3000, -50, 50, 2500, 1800, 4000]

categories = {
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": [],
}

for amount in transactions:
    if amount <= 0:
        categories["invalid"].append(amount)
    elif 1 <= amount <= 500:
        categories["normal"].append(amount)
    elif 501 <= amount <= 2000:
        categories["large"].append(amount)
    else:
        categories["high_risk"].append(amount)

valid = [amount for amount in transactions if amount > 0]

total = sum(valid)
count = len(valid)
high_risk_count = len(categories["high_risk"])

if high_risk_count >= 3:
    level = "High Risk"
elif total > 5000 or count > 5:
    level = "Moderate Risk"
else:
    level = "Low Risk"

summary = (total, count, level)

print("--- RISK ANALYSIS REPORT ---")
print(f"Categories: {categories}")
print(f"Total Value: {summary[0]}")
print(f"Total Transactions: {summary[1]}")
print(f"Final Result: {summary[2]}")
