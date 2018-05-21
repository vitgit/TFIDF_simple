# in java:
#    https://gist.github.com/guenodz/d5add59b31114a3a3c66

import math

# doc - list of strings (words)
# term - tested word
def tf(doc, term):
    res = 0.
    for word in doc:
        if term.lower() == word.lower():
            res += 1.
    return res / len(doc)

# docs - list of list of strings represents the dataset
# term String represents a term
def idf(docs, term):
    n = 0
    for doc in docs:
        for word in doc:
            if term.lower() == word.lower():
                n += 1
                break
    return math.log(len(docs) / n)

def tfidf(doc, docs, term):
    return tf(doc, term) * idf(docs, term)

def main():
    doc1 = ["Lorem", "ipsum", "dolor", "ipsum", "sit", "ipsum"]
    doc2 = ["Vituperata", "incorrupte", "at", "ipsum", "pro", "quo"]
    doc3 = ["Has", "persius", "disputationi", "id", "simul"]

    documents = [doc1, doc2, doc3]

    tfidf_res = tfidf(doc1, documents, "ipsum")
    print ("TFIDF for {} is {}".format("ipsum", tfidf_res))

if __name__ == main():
    main()