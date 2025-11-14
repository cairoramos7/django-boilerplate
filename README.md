# 🚀 Django Boilerplate - DDD Architecture Template

## 📋 **About the Project**

A modern Django boilerplate following **Domain-Driven Design (DDD)** principles. This is a flexible foundation for building scalable applications with clean architecture, ready to be extended with any domain or feature.

## 🎯 **Features**

- ✅ **Clean DDD Architecture** with proper layer separation
- ✅ **RESTful API** ready with standardized patterns
- ✅ **Flexible structure** for any domain implementation
- ✅ **Automated testing** framework setup
- ✅ **Consistent formatting** with Black + EditorConfig
- ✅ **Scalable design** for multiple domains and microservices
- ✅ **Production-ready** configuration

## 🏗️ **Architecture Structure**

```
django_boilerplate/
├── app/                 # Django project configurations
│   ├── settings.py      # Application settings (DEV/PROD ready)
│   ├── urls.py         # Main URL routing
│   ├── asgi.py         # ASGI config
│   └── wsgi.py         # WSGI config
├── {domain_name}/       # Domain app (example: notes/, users/, products/)
│   ├── application/     # Use cases and business rules
│   │   └── use_cases.py
│   ├── domain/         # Entities and interfaces (CORE)
│   │   ├── entities.py
│   │   ├── repositories.py
│   │   └── __init__.py
│   ├── infrastructure/  # Concrete implementations
│   │   ├── models/
│   │   │   └── {entity}_model.py
│   │   ├── mappers.py
│   │   ├── repositories.py
│   │   └── __init__.py
│   ├── interfaces/     # APIs and presentation layer
│   │   └── api/
│   │       └── views/
│   │           ├── {entity}_list.py
│   │           ├── {entity}_detail.py
│   │           ├── mixins.py
│   │           └── __init__.py
│   ├── migrations/     # Database migrations
│   ├── __init__.py
│   ├── apps.py
│   └── urls.py
├── shared/             # Shared utilities (optional)
│   ├── exceptions.py
│   ├── utils.py
│   └── __init__.py
├── manage.py
├── requirements.txt
├── .editorconfig       # Consistent code formatting
├── .gitignore
└── README.md
```

## 🌐 **API Pattern**

| Method | Endpoint Pattern | Description |
|--------|------------------|-------------|
| `GET` | `/api/{domain}/{entity}/` | List all entities |
| `POST` | `/api/{domain}/{entity}/` | Create new entity |
| `GET` | `/api/{domain}/{entity}/{id}/` | Get specific entity |
| `PUT` | `/api/{domain}/{entity}/{id}/` | Update entity |
| `DELETE` | `/api/{domain}/{entity}/{id}/` | Delete entity |

**Examples:**
- `/api/notes/notes/` - Notes domain, Note entity
- `/api/users/users/` - Users domain, User entity  
- `/api/products/products/` - Products domain, Product entity

## 🛠️ **Technology Stack**

- **Python 3.13** + Django 5.1
- **Django REST Framework** for API development
- **SQLite** (development) / **PostgreSQL** (production ready)
- **Black** + **EditorConfig** for code consistency
- **Pytest** for testing framework
- **DDD Architecture** with clear separation of concerns

## 🚀 **Quick Start**

### 1. **Clone and setup**
```bash
git clone <your-repo-url>
cd django_boilerplate

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac

pip install -r requirements.txt
```

### 2. **Configure your domain**
```bash
# Create your domain app structure
python manage.py startapp your_domain

# Follow the DDD structure pattern from existing apps
mkdir -p your_domain/{application,domain,infrastructure,interfaces/api/views}
```

### 3. **Run and develop**
```bash
python manage.py migrate
python manage.py runserver
```

Access: 🌐 **http://localhost:8000/api/**

## 🧪 **Testing**

```bash
# Run all tests
python manage.py test

# Run specific domain tests
python manage.py test your_domain

# Run with coverage
coverage run manage.py test
coverage report
```

## 🔧 **Development Commands**

```bash
# Code formatting
black .

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Django shell
python manage.py shell

# Create admin user
python manage.py createsuperuser

# Check project health
python manage.py check
```

## 📁 **DDD Layers Explained**

### **Domain Layer (CORE BUSINESS)**
- `entities.py`: Pure business objects, no framework dependencies
- `repositories.py`: Interface definitions for data persistence
- **Purpose**: Heart of the business logic, framework-agnostic

### **Application Layer (USE CASES)**  
- `use_cases.py`: Orchestrates domain objects, implements business workflows
- **Purpose**: Connects domain with infrastructure, contains application logic

### **Infrastructure Layer (IMPLEMENTATION)**
- `models/`: Django ORM models for persistence
- `repositories.py`: Concrete implementations of domain interfaces
- `mappers.py`: Converts between domain entities and persistence models
- **Purpose**: Framework-specific implementations, external integrations

### **Interfaces Layer (PRESENTATION)**
- `api/views/`: REST API endpoints
- `mixins.py**: Shared view utilities
- **Purpose**: Entry points for external communication (API, Web, etc.)

## 🎨 **Code Standards**

- **Formatting**: Black (4 spaces, 88 char line length, LF line endings)
- **Imports**: Absolute imports, grouped and sorted
- **Naming**: Snake_case for Python, CamelCase for classes
- **Typing**: Full type hints throughout the codebase
- **Structure**: Consistent DDD patterns across all domains

## 🔄 **Adding New Domains**

### 1. **Create Domain Structure**
```bash
python manage.py startapp your_domain
cd your_domain
mkdir -p application domain infrastructure/models interfaces/api/views
```

### 2. **Implement Domain Layer**
```python
# domain/entities.py
class YourEntity:
    id: int
    name: str
    # Business attributes and methods

# domain/repositories.py
class YourRepositoryInterface:
    def get(self, id: int) -> YourEntity: ...
    def save(self, entity: YourEntity) -> YourEntity: ...
```

### 3. **Implement Infrastructure**
```python
# infrastructure/models/your_entity_model.py
class YourEntityModel(models.Model):
    # Django ORM model

# infrastructure/repositories.py  
class YourRepository(YourRepositoryInterface):
    # Concrete implementation
```

### 4. **Implement Application Layer**
```python
# application/use_cases.py
class YourUseCases:
    # Business workflows and operations
```

### 5. **Implement Interfaces**
```python
# interfaces/api/views/your_entity_list.py
class YourEntityListView(APIView):
    # API endpoints
```

### 6. **Register URLs**
```python
# your_domain/urls.py
urlpatterns = [
    path('your_entity/', YourEntityListView.as_view()),
]

# app/urls.py
urlpatterns += [
    path('api/your_domain/', include('your_domain.urls')),
]
```

## 🚀 **Deployment Ready**

- **Environment configurations** (DEV/STAGING/PROD)
- **Database settings** for PostgreSQL
- **Static files** configuration
- **WSGI/ASGI** production setup
- **Docker support** ready to be added

## 📈 **Why This Architecture?**

- **Maintainable**: Clear separation of concerns
- **Testable**: Each layer can be tested independently  
- **Scalable**: Easy to add new domains and features
- **Flexible**: Swap implementations without affecting business logic
- **Modern**: Follows industry best practices for enterprise applications

---

## 👥 **Contributors**

- **Developer** - [@audax-cairo](https://github.com/audax-cairo)

---

⭐ **Give this repository a star if you find it useful!**

---

**✨ Built with ❤️ using Django and Clean Architecture Principles**

---

**📄 License**: MIT - Feel free to use this as a foundation for your projects!
