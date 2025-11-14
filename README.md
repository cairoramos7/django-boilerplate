1. **Criar a pasta de documentação**

```bash
mkdir docs
```

2. **Adicionar cada `.md` dentro de `docs/`**
   Copiar o conteúdo que já te entreguei (um arquivo para cada título).

3. **Configurar o projeto Django**

```bash
python -m venv .venv && source .venv/bin/activate   # ou .venv\Scripts\activate no Windows
pip install "Django>=5.0,<6.0" djangorestframework pytest pytest-django
django-admin startproject myproject .
python manage.py startapp myapp
```

4. **Aplicar ajustes no `settings.py` e `urls.py` (root)**

* Adicionar `rest_framework` e `myapp` em `INSTALLED_APPS`.
* Configurar `REST_FRAMEWORK` conforme no `settings_configuration.md`.
* Editar `myproject/urls.py` para incluir `api/`.

5. **Criar a estrutura de pastas do app**

```bash
mkdir -p myapp/repositories myapp/services myapp/use_cases myapp/validators myapp/utils myapp/tests
```

6. **Preencher os arquivos do app**
   Copiar o conteúdo de cada `.md` correspondente (`models_definition.md`, `user_repository.md`, `user_validators.md`, etc.).

7. **Rodar migrações**

```bash
python manage.py makemigrations
python manage.py migrate
```

8. **Rodar os testes**

```bash
pytest -q
```

9. **Subir servidor**

```bash
python manage.py runserver
```

10. **Testar a API**

* `POST /api/users/` com JSON `{ "email": "x@y.com", "username": "xy", "password": "password123" }`
* `GET /api/users/` para listar.
