from django.shortcuts import render, redirect
from users.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            name = form['name'].value()
            password = form['password'].value()

        user = auth.authenticate(
            request,
            username = name,
            password = password,
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Seja bem vindo(a) ao Space')
            return redirect('index')
        else:
            messages.error(request, 'Houve um erro ao tentar realizar o login, tente novamente mais tarde!')
            return redirect('login')


    return render(request, 'auth/login.html', {'form': form})

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST) # pega todas as informações e coloca em um novo form

        #primeiro verifica se as informações são validas
        if form.is_valid():
            #pega o valor de cada campo
            name = form['name'].value()
            email = form['email'].value()
            password = form['password'].value()

            # se o usuario já existir, redireciona para pagina de registro
            if User.objects.filter(username=name).exists(): #verificando se o user já existe
                messages.error(request, 'Usuário já existente!')
                return redirect('register')

            # senão ele cria o usuario
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )

            user.save()
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('login')

    return render(request, 'auth/register.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')