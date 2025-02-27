import os
import spacy
from collections import Counter

# load the spacy model (pre-trained model that can do everything we want)
nlp = spacy.load("en_core_web_sm")

"""
This function loads the files within data/ and returns a dictionary 
of important words and example sentences
"""

def process_text_files(directory="data/"):

    #dict to count word occurences
    word_counter = Counter()


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

    print(word_counter)

if __name__ == "__main__":
    process_text_files()
