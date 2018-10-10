from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': "Olá BSI6, este texto veio da view!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'bunda': 'Gustavo Miranda'}
    # a variavel bunda pega o valor que esta depois dos
    # dois pontos logo la no html eu coloco {{ bunda }}
    # que vai mostrar o resultado que tem nela

    return render(request, 'rango/about.html', context=context_dict)

def teste(request):
    variavel = 1+1
    context_dict = {'oi': variavel}

    return render(request, 'rango/teste.html', context=context_dict)

