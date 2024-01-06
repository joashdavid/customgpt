from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .promptProccessor import processPromptInput

def homePage(request):
    return render(request,"index.html")

def processPromptRequest(request):
    prompt = request.GET.get("prompt")
    response = processPromptInput(prompt)
    return JsonResponse(response)