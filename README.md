# Projeto MAMOIA - Sistema de Upload de Imagens Médicas

Este projeto é um sistema web desenvolvido em Django, destinado ao upload de imagens médicas e à geração de laudos com base nas imagens carregadas.

## Funcionalidades

- **Upload de Imagens Médicas**: Permite o upload de imagens no sistema para processamento posterior.
- **Cadastro de Usuários**: Sistema de cadastro de usuários com campos como nome, email e setor.
- **Visualização de Laudos**: Após o upload, os usuários podem visualizar uma descrição da imagem na tela de laudo.
- **Layout Responsivo**: O projeto utiliza CSS para garantir um layout simples e funcional.

## Estrutura do Projeto

- `manage.py`: Script de gerenciamento do Django.
- `projeto_mamoia/`: Contém as configurações principais do projeto Django.
  - `settings.py`: Configurações do projeto.
  - `urls.py`: Rotas principais do projeto.
  - `wsgi.py` e `asgi.py`: Configurações de deploy.
- `api_rest/`: Aplicativo responsável pelo core do sistema.
  - `views.py`: Define as views para upload de imagens e exibição de laudos.
  - `models.py`: Modelos de dados relacionados ao sistema, como uploads de imagens médicas.
  - `forms.py`: Formulários para cadastro e upload de imagens.
  - `templates/`: Contém os arquivos HTML usados no frontend.
  - `static/`: Contém os arquivos estáticos, como CSS e imagens.
  
## Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   ```
   
2. Acesse o diretório do projeto:
   ```bash
   cd Projeto_mamoia
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

6. Execute o servidor:
   ```bash
   python manage.py runserver
   ```

## Uso

1. Acesse `http://localhost:8000/` no seu navegador.
2. Realize o upload da imagem médica na página correspondente.
3. Acompanhe o laudo gerado na página de visualização.
