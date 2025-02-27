# Document Word Extractor

## Introduction

Before implementing this solution, I would like to justify my choice of technologies.

## Technology Choices

### Python
- The specification states that the solution should be programmed in Python.

### Django
- **Reason for selection:** Harsha suggested that the team use this framework.
- **Personal motivation:** I want to demonstrate my proficiency with Django.

### spaCy (Natural Language Processing Library)
I have chosen **spaCy** over **NLTK** for the following reasons:

1. **Optimized for speed**  
   - Built in **Cython**, making it faster than NLTK.
2. **Includes sentence segmentation**  
   - Easily splits paragraphs into sentences, which can then be broken down into individual words.
3. **Built-in tokenization**  
   - Directly available, eliminating the need for manual text splitting.
4. **Predefined stopword list**  
   - Automatically filters out common words without requiring custom parsing.
5. **Future-proofing**  
   - While **NLTK** is suitable for this scenario, **spaCy** is better for scheduled implementations due to its speed and cleaner API.
