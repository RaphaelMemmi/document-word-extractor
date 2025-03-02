# Document Word Extractor
This was a very fun project to work on!

## Technology Choices

Before I begin implementing this solution, I would like to justify why I have decided to use certain technologies:

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
   - While NLTK is suitable for this scenario, I am assuming we want to scale this implementation in the future, in which case using spaCy is much faster.
  
### Docker
 - Harsha informed that the team uses Docker.
 - It provides a neat and easy way to run the code in a consistent environment.
 - I want to demonstrate my proficiency with it.

## Additional Features
### Interactive Sliders for Better Visualisation
To improve data exploration, the application includes interactive sliders that allow users to:
  - Filter words by frequency
     - Users can dynamically adjust the minimum word frequency threshold.
     - This helps in focusing on commonly used words while removing less relevant ones.
  - Control sentence display
     - Users can set a limit on the maximum number of sentences displayed per word.
     - This ensures better readability, especially for words with many occurrences.
By allowing users to interactively refine the data, the sliders make it easier to visually analyse word importance and context without overwhelming the display.

## Project Structure

```
document_word_extractor/
│── api/                  # Django API views
│── processing/           # Text processing logic (using spaCy)
│── static/               # CSS & JavaScript files
│── templates/            # HTML templates for frontend
│── document_word_extractor/ # Django project settings
│── Dockerfile            # Docker build configuration
│── docker-compose.yml    # Docker Compose setup
│── requirements.txt      # Python dependencies
│── README.md             # Project instructions
```

## Prerequisites

Before running this project, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup

### Clone the Repository

```sh
git clone https://github.com/your-username/document-word-extractor.git
cd document-word-extractor
```

### Build the Docker Container

```sh
docker compose build
```

### Start the Application

```sh
docker compose up -d
```

### Apply Migrations

Although I don't use any models, there are still default migrations to be made:

```sh
docker exec -it document-word-extractor python manage.py migrate
```

