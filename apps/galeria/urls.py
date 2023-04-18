from django.urls import path
from apps.galeria.views import index, article, search, new_image, edit_image, delete_image

urlpatterns = [
    path('', index, name='index'),
    path('article/<int:article_id>/', article, name='article'),
    path('search', search, name='search'),
    path('new-image', new_image, name='new-image'),
    path('edit-image/<int:article_id>', edit_image, name='edit-image'),
    path('delete-image', delete_image, name='delete-image'),
]   