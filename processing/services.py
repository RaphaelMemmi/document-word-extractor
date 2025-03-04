import os
import spacy
from collections import Counter, defaultdict

# load the spacy model (pre-trained model that can do everything we want)
nlp = spacy.load("en_core_web_sm")

"""
This function loads the files within data/ and returns a dictionary 
of important words and example sentences
"""

def process_text_files(directory="data/"):

    #dict to count word occurences
    word_counter = Counter()
    # dict to map sentences to words
    # we can append sentences without checking if they are already in the list
    #defaultdict means that if a key is not found in the dictionary, it will create a new one automatically
    sentence_map = defaultdict(list)
    #  stores document where word is found 
    doc_map = defaultdict(set)

    # get all files and ensure they are sorted
    sorted_files = sorted(os.listdir(directory))

    # loop through all files in the directory
    for filename in sorted_files:
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

    # Convert sets to lists so they can be used in JSON responses and sort them
    doc_map = {word: sorted(docs, key=lambda x: int(''.join(filter(str.isdigit, x)))) for word, docs in doc_map.items()} 

    # get the minimum and maximum frequency of words
    min_freq = min(word_counter.values()) if word_counter else 0
    max_freq = max(word_counter.values()) if word_counter else 0

    # return the word counts, sentences, documents, and min/max frequency
    result = {
        "word_counts": word_counter,
        "sentences": sentence_map,
        "documents": doc_map,
        "min_freq": min_freq, 
        "max_freq": max_freq   
    }

    return result

def filter_words_by_frequency(preprocessed_data, min_frequency, max_sentences):
    """Filters the words based on selected minimum frequency."""
    word_counts = {word: count for word, count in preprocessed_data["word_counts"].items() if count >= min_frequency}
    word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

    # Filter sentences and documents based on the selected words
    filtered_sentences = {word: preprocessed_data["sentences"][word][:max_sentences] for word in word_counts}
    filtered_documents = {word: preprocessed_data["documents"][word] for word in word_counts}

    return {
        "word_counts": word_counts,
        "sentences": filtered_sentences,
        "documents": filtered_documents,
        "min_freq": preprocessed_data["min_freq"],
        "max_freq": preprocessed_data["max_freq"]
    }