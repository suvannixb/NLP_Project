import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

df = pd.read_csv("NLP_Data.csv")

def process_sentence(sentence):
	doc = nlp(sentence)

	tokens = []
	pos_tags = []
	dep_tags = []

	for token in doc:
		tokens.append(token.text)
		pos_tags.append(token.pos_)
		dep_tags.append(token.dep_)

	return tokens, pos_tags, dep_tags

df["tokens"], df["pos_tags"], df["dep_tags"] = zip(*df["sentence"].apply(process_sentence))

df.to_csv("ipl_tagged.csv", index=False)

print("Tagging complete!")
