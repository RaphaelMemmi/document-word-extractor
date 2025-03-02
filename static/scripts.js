let minFreq, maxFreq;

async function initializeSliders() {
    try {
        const response = await fetch(`/process/`);
        const data = await response.json();

        minFreq = data.min_freq || 1;
        maxFreq = data.max_freq || 100;

        document.getElementById('wordFrequency').min = minFreq;
        document.getElementById('wordFrequency').max = maxFreq;
        document.getElementById('wordFrequency').value = minFreq;
        document.getElementById('sliderValueFreq').textContent = minFreq;

        document.getElementById('sentenceSlider').min = minFreq;
        document.getElementById('sentenceSlider').max = maxFreq;
        document.getElementById('sentenceSlider').value = maxFreq;
        document.getElementById('sliderValueSentences').textContent = maxFreq;

        loadData(minFreq, maxFreq);
    } catch (error) {
        console.error("Error initializing sliders:", error);
    }
}

async function loadData(minFrequency, maxSentences) {
    try {
        const response = await fetch(`/process/?min_frequency=${minFrequency}&max_sentences=${maxSentences}`);
        const data = await response.json();

        document.getElementById('sliderValueFreq').textContent = minFrequency;
        document.getElementById('sliderValueSentences').textContent = maxSentences;

        const tableBody = document.getElementById('data-body');
        tableBody.innerHTML = "";

        for (let word in data.word_counts) {
            let row = document.createElement('tr');

            let wordCell = document.createElement('td');
            wordCell.textContent = `${word} (${data.word_counts[word]})`;
            row.appendChild(wordCell);

            let docsCell = document.createElement('td');
            docsCell.textContent = data.documents[word] ? data.documents[word].join(", ") : "N/A";
            row.appendChild(docsCell);

            let sentencesCell = document.createElement('td');
            sentencesCell.innerHTML = data.sentences[word] 
                ? data.sentences[word].map(s => `<p>${s.replace(new RegExp("\\b" + word + "\\b", "gi"), `<b>${word}</b>`)}</p>`).join("") 
                : "N/A";
            row.appendChild(sentencesCell);

            tableBody.appendChild(row);
        }
    } catch (error) {
        console.error("Error loading data:", error);
    }
}

function updateFilters() {
    const minFrequency = document.getElementById('wordFrequency').value;
    const maxSentences = document.getElementById('sentenceSlider').value;
    loadData(minFrequency, maxSentences);
}

window.onload = initializeSliders;
