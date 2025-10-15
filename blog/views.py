from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse, JsonResponse
from datetime import date
# Create your views here.

class blog(View):
    def get(request):
        return HttpResponse("<h1>Bem vindo ao blog do itallume!</h1>")
    
    def home(request, nome, numero):
        is_logged_in = True if numero > 10 else False

        produtos = [
            {'nome': 'perfume',
             'preco': 50},
              {'nome': 'creme',
             'preco': 30},
              {'nome': 'base',
             'preco': 35},
              {'nome': 'batom',
             'preco': 20},
              {'nome': 'pó',
             'preco': 25},
              {'nome': 'lapís de olho',
             'preco': 12},
        ]


        context = {
            'msg': f"Olá {nome}, seja bem vindo ao nosso sistema!",
            'numero': numero * 2,
            'now': date.today(),
            'is_logged_in': is_logged_in,
            'idade': 19,
            'role': 'USER',
            'produtos': produtos,
                   }

        return render(request, 'blog/home.html', context)
    
    def contato(request, numerotel):

        return render(request, 'blog/contato.html', {'numero': numerotel})
    
    def homeTop(request):
        return render(request, 'global/home.html')
    
    def about(request):
        return render(request, 'global/about.html')
    
    def info(request):
        return JsonResponse( {
     "disciplina": "RAD",
     "framework": "Django",
     "semestre": "2025.2"
    })