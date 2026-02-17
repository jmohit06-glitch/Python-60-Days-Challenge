full_name = input("Enter your full name: ")
L = 0
for c in full_name:
    if c != " ":
        L += 1

PLI = L % 3
print("Name Length (L):", L)
print("Personalization Logic Index (PLI):", PLI)

n = int(input("Enter number of resource requests to process: "))
requests = []
for i in range(n):
    val = int(input("Enter request value: "))
    requests.append(val)

low = []
moderate = []
high = []
invalid = []

valid = 0
removed = 0

for r in requests:
    if r < 0:
        invalid.append(r)
    else:
        valid += 1
        if r == 0:
            pass 
        elif r <= 20:
            low.append(r)
        elif r <= 50:
            moderate.append(r)
        else:
            high.append(r)


if PLI == 0:
    for item in low:
        removed += 1
    low = []
    print("\nRule A Applied: Removed all Low Demand requests.")

elif PLI == 1:
    for item in high:
        removed += 1
    high = []
    print("\nRule B Applied: Removed all High Demand requests.")

elif PLI == 2:
    for item in low:
        removed += 1
    low = []
    for item in high:
        removed += 1
    high = []
    print("\nRule C Applied: Kept only Moderate Demand. Removed Low and High.")

print("Low Demand:", low)
print("Moderate Demand:", moderate)
print("High Demand:", high)
print("Invalid Requests (Ignored):", invalid)

print("\nTotal Valid Requests:", valid)
print("Total Removed via PLI:", removed)