import pandas as pd
import matplotlib.pyplot as plt
import re
import os

txt_path = "slice_output.txt"
project_path = os.path.dirname(__file__)

with open(txt_path, "r") as f:
    lines = f.readlines()

data = []

current_feature = None
for line in lines:
    line = line.strip()
    if line == "":
        continue
        
    m = re.match(r"(\w[\w\-]*):\s*(.*), Count: (\d+)", line)
    if m:
        current_feature = m.group(1)
        value = m.group(2)
        count = int(m.group(3).replace(",", ""))
        data.append({
            "feature": current_feature,
            "value": value,
            "count": count,
            "precision": None,
            "recall": None,
            "f1": None
        })
        continue

    m = re.match(r"Precision:\s*([\d\.]+)\s*\|\s*Recall:\s*([\d\.]+)\s*\|\s*F1:\s*([\d\.]+)", line)
    if m and data:
        data[-1]["precision"] = float(m.group(1))
        data[-1]["recall"] = float(m.group(2))
        data[-1]["f1"] = float(m.group(3))

df = pd.DataFrame(data)

features = df['feature'].unique()
for feature in features:
    sub_df = df[df['feature'] == feature].sort_values('value')
    plt.figure(figsize=(10, 6))
    plt.bar(sub_df['value'], sub_df['f1'], color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel(feature)
    plt.ylabel('F1 Score')
    plt.title(f'F1 Score by {feature}')
    plt.tight_layout()
    
    png_path = os.path.join(project_path, f"bias_{feature}.png")
    plt.savefig(png_path)
    plt.close()
    print(f"Saved plot for {feature} at {png_path}")
