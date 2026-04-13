import csv
import ast

input_file = "ipl_tagged_manual_correct.csv"
output_file = "final_data.csv"

rows = []

with open(input_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        tokens = ast.literal_eval(row["tokens"])
        
        # Check if event_tags is empty or missing
        if row["event_tags"].strip() == "" or row["event_tags"] == "[]":
            tags = ["O"] * len(tokens)
        else:
            try:
                tags = ast.literal_eval(row["event_tags"])
                
                # If mismatch, fix it
                if len(tags) != len(tokens):
                    print(f"Fixing mismatch at row {row['id']}")
                    tags = ["O"] * len(tokens)
            except:
                print(f"Error parsing tags at row {row['id']}, filling with O")
                tags = ["O"] * len(tokens)
        
        # Save back as string
        row["event_tags"] = str(tags)
        rows.append(row)

# Write updated CSV
with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Done! Filled missing tags with 'O'")
