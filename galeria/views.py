from django.shortcuts import render, get_object_or_404
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'galeria/index.html', {'articles': articles} )

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'galeria/article.html', {'article': article})
