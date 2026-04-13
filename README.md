# 📌 Treebank Creation for a Small Corpus

## 📖 Overview

This project focuses on building a **domain-specific treebank** using cricket match report headlines and summaries. It combines **automatic NLP annotation** with **manual corrections** and **custom domain tagging** to better capture cricket-specific linguistic patterns.

---

## 🎯 Objectives

* Create a small annotated corpus (treebank)
* Compare **automatic vs manual annotation**
* Introduce **domain-specific entity tags**
* Analyze linguistic patterns in **headlines vs summaries**

---

## 📂 Dataset

* Source: ESPNcricinfo match reports from IPL 2025 season
* Data used:

  * Match headlines
  * Summary lines below headline
* Total sentences: **148**

---

## ⚙️ Methodology

### 1. Preprocessing

* Removed leading/trailing whitespace
* Tokenization using **spaCy**

### 2. Automatic Annotation

* Generated:

  * POS (Part-of-Speech) tags
  * Dependency tags

### 3. Manual Annotation

* Annotated **30 sentences (~20% of dataset)**
* Corrected:

  * POS tagging errors
  * Dependency inconsistencies

### 4. Custom Tagging

Introduced cricket-specific tags:

```
PLAYER, TEAM, VENUE, TOURNAMENT,
RUN_EVENT, WICKET, PARTNERSHIP, BOUNDARY,
OVER, SCORE, RESULT, MARGIN,
PHASE, AWARD, ROLE
```

* Non-entity tokens labeled as: `O`

### 5. Data Format

* Converted dataset from `.csv` → `.json`
* Stored:

  * Tokens
  * POS tags
  * Dependency tags
  * Custom tags

---

## 📊 Analysis

### 🔹 Dataset Statistics

* Total sentences: 148
* Average sentence length: **15.84 tokens**

| Type     | Avg Length |
| -------- | ---------- |
| Headline | 11.43      |
| Summary  | 20.26      |

---

### 🔹 POS Tag Insights

* Most frequent: **PROPN (Proper Nouns)**
* Reflects heavy use of:

  * Player names
  * Team names

---

### 🔹 Dependency Insights

* High frequency of:

  * `prep`, `pobj` → structured score expressions
* `ROOT ≈ number of sentences` → mostly single-clause sentences

---

### 🔹 Manual vs Automatic Comparison

* Automatic tagging:

  * Misclassifies proper nouns as common nouns
* Manual tagging:

  * More accurate for domain-specific entities

---

### 🔹 Headlines vs Summaries

| Feature | Headlines    | Summaries           |
| ------- | ------------ | ------------------- |
| Style   | Short, dense | Longer, descriptive |
| Focus   | Entities     | Context + details   |
| Tokens  | More PROPN   | More ADP & NUM      |

---

### 🔹 Custom Tag Insights

* Most important:

  * `PLAYER`, `TEAM`, `RESULT`, `SCORE`
* Less frequent:

  * `VENUE`, `PARTNERSHIP`, `ROLE`

---

## 💡 Key Contributions

### ✅ Domain-Specific Tagging

* Captures cricket-specific semantics ignored by standard NLP tags

### ✅ Hybrid Annotation Approach

* Combines:

  * Automated efficiency
  * Manual accuracy

---

## 🧠 Conclusion

* Automatic NLP methods provide a good baseline
* However, they struggle with:

  * Domain-specific entities
  * Contextual nuances
* Manual corrections + custom tags significantly improve quality

---

## 🛠️ Tech Stack

* Python
* spaCy
* JSON / CSV

---

## 🚀 Future Improvements

* Increase manually annotated dataset size
* Train a custom NER model on cricket data
* Extend to full match reports (not just summaries)

---

## 🙌 Acknowledgment

* Dataset sourced from ESPNcricinfo
* Built as part of NLP coursework

---

## 📬 Contact

**Name:** Suvan Gururaj
**Course:** CS458 – NLP Project