from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')

        return render(request, 'login.html',{
            'error': "Nome de usuario ou senha inválidos."
        })
    
    return render(request, "login.html")

def novo_usuario(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if password != confirm_password:
            return render(request, 'novo_usuario.html', {
                'error': "As senhas não coincidem."
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'novo_usuario.html',{
                'error': "Este nome de usuario já esta cadastrado."
            })

        User.objects.create_user(username=username, password=password)
        return redirect('login')
    
    return render(request, "novo_usuario.html")

def logout(request):
    auth_logout(request)
    return redirect('login')