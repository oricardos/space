from django.urls import path
from apps.galeria.views import index, article, search, new_image, edit_image, delete_image, filter_category

urlpatterns = [
    path('', index, name='index'),
    path('article/<int:article_id>/', article, name='article'),
    path('search', search, name='search'),
    path('new-image', new_image, name='new-image'),
    path('edit-image/<int:article_id>', edit_image, name='edit-image'),
    path('delete-image/<int:article_id>', delete_image, name='delete-image'),
    path('filter-category/<str:category>', filter_category, name="filter-category")
]   