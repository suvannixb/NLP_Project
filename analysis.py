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

headline_data = []
summary_data = []

for entry in data:
    if entry["type"] == "Headline":
        headline_data.append(entry)
    else:
        summary_data.append(entry)

headline_manual = []
summary_manual = []

for i, entry in enumerate(data):
    if i < 30:  # only manual
        if entry["type"] == "Headline":
            headline_manual.append(entry)
        else:
            summary_manual.append(entry)

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

def avg_length(dataset):
    return sum(len(x["tokens"]) for x in dataset) / len(dataset)

print("\n=== HEADLINE vs SUMMARY LENGTH ===")
print(f"Headline Avg Length: {avg_length(headline_data):.2f}")
print(f"Summary Avg Length: {avg_length(summary_data):.2f}")

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


def pos_percent(dataset):
    counter = Counter()
    total = 0
    
    for entry in dataset:
        counter.update(entry["pos_tags"])
        total += len(entry["pos_tags"])
    
    return {k: (v/total)*100 for k, v in counter.items()}

headline_pos = pos_percent(headline_data)
summary_pos = pos_percent(summary_data)

print("\n=== POS TAG % (HEADLINE) ===")
for k, v in sorted(headline_pos.items(), key=lambda x: -x[1])[:5]:
    print(f"{k}: {v:.2f}%")

print("\n=== POS TAG % (SUMMARY) ===")
for k, v in sorted(summary_pos.items(), key=lambda x: -x[1])[:5]:
    print(f"{k}: {v:.2f}%")


def tag_percent(dataset):
    counter = Counter()
    total = 0
    
    for entry in dataset:
        counter.update(entry["tags"])
        total += len(entry["tags"])
    
    return {k: (v/total)*100 for k, v in counter.items()}

headline_tags = tag_percent(headline_manual)
summary_tags = tag_percent(summary_manual)

print("\n=== CUSTOM TAG % (HEADLINE - MANUAL ONLY) ===")
for k, v in sorted(headline_tags.items(), key=lambda x: -x[1]):
    print(f"{k}: {v:.2f}%")

print("\n=== CUSTOM TAG % (SUMMARY - MANUAL ONLY) ===")
for k, v in sorted(summary_tags.items(), key=lambda x: -x[1]):
    print(f"{k}: {v:.2f}%")



