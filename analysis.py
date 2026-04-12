import json
from collections import Counter

input_file = "data.json"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Counters
tag_counter = Counter()
pos_counter = Counter()
dep_counter = Counter()

manual_tag_counter = Counter()
auto_tag_counter = Counter()

manual_tokens = 0
auto_tokens = 0

sentence_lengths = []

for i, entry in enumerate(data):
    tokens = entry["tokens"]
    tags = entry["tags"]
    pos = entry.get("pos_tags", [])
    dep = entry.get("dep_tags", [])
    
    sentence_lengths.append(len(tokens))
    
    # overall counts
    tag_counter.update(tags)
    pos_counter.update(pos)
    dep_counter.update(dep)
    
    # manual vs auto split
    if i < 30:  # first 30 = manual
        manual_tag_counter.update(pos)
        manual_tokens += len(tokens)
    else:
        auto_tag_counter.update(pos)
        auto_tokens += len(tokens)

# 🔹 Basic stats
print("\n=== DATASET STATS ===")
print(f"Total Sentences: {len(data)}")
print(f"Average Length: {sum(sentence_lengths)/len(data):.2f}")

print("\n=== CUSTOM TAGS (MANUAL 1–30 ONLY) ===")
manual_custom_counter = Counter()
for i, entry in enumerate(data):
    if i < 30:
        manual_custom_counter.update(entry["tags"])

total_manual = sum(manual_custom_counter.values())
for tag, count in manual_custom_counter.most_common():
    percent = (count / total_manual) * 100
    print(f"{tag}: {count} ({percent:.2f}%)")

# 🔹 POS Tags
print("\n=== POS TAG DISTRIBUTION ===")
for tag, count in pos_counter.most_common(10):
    print(f"{tag}: {count}")

# 🔹 Dependency Tags
print("\n=== DEPENDENCY TAG DISTRIBUTION ===")
for tag, count in dep_counter.most_common(10):
    print(f"{tag}: {count}")

# 🔹 Manual vs Auto Comparison
print("\n=== MANUAL (1–30) vs AUTO (31+) ===")

print("\nManual Tags:")
for tag, count in manual_tag_counter.most_common():
    total_manual = sum(manual_tag_counter.values())
    percent = (count/total_manual) * 100
    print(f"{tag}: {percent:.2f}")
    

print("\nAuto Tags:")
for tag, count in auto_tag_counter.most_common():
    total_auto = sum(auto_tag_counter.values())
    percent = (count/total_auto) * 100
    print(f"{tag}: {percent:.2f}")


with open("analysis.txt", "w", encoding="utf-8") as f:
    
    # Dataset stats
    f.write("=== DATASET STATS ===\n")
    f.write(f"Total Sentences: {len(data)}\n")
    f.write(f"Average Length: {sum(sentence_lengths)/len(data):.2f}\n\n")
    
    f.write("\n=== CUSTOM TAGS (MANUAL 1–30 ONLY) ===\n")

    manual_custom_counter = Counter()

    for i, entry in enumerate(data):
        if i < 30:
            manual_custom_counter.update(entry["tags"])

    total_manual = sum(manual_custom_counter.values())

    for tag, count in manual_custom_counter.most_common():
        percent = (count / total_manual) * 100
        f.write(f"{tag}: {count} ({percent:.2f}%)\n")
    
    f.write("\n=== TAG PERCENTAGES ===\n")
    for tag, count in tag_counter.most_common():
        percent = (count / sum(tag_counter.values())) * 100
        f.write(f"{tag}: {percent:.2f}%\n")
    
    # POS tags
    f.write("\n=== POS TAG DISTRIBUTION ===\n")
    for tag, count in pos_counter.most_common():
        f.write(f"{tag}: {count}\n")
    
    # Dependency tags
    f.write("\n=== DEPENDENCY TAG DISTRIBUTION ===\n")
    for tag, count in dep_counter.most_common():
        f.write(f"{tag}: {count}\n")
    
    # Manual vs Auto
    f.write("\n=== MANUAL (1–30) TAGS ===\n")
    total_manual = sum(manual_tag_counter.values())

    for tag, count in manual_tag_counter.most_common():
        percent = (count / total_manual) * 100
        f.write(f"{tag}: {count} ({percent:.2f}%)\n")

    f.write("\n=== AUTO (31+) TAGS ===\n")
    total_auto = sum(auto_tag_counter.values())

    for tag, count in auto_tag_counter.most_common():
        percent = (count / total_auto) * 100
        f.write(f"{tag}: {count} ({percent:.2f}%)\n")

print("Analysis saved to analysis.txt")
