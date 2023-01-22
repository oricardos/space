from django.urls import path
from galeria.views import index, article, search

urlpatterns = [
    path('', index, name='index'),
    path('article/<int:article_id>/', article, name='article'),
    path('search', search, name='search'),
]   