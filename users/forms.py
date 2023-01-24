from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(
        label="Nome completo",
        required=True,
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome completo'
            }
        )
    )
    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        )
    )

class RegisterForm(forms.Form):
    name = forms.CharField(
        label="Nome Completo",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome Completo',
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Seu melhor email',
            }
        )
    )
    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Crie uma senha',
            }
        )
    )
    confirm_password = forms.CharField(
        label="Confirmar Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme sua senha',
            }
        )
    )

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')

    #     if name:
    #         name = name.strip()
    #         if ' ' in name:
    #             raise forms.ValidationError('Não é possível inserir espaço no campo usuário')
    #         else:
    #             return name

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError('As senhas não são iguais.')
            else:
                return confirm_password