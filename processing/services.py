import os
import spacy
from collections import Counter, defaultdict

# load the spacy model (pre-trained model that can do everything we want)
nlp = spacy.load("en_core_web_sm")

"""
This function loads the files within data/ and returns a dictionary 
of important words and example sentences
"""

def process_text_files(directory="data/", min_word_count=4, max_sentences=10):

    #dict to count word occurences
    word_counter = Counter()
    # dict to map sentences to words
    # we can append sentences without checking if they are already in the list
    #defaultdict means that if a key is not found in the dictionary, it will create a new one automatically
    sentence_map = defaultdict(list)
    #  stores document where word is found 
    doc_map = defaultdict(set)


    # loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  
            file_path = os.path.join(directory, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
                # break loadedd text into sentences
                spacy_doc = nlp(text)  

                # for each word in the sentence, convert it to lowercase, and add it to a new word list 
                # if it is an alphabetical character and not a stop word
                for sent in spacy_doc.sents:
                    words = [token.text.lower() for token in sent if token.is_alpha and not token.is_stop]
                    # update the dictionary with the new words currently in words (broken apart sentence by sentence)
                    word_counter.update(words)
                    
                    # for each word in the sentence, add the sentence to the list of sentences
                    # and the document that contains the word
                    for word in set(words):
                        sentence_map[word].append(sent.text)
                        doc_map[word].add(filename)

    # only keep the first max_sentences sentences for each word
    sentence_map = {word: sentences[:max_sentences] for word, sentences in sentence_map.items()}

    # Convert sets to lists so they can be used in JSON responses and sort them
    doc_map = {word: sorted(docs, key=lambda x: int(''.join(filter(str.isdigit, x)))) for word, docs in doc_map.items()}  # ✅ Sort docs numerically


    # sort words by frequency and filter out words that don't meet the minimum word count
    word_counter = {word: count for word, count in word_counter.items() if count >= min_word_count}
    word_counter = dict(sorted(word_counter.items(), key=lambda item: item[1], reverse=True))

    return {
        "word_counts": word_counter,
        "sentences": sentence_map,
        "documents": doc_map
    }