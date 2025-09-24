from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse, JsonResponse
# Create your views here.

class blog(View):
    def get(request):
        return HttpResponse("<h1>Bem vindo ao blog do itallume!</h1>")
    
    def eco(request, texto):
        return HttpResponse(f"<h1>Você digitou: {texto}<h1>")
    
    def info(request):
        return JsonResponse( {
     "disciplina": "RAD",
     "framework": "Django",
     "semestre": "2025.2"
  })