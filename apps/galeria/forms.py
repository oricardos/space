from django import forms

from apps.galeria.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['is_posted',]
        labels = {
            'title': 'Título',
            'content': 'Conteúdo',
            'image_file': 'Arquivo de Imagem',
            'image_url': 'URL da Imagem',
            'category': 'Categoria',
            'created_at': 'Criado em',
            'user': 'Usuário',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image_file': forms.FileInput(attrs={'class': 'form-control'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'created_at': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                }
            ),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }