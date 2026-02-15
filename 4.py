
reg = int(input("Enter your Register Number: "))
D = reg % 10
print("Register Digit (D):", D)

n = int(input("Enter the number of activity scores: "))
scores = []
for i in range(n):
    score = int(input("Enter activity score: "))
    scores.append(score)

low_risk = []
med_risk = []
high_risk = []
crit_risk = []

valid = 0
ignored = 0
removed = 0

for score in scores:
    if score < 0:
        ignored += 1
    else:
        valid += 1
        if score <= 30:
            low_risk.append(score)
        elif score <= 60:
            med_risk.append(score)
        elif score <= 100:
            high_risk.append(score)
        else:
            crit_risk.append(score)

print("\nLow Risk:", low_risk)
print("Medium Risk:", med_risk)
print("High Risk:", high_risk)
print("Critical Risk:", crit_risk)

if D % 2 == 0:
    for item in low_risk:
        removed += 1
    low_risk = []
else:
    for item in crit_risk:
        removed += 1
    crit_risk = []

print("\nAfter Personalized Filtering:")
print("Low Risk:", low_risk)
print("Medium Risk:", med_risk)
print("High Risk:", high_risk)
print("Critical Risk:", crit_risk)

print("\nTotal Valid Entries:", valid)
print("Ignored Entries:", ignored)
print("Removed Due to Personalization:", removed)