# 🚀 Django Boilerplate - Notes API with DDD Architecture

## 📋 **About the Project**

A modern Django application following **Domain-Driven Design (DDD)** for note management with a complete RESTful API.

## 🎯 **Features**

- ✅ **Complete CRUD** for notes
- ✅ **RESTful API** with standardized endpoints
- ✅ **Well-structured DDD Architecture**
- ✅ **Automated tests** ready
- ✅ **Consistent formatting** with Black + EditorConfig
- ✅ **Scalable structure** for multiple apps

## 🏗️ **Application Structure**

```
django_boilerplate/
├── app/                 # Django project configurations
│   ├── settings.py      # Application settings
│   ├── urls.py         # Main URLs
│   ├── asgi.py         # ASGI config
│   └── wsgi.py         # WSGI config
├── notes/              # Main app (DDD)
│   ├── application/     # Use cases and business rules
│   │   └── use_cases.py
│   ├── domain/         # Entities and interfaces
│   │   ├── entities.py
│   │   ├── repositories.py
│   │   └── __init__.py
│   ├── infrastructure/  # Concrete implementations
│   │   ├── models/
│   │   │   └── note_model.py
│   │   ├── mappers.py
│   │   ├── repositories.py
│   │   └── __init__.py
│   ├── interfaces/     # APIs and controllers
│   │   └── api/
│   │       └── views/
│   │           ├── note_list.py
│   │           ├── note_detail.py
│   │           ├── mixins.py
│   │           └── __init__.py
│   ├── migrations/     # Database migrations
│   ├── __init__.py
│   ├── apps.py
│   └── urls.py
├── users/              # Users app (in development)
│   └── urls.py
├── manage.py
├── requirements.txt
├── .editorconfig       # Formatting configurations
└── README.md
```

## 🌐 **API Endpoints**

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/notes/` | List all notes |
| `POST` | `/api/notes/` | Create new note |
| `GET` | `/api/notes/{id}/` | Get specific note |
| `PUT` | `/api/notes/{id}/` | Update note |
| `DELETE` | `/api/notes/{id}/` | Delete note |

## 🛠️ **Technologies Used**

- **Python 3.13** + Django 5.1
- **Django REST Framework** for APIs
- **SQLite** (development)
- **Black** + **EditorConfig** for formatting
- **DDD Architecture** with clear layer separation

## 🚀 **How to Run**

### 1. **Set up the environment**
```bash
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### 2. **Run migrations**
```bash
python manage.py migrate
```

### 3. **Start the server**
```bash
python manage.py runserver
```

### 4. **Access the API**
🌐 **http://localhost:8000/api/notes/**

## 🧪 **Testing**

```bash
# Run all tests
python manage.py test

# Run specific tests for notes app
python manage.py test notes
```

## 🔧 **Useful Commands**

```bash
# Format code with Black
black .

# Create migrations
python manage.py makemigrations

# Interactive shell
python manage.py shell

# Create superuser
python manage.py createsuperuser

# Check application health
python manage.py check
```

## 📁 **DDD Structure Explained**

### **Domain Layer**
- `entities.py`: Domain entities (NoteEntity)
- `repositories.py`: Repository interfaces

### **Application Layer**  
- `use_cases.py`: Use cases and business rules

### **Infrastructure Layer**
- `models/`: Django persistence models
- `repositories.py`: Concrete repository implementations
- `mappers.py`: Converters between entities and models

### **Interfaces Layer**
- `api/views/`: API REST views
- `mixins.py`: View utilities

## 🎨 **Code Standards**

- **Formatting**: Black + EditorConfig (4 spaces, LF line endings)
- **Imports**: Absolute and organized
- **Naming**: Snake_case for Python
- **Typing**: Type hints in all functions

## 🔄 **Adding New Apps**

1. Create the DDD folder structure
2. Implement domain/entities.py and domain/repositories.py
3. Implement infrastructure/repositories.py and infrastructure/models/
4. Implement application/use_cases.py  
5. Implement interfaces/api/views/
6. Add URLs in app/urls.py

---

## 👥 **Authors**

- **Developer** - [@audax-cairo](https://github.com/audax-cairo)

---

⭐ **Give this repository a star if this project helped you!**

---

**✨ Developed with ❤️ using Django and DDD Architecture**
