from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import MedicalImageUpload  

class CustomUserCreationForm(UserCreationForm):
    nome = forms.CharField(max_length=255, required=True, label="Nome")
    email = forms.EmailField(max_length=255, required=True, label="Email")
    setor = forms.CharField(max_length=100, required=False, label="Setor")
    
    # class Meta:
    #     model = User  # ou o modelo que você estiver usando
    #     fields = ['nome', 'email', 'setor', 'password1', 'password2']

class MedicalImageUploadForm(forms.ModelForm):
    class Meta:
        model = MedicalImageUpload
        fields = ['file', 'file_type']

    