from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('cadastro/', views.register, name='cadastro'),  # Página de cadastro
    path('upload_image/', views.upload_image, name='upload_image'),  # Página de upload
    path('view_report/<int:upload_id>/', views.view_report, name='view_report'),  # URL para visualizar o laudo
    path('login/', views.login, name='login'),  # Adicionando a rota para login
]
