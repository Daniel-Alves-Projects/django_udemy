from django.shortcuts import render

def index(request):
    print(dir(request))
    print(f'Headers: {request.headers}')
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

