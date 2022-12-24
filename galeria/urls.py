from django.urls import path
from galeria.views import index, article

urlpatterns = [
    path('', index, name='index'),
    path('article', article, name='article'),
]