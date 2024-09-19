from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Configuração do modelo de usuário e uploads
# Modelo simples de Item (se necessário)

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

# Gerenciador de usuários customizado
class UserManager(BaseUserManager):
    def create_user(self, email, nome, password=None):
        if not email:
            raise ValueError('O usuário deve ter um endereço de email')
        user = self.model(email=self.normalize_email(email), nome=nome)
        user.set_password(password)  # Criptografia da senha
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password):
        user = self.create_user(email, nome, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

# Modelo de Usuário Customizado
class User(AbstractBaseUser):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    setor = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=128)  # Gerenciado pelo Django para criptografia
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

# Modelo de Upload de Imagem Médica
class MedicalImageUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploads')
    file = models.ImageField(upload_to='uploads/images/')  # Apenas imagens médicas
    upload_date = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=10, choices=[('txt', 'Texto'), ('other', 'Outro')])
    report = models.TextField(blank=True, null=True)  # Campo para o laudo médico gerado

    def __str__(self):
        return f"Imagem de {self.user.nome} em {self.upload_date}"

    def generate_report(self):
        # Exemplo simplificado de como um laudo pode ser gerado.
        if self.file_type == 'txt':
            self.report = "Laudo gerado para o arquivo de texto."
        else:
            self.report = "Laudo gerado para a imagem."
        self.save()
