import csv
import json
import ast

input_file = "final_data.csv"
output_file = "data.json"

data = []

with open(input_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        try:
            tokens = ast.literal_eval(row["tokens"])
            event_tags = ast.literal_eval(row["event_tags"])
            pos_tags = ast.literal_eval(row["pos_tags"])
            dep_tags = ast.literal_eval(row["dep_tags"])
            
            # sanity check
            if not (len(tokens) == len(event_tags) == len(pos_tags) == len(dep_tags)):
                print(f"Length mismatch at row {row['id']}")
                continue
            
            data.append({
                "type": row["type"],
                "tokens": tokens,
                "tags": event_tags,
                "pos_tags": pos_tags,
                "dep_tags": dep_tags
            })
        
        except Exception as e:
            print(f"Error at row {row['id']}: {e}")

# write JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Conversion complete!")
