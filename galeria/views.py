from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não conectado')
        return redirect('login')
    articles = Article.objects.order_by('-created_at').filter(is_posted=True)
    return render(request, 'galeria/index.html', {'articles': articles} )

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'galeria/article.html', {'article': article})

def search(request):
    articles = Article.objects.order_by('-created_at').filter(is_posted=True)
    if 'search' in request.GET:
        search_term = request.GET['search']
        if search_term:
            articles = articles.filter(title__icontains=search_term)
            print(search_term, 'search term')
    return render(request, 'search.html', {'articles': articles})
