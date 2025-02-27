# Document Word Extractor

Before I begin implementing this solution, I would like to justify why I have decided to use certain technologies:

## Technology Choices

### Python
- The specification states that the solution should be programmed in this language.

### Django
- Harsha suggested that the team uses this framework.
- I want to demonstrate my proficiency with it.

### spaCy
This NLP library will be used over NLTK for a few reasons:

1. **Optimized for speed**  
   - Built in Cython, so it runs faster than NLTK.
2. **Includes sentence segmentation**  
   - Can easily split paragraphs into sentences, allowing me to further split those sentences into individual words.
3. **Built-in tokenization**  
   - I can use this directly instead of manually splitting text.
4. **Predefined stopword list**  
   - I won't need to manually parse for common words.
5. **Future-proofing**  
   - While NLTK is suitable for this scenario, I am assuming we want to schedule this implementation in the future, in which case using spaCy is much faster and cleaner.
