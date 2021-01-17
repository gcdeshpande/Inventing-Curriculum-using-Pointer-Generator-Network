import spacy
from collections import Counter

unwanted={"fresher", "candidate", "inr", "graduation", "qualification", "experience", "annual", "lac", "hiring", "understanding", "convert", "candidates", "qualifications", "salary", "skill", "year"}

nlp=spacy.load("en_core_web_sm")

#filein=open("dataset.txt", "r")
#my_text=filein.read()

my_text="""
The ideal candidate will be responsible for designing, developing, testing, and debugging responsive web and mobile applications for the company. Using HTML and CSS, this candidate will be able to translate user and business needs into functional frontend design.

Responsibilities

    Designing & developing UI for web & mobile applications
    Build reusable code and libraries for future use
    Ability to convert comprehensive layout and wireframes into working HTML pages.
    Accurately translate user and business needs into functional frontend code

Qualifications

    Familiarity using Scrum/Agile development methodologies
    Fresher or less than 2 years of experience in frontend development
    Good understanding of front-end technologies including HTML, CSS(flex), JavaScript, jQuery & Bootstrap framework

Required Web Developer and Designer Candidates must have good knowledge of wordpress,HTML,PHP Skills:- Wordpress and HTML .Experience :- Fresher to 1 year

Web Developer We are hiring full time web developer and looking for bright candidate to join team Random Soft Solution
Skills: Html, CSS, Bootstrap, PHP, Jquery, WordPress, CI.
Qualification: Graduation.
Expreince: Fresher 2 Year.
Salary: 1.8 to 2.6 lac INR/Annual
Skills:Html, CSS, Bootstrap, PHP, Jquery, WordPress, CI. Qualification:Graduation. Expreince:Fresher 2 Year. Salary: 1.8 to 2.6 lac INR/Annual

"""
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
syllabus=["web", "html", "css", "bootstrap", "jquery", "angular", "html css","wordpress html"]
print(syllabus)
res = sum(ele in syllabus for ele in gram)
print("\nNumber of grams found in syllabus")
print(res)
percent=str((res/len(gram))*100)
print("\n The syllabus is "+percent+ " percent closer to the objective")

bgstring=[str(bigram[i][0])+" "+str(bigram[i][1]) for i in range(10) for j in range(1)]
#print(bgstring)
res = sum(ele in syllabus for ele in bgstring)
print("\nNumber of Bigrams found in syllabus")
print(res)
percent=str((res/len(bigram))*100)
print("\n The syllabus is "+percent+ " percent closer to the objective")

tgstring=[str(trigram[i][0])+" "+str(trigram[i][1])+" "+str(trigram[i][2]) for i in range(10) for j in range(2)]
#print(tgstring)
