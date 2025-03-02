from django.http import JsonResponse
from processing.services import process_text_files
from django.shortcuts import render

def process_documents(request):
    data = process_text_files()
    return JsonResponse(data)

def frontend_view(request):
    return render(request, "index.html") 
