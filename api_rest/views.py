from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, MedicalImageUploadForm
from django.contrib.auth.decorators import login_required

# View para a página inicial (home) - faz login e redireciona
def home(request):
    if request.method == 'POST':
        email = request.POST.get('username')  # Certifique-se de que o nome do campo é "username"
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('upload_image')  # Redireciona para a tela de upload após login
        else:
            return render(request, 'home.html', {'login_error': 'Usuário ou senha incorretos'})

    return render(request, 'home.html')

# View de Cadastro - cadastro.html
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automático após cadastro
            return redirect('home')  # Redireciona para a tela de upload após o cadastro
    else:
        form = CustomUserCreationForm()  # Mostra o formulário vazio para cadastro
    return render(request, 'cadastro.html', {'form': form})

# View de upload de imagem médica - após login/cadastro
@login_required
def upload_image(request):
    if request.method == 'POST':
        form = MedicalImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user  # Associa o upload ao usuário logado
            upload.save()
            upload.generate_report()  # Gera o laudo
            return redirect('view_report', upload_id=upload.id)  # Redireciona após o upload
    else:
        form = MedicalImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

# View para visualizar o laudo
@login_required
def view_report(request, upload_id):
    upload = MedicalImageUploadForm.objects.get(id=upload_id, user=request.user)
    return render(request, 'view_report.html', {'upload': upload})
