import pandas as pd
import numpy as np
import random
import math
import copy

roll = 22
mod_idx = roll % 3
threshold = 5.0

def generate(n):
    students = []
    for i in range(101, 101 + n):
        rec = {
            "id": i,
            "marks": random.randint(40, 95),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 20), random.randint(15, 30)]
        }
        students.append(rec)
    return students

def apply_mutation(d_list):
    divisor = mod_idx if mod_idx != 0 else 1
    for idx, student in enumerate(d_list):
        if idx % divisor == 0:
            student["marks"] = student["marks"] + math.sqrt(student["marks"])
            student["scores"][0] += 5 
            student["attendance"] = min(100, student["attendance"] + 2)

def calc_mean(d_frame):
    marks_list = d_frame["marks"].tolist()
    return sum(marks_list) / len(marks_list)

def analyze_drift(original_df, modified_df):
    original_mean = calc_mean(original_df)
    mod_mean = modified_df["marks"].mean()
    drift = abs(original_mean - mod_mean)
    std_dev = np.std(modified_df["marks"])
    return drift, std_dev

raw_data = generate(random.randint(10, 15))
original_df = pd.DataFrame(copy.deepcopy(raw_data))

shallow_data = list(raw_data)
deep_data = copy.deepcopy(raw_data)

apply_mutation(shallow_data)
apply_mutation(deep_data)

shallow_df = pd.DataFrame(shallow_data)
deep_df = pd.DataFrame(deep_data)

drift_val, current_std = analyze_drift(original_df, deep_df)

copy_failure = False
for i in range(len(raw_data)):
    if raw_data[i]["marks"] != original_df.iloc[i]["marks"]:
        copy_failure = True
        break

if copy_failure:
    status = "Copy Failure Detected"
elif drift_val > threshold:
    status = "Critical Drift"
elif drift_val > 0:
    status = "Minor Drift"
else:
    status = "Stable Data"

summary_tuple = (deep_df["marks"].mean(), drift_val, current_std)

print("--- ORIGINAL DATAFRAME ---")
print(original_df.head())
print("\n--- DRIFT ANALYSIS ---")
print(f"Calculated Drift: {drift_val:.2f}")
print(f"Status: {status}")
print(f"Summary (Mean, Drift, StdDev): {summary_tuple}")