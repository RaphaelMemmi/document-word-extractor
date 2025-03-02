from django.http import JsonResponse
from processing.services import process_text_files, filter_words_by_frequency
from django.shortcuts import render

# ✅ Precompute full dataset (includes all words)
PREPROCESSED_DATA = process_text_files()

def process_documents(request):
    """API endpoint to return dynamically filtered word analysis."""
    print("API Request Received")

    if "min_freq" not in PREPROCESSED_DATA or "max_freq" not in PREPROCESSED_DATA:
        print("Error: min_freq or max_freq missing from preprocessed data")
        return JsonResponse({"error": "Preprocessing failed. Check process_text_files() output."}, status=500)

    # ✅ Get min_frequency and max_sentences from request
    min_frequency = request.GET.get("min_frequency", PREPROCESSED_DATA["min_freq"])
    max_sentences = request.GET.get("max_sentences", PREPROCESSED_DATA["max_freq"])

    # ✅ Ensure they are integers
    if not str(min_frequency).isdigit() or not str(max_sentences).isdigit():
        return JsonResponse({"error": "Invalid parameters"}, status=400)

    min_frequency = int(min_frequency)
    max_sentences = int(max_sentences)

    print(f"Filtering words with min_frequency >= {min_frequency} and max_sentences = {max_sentences}")
    filtered_data = filter_words_by_frequency(PREPROCESSED_DATA, min_frequency, max_sentences)

    return JsonResponse(filtered_data)

def frontend_view(request):
    return render(request, "index.html") 
