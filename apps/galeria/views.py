from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Article
from django.contrib import messages
from apps.galeria.forms import ArticleForm

def index(request):
    """
    View que renderiza a index da aplicação
    Verifica se o usuário está autenticado. Caso contrário, exibe uma mensagem de erro e redireciona para a página de login.
    Obtém todos os artigos publicados ordenados por data de criação decrescente e os passa para o template 'galeria/index.html'.

    Args:
        - request: um objeto HttpRequest contendo informações sobre a requisição HTTP atual.

    Returns:
        - Um objeto HttpResponse contendo o conteúdo HTML da página inicial da aplicação.
    """
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

def new_image(request):
    """
    Renderiza o formulário de criação de uma nova imagem e processa o envio do formulário submetido pelo usuário.

    Verifica se o usuário está autenticado, caso contrário, redireciona para a página de login.

    Caso o método da requisição seja POST, cria um objeto de formulário de artigo, popula com os dados submetidos e salva
    o novo artigo no banco de dados, se o formulário for válido. Caso contrário, redireciona para a página inicial.

    Args:
        Um objeto HttpRequest que contém informações sobre a solicitação do usuário.
    
    Return: 
        Um objeto HttpResponse que renderiza o formulário de criação de nova imagem ou redireciona para a página inicial.
    """
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não conectado')
        return redirect('login')
    
    form = ArticleForm
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, 'Novo artigo criado com sucesso')
            return redirect('index')
        
    return render(request, 'form/new.html', {'form': form})

def edit_image(request, article_id):
    """
    Renderiza um formulário pré-preenchido com os dados de um artigo especificado pelo ID,
    e permite sua edição. Caso o formulário seja submetido com sucesso, atualiza o artigo
    no banco de dados e redireciona para a página inicial.

    Args:
        request: objeto HttpRequest contendo os dados da requisição HTTP.
        article_id (number): inteiro representando o ID do artigo a ser editado.

    Returns:
        Renderização do template 'form/edit.html', passando o formulário preenchido e o ID do artigo.
    """
    article = Article.objects.get(id=article_id)
    form = ArticleForm(instance=article)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid:
            form.save()
            messages.success(request, 'Artigo atualizado com sucesso')
            return redirect('index')
    
    return render(request, 'form/edit.html', {'form': form, 'article_id': article_id})

def delete_image(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    messages.success(request, 'Artigo deletado')
    
    return redirect('index')
