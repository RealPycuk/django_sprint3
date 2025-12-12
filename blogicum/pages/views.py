from django.shortcuts import render


# Create your views here.
def about(request):
    """Страница 'О проекте'"""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Страница 'Правила'"""
    template = 'pages/rules.html'
    return render(request, template)
