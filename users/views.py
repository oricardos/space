from django.shortcuts import render, redirect
from users.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User

def login(request):
    form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST) # pega todas as informações e coloca em um novo form

        #primeiro verifica se as informações são validas
        if form.is_valid():
            if form['password'].value() != form['confirm_password'].value(): #verificando se as senhas são iguais
                return redirect('register')

            #pega o valor de cada campo
            name = form['name'].value()
            email = form['email'].value()
            password = form['password'].value()

            # se o usuario já existir, redireciona para pagina de registro
            if User.objects.filter(username=name).exists(): #verificando se o user já existe
                return redirect('register')

            # senão ele cria o usuario
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )

            user.save()

            return redirect('login')

    return render(request, 'auth/register.html', {'form': form})