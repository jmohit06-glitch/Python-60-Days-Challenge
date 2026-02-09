n = int(input("Enter number of students: "))
roll = int(input("Enter your Register Number: "))

marks = []

if roll % 2 == 0:
    for i in range(n):
        mark = int(input("Enter mark: "))
        marks.append(mark + 5)
else:
    for i in range(n):
        mark = int(input("Enter mark: "))
        marks.append(mark - 5)

valid_count = 0
failed_count = 0

for m in marks:
    category = ""
    
    if m < 0 or m > 100:
        category = "Invalid"
    elif m >= 90:
        category = "Excellent"
        valid_count += 1
    elif m >= 75:
        category = "Very Good"
        valid_count += 1
    elif m >= 60:
        category = "Good"
        valid_count += 1
    elif m >= 40:
        category = "Average"
        valid_count += 1
    else:
        category = "Fail"
        valid_count += 1
        failed_count += 1
    
    print("Mark:", m, "→", category)

print("\nFinal Summary:")
print("Total Valid Students:", valid_count)
print("Total Failed Students:", failed_count)