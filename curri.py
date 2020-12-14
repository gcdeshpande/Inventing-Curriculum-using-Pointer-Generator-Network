import spacy
from collections import Counter

unwanted={"fresher", "candidate", "inr", "graduation", "qualification", "experience", "annual", "lac", "hiring", "understanding", "convert", "candidates", "qualifications", "salary", "skill", "year"}

nlp=spacy.load("en_core_web_sm")

filein=open("dataset.txt", "r")
my_text=filein.read()

my_doc = nlp(my_text)

print('\nBefore PreProcessing n_Tokens: ', len(my_doc))

my_doc=[token for token in my_doc if not token.is_stop and not token.is_punct and not token.is_digit and not token.is_space and not token.like_num and not token.like_url and not token.like_email]

my_doc=[token.lemma_ for token in my_doc]
my_doc=[token.lower() for token in my_doc]

my_doc = [ele for ele in my_doc if ele not in unwanted] 
print("\nToken List after Preprocessing")
print(my_doc)
print("\n")

print('After PreProcessing n_Tokens: ', len(my_doc))
print("\n")

print("Word frequency of Grams");
gram=Counter(my_doc)
print(gram)
gram=sorted(gram, key=lambda i: gram[i], reverse=True)[:10]
print("\nTop 10 grams");
print(gram)
print("\n")

print("Word frequency of Bigrams");
bigram=Counter(zip(my_doc[::],my_doc[1::]))
print(bigram)
bigram=sorted(bigram, key=lambda i: bigram[i], reverse=True)[:10]
print("\nTop 10 Bigrams");
print(bigram)
print("\n")

print("Word frequency of Trigrams");
trigram=Counter(zip(my_doc[::],my_doc[1::],my_doc[2::]))
print(trigram)
print("\nTop 10 Trigrams");
trigram=sorted(trigram, key=lambda i: trigram[i], reverse=True)[:10]
print(trigram)

res = sum(ele in my_doc for ele in gram)
#print(res)

print("\nList of tokens from syllabus after preprocessing")
syllabus=["web", "html", "css", "bootstrap", "jquery", "angular", "html css"]
print(syllabus)
res = sum(ele in syllabus for ele in gram)
print("\nNumber of grams found in syllabus")
print(res)

bgstring=[str(bigram[i][0])+" "+str(bigram[i][1]) for i in range(10) for j in range(1)]
#print(bgstring)
res = sum(ele in syllabus for ele in bgstring)
print("\nNumber of Bigrams found in syllabus")
print(res)

tgstring=[str(trigram[i][0])+" "+str(trigram[i][1])+" "+str(trigram[i][2]) for i in range(10) for j in range(2)]
#print(tgstring)
