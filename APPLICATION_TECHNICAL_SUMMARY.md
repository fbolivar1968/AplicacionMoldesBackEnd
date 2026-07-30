# Application Technical Summary — Moldes & Herramentales Backend (GHFB)

> **Document Version:** 1.0  
> **Target Audience:** Backend Developers, DevOps Engineers, System Architects  
> **Last Updated:** July 2026  
> **Repository:** [AplicacionMoldesBackEnd](file:///c:/Users/tdigital/OneDrive%20-%20FORJAS%20BOLIVAR/Documentos/Backend%20GHFB/AplicacionMoldesBackEnd)

---

## 1. Core Purpose & Functionality

The **AplicacionMoldesBackEnd** (GHFB - Forjas Bolívar) is a specialized industrial REST API backend designed to manage plant tooling (*herramentales*), molds (*moldes*), die sets (*diesets*), and related industrial components across manufacturing plants.

### Key Capabilities & Business Features:
- **Tooling & Mold Lifecycle Management (`herramental`):** Registers and tracks individual tool items (`HerramentalEspecifico`), die sets (`DieSet`), physical state (`EstadoHerramental`), scrap status (`Chatarrizacion`), and loan status (`Prestamo`).
- **Automated Tool Code Generation System:** Dynamic alfanumeric code generation format `{CodHerramental}{CodTipo}-{CodFamilia}{Consecutivo:02d}` (e.g. `ME-HX01`) with query endpoints (`/api/herramental/next-consecutive`) for real-time frontend pre-visualization and optimistic concurrency collision protection (409 Conflict).
- **Physical Warehouse & Warehouse Location Hierarchy (`posicion`):** Tracks exact warehouse location across floors (`Piso`), shelving units (`Estanteria`), and row/column/position coordinates (`UbicacionHerramental`).
- **Material Properties & Consolidated Catalogs:** Exposes single consolidated REST responses for steel grade (`Acero`), hardness rating (`Dureza`), and steel supplier (`Proveedor`) to minimize HTTP request overhead on form initialization (`/api/propiedades-herramental/`).
- **Integration with Plant Production Orders (`ipsl`):** Integrates read-only production order tracking directly from forge plant database views (`v_plantaVirtual` / `OrdenProduccionForja`).
- **Machine & Activity Tracking (`produccion`):** Manages industrial machines (`Maquina`), machine status (`EstadoMaquina`), machine types (`TipoMaquina`), and plant activities (`Actividad`).
- **Document & Technical File Management (`documents`):** Handles file uploads (blueprints, technical sheets, photos, manuals) with automated file organization into `pdf/`, `imagenes/`, and `docs/` subdirectories and metadata persistence in the `IMAGEN` table.
- **Staging / QR Scanner Integration (`temp`):** Temporary staging table (`sabana_qr_files` / `DataQRFile`) for bulk batch importing and decoding of QR scanner data.
- **User Management & Role Catalog (`usuarios`):** Enterprise user management (`Usuario`), job positions (`Cargo`), and user types (`TipoUsuario`).

---

## 2. Backend Tech Stack & Architecture

### Core Stack Components:
- **Framework:** Python 3.12+ / Django 5.2.7 & Django REST Framework (DRF) 3.15+.
- **Database Engine:** Microsoft SQL Server.
- **Database Driver & ORM Adapter:** `mssql-django` (and `pyodbc` / `django-mssql-backend`).
- **Authentication:** JWT via `djangorestframework-simplejwt` with `rest_framework_simplejwt.token_blacklist`.
- **CORS Management:** `django-cors-headers`.
- **Environment Management:** `python-dotenv`.
- **Application Servers:** Gunicorn / Waitress (configured in `requirements.txt`).

### Architectural Paradigm:
- **Database-First / Unmanaged ORM Pattern (`managed = False`):** All Django models mirror pre-existing Microsoft SQL Server tables and views (`managed = False`). DDL migrations are handled externally in SQL Server.
- **RESTful ViewSet & APIView Architecture:** Mix of standard DRF `ModelViewSet` for CRUD resources and custom `APIView` components for complex queries, file handlers, and code calculations.
- **Dual Authenticator Setup:** Custom authentication backend (`UsuarioNegocioBackend`) designed for business user lookup in `USUARIO` alongside Django fallback `ModelBackend` for admin interface.

---

## 3. Directory Structure

```
AplicacionMoldesBackEnd/
├── .gitignore
└── backend/
    ├── manage.py                         # Django administrative runner
    ├── requirements.txt                  # Python dependencies
    ├── backend/                          # Django Project Configuration Core
    │   ├── __init__.py
    │   ├── asgi.py                       # ASGI configuration for async execution
    │   ├── wsgi.py                       # WSGI entrypoint for web servers (Gunicorn/Waitress)
    │   ├── settings.py                   # Primary settings (DB, Auth, CORS, Installed Apps)
    │   └── urls.py                       # Global URL routing table (/api/ root routes)
    └── app/                              # Application Modules Directory
        ├── __init__.py
        ├── auth_app/                     # JWT Authentication Module (Stubs / Pending Implementation)
        │   ├── backends.py               # Custom UsuarioNegocioBackend (0 KB - to be implemented)
        │   ├── serializers.py            # Auth JWT Serializers (0 KB)
        │   ├── views.py                  # Login, Refresh, Logout, Me endpoints (0 KB)
        │   └── urls.py                   # /api/auth/ routing
        ├── documents/                    # File & Document Upload Module
        │   ├── models.py                 # Imagen model & upload_to_path logic
        │   ├── serializers.py            # DocumentoSerializer
        │   ├── views.py                  # DocumentoUploadView & DocumentoDetailView
        │   └── urls.py                   # /api/documents/ endpoints
        ├── herramental/                  # Core Business Domain (Molds & Tooling)
        │   ├── models.py                 # HerramentalEspecifico, DieSet, Catalogs, Properties
        │   ├── serializers.py            # HerramentalEspecificoSerializer (ReadOnly fields & FKs)
        │   ├── views.py                  # ViewSets, _construir_codigo, NextConsecutiveView, PropiedadesHerraView
        │   └── urls.py                   # /api/herramental_especifico/, /api/propiedades-herramental/, etc.
        ├── ipsl/                         # Forge Plant Production Integration
        │   ├── models.py                 # OrdenProduccionForja -> v_plantaVirtual DB view
        │   ├── serializers.py            # OrdenProduccionForjaSerializer
        │   ├── views.py                  # ReadOnlyModelViewSet for plant orders
        │   └── urls.py                   # /api/ordenes-produccion/
        ├── posicion/                     # Warehouse Location Hierarchy (Piso, Estanteria, Ubicacion)
        │   ├── models.py                 # Piso, Estanteria, UbicacionHerramental
        │   ├── serializers.py            # Location serializers
        │   ├── views.py                  # PisoViewSet, EstanteriaViewSet, UbicacionViewSet
        │   └── urls.py                   # /api/pisos/, /api/estanterias/, /api/ubicaciones/
        ├── produccion/                   # Machines & Production Activities
        │   ├── models.py                 # Maquina, EstadoMaquina, TipoMaquina, Actividad
        │   ├── serializers.py            # MaquinaSerializer, MaquinaReadSerializer, ActividadSerializer
        │   ├── views.py                  # MaquinaViewSet, ActividadViewSet
        │   └── urls.py                   # /api/maquinas/, /api/actividades/
        ├── usuarios/                     # User & Role Management
        │   ├── models.py                 # Usuario, TipoUsuario, Cargo (unmanaged SQL models)
        │   ├── serializers.py            # UsuarioSerializer, UsuarioReadSerializer (hides password)
        │   ├── views.py                  # UsuarioViewSet (ModelViewSet)
        │   └── urls.py                   # /api/usuarios/
        └── temp/                         # QR Scanner Import Staging Data
            ├── models.py                 # DataQRFile -> sabana_qr_files table
            ├── serializers.py            # DataQRFileSerializer
            ├── views.py                  # DataQRFileViewSet
            └── urls.py                   # /api/sabana_qr_files/
```

---

## 4. Key Modules & User Flows

### A. Automatic Code Calculation & Creation Flow (`herramental`)
```
  [Frontend User Interface]
             │
             ├── 1. User selects Herramental (H), Tipo (T), and Familia (F) dropdowns
             │
             ▼
  [GET /api/herramental/next-consecutive?h=1&t=2&f=5]
             │
             ├── Executes _construir_codigo(id_herramental, id_tipo, id_familia)
             ├── Fetches prefixes from DB (e.g. M, E, HX -> base "ME-HX")
             ├── Scans existing codes matching base prefix and finds MAX consecutive
             │
             ▼
  [Returns JSON Payload]
  { "nextValue": 3, "codigo_completo": "ME-HX03", "codigo_base": "ME-HX", "consecutivo_fmt": "03" }
             │
             ├── 2. User submits POST /api/herramental_especifico/ with form payload
             │
             ▼
  [POST /api/herramental_especifico/]
             │
             ├── Recalculates code server-side
             ├── Checks if code exists in DB (returns 409 Conflict if collision occurs)
             └── Saves new HerramentalEspecifico record -> returns 201 Created
```

### B. Single-Request Catalog Consolidation Flow (`herramental`)
- **Endpoint:** `GET /api/propiedades-herramental/`
- **Purpose:** Instead of forcing the SPA client to fire 3 parallel HTTP requests on page load, `PropiedadesHerraView` queries `Acero`, `Dureza`, and `Proveedor` tables in parallel and aggregates them into a unified payload:
  ```json
  {
    "aceros": [ { "ac_IdAcero": 1, "ac_DescripAcero": "D2" } ],
    "durezas": [ { "du_IdDureza": 1, "du_ValorDureza": "58-62 HRC" } ],
    "proveedores": [ { "pr_IdProveedor": 1, "pr_NombreProv": "Aceros S.A." } ]
  }
  ```

### C. Technical Document Upload & File Handling Flow (`documents`)
- **Endpoint:** `POST /api/documents/` (`multipart/form-data`)
- **File System Processing:** `upload_to_path` generates timestamped filenames (`YYYYMMDD_HHMMSS_<nombre_limpio>.<ext>`) and routes files to target subdirectories based on extension:
  - `.pdf` → `pdf/`
  - `.jpg`, `.png`, `.jpeg` → `imagenes/`
  - `.doc`, `.docx` → `docs/`
- **Storage Target:** Files stored physically under `MEDIA_ROOT` (`E:/FileServer/media` in current settings), accessible via static URL `/media/<folder>/<filename>`.

---

## 5. Backend Database Schema & API Contracts

### A. SQL Server Tables & Unmanaged Models Mapping

| Django App | Model Name | SQL Server Table / View | Key Primary & Foreign Keys |
| :--- | :--- | :--- | :--- |
| `herramental` | `HerramentalEspecifico` | `HERRAMENTALESPECIFICO` | PK: `hesp_IdHerramentalEspecifico`. FKs to `Piso`, `Estanteria`, `UbicacionHerramental`, `TipoHerramental`, `Familia`, `EstadoHerramental`, `Maquina`, `Actividad`, `DieSet`, `Chatarrizacion`, `OrdenProduccion`, `Prestamo` |
| `herramental` | `TipoHerramental` | `TIPOHERRAMENTAL` | PK: `th_IdTipoHerramental`, Code: `th_CodigoTipoHerramental` |
| `herramental` | `Familia` | `FAMILIA` | PK: `fa_IdFamilia`, Code: `fa_CodigoFamilia` |
| `herramental` | `EstadoHerramental` | `ESTADOHERRAMENTAL` | PK: `eh_IdEstadoHerr` |
| `herramental` | `DieSet` | `DIESET` | PK: `di_IdDieSet`. FKs to `Piso`, `Estanteria`, `UbicacionHerramental` |
| `herramental` | `Acero`, `Dureza`, `Proveedor` | `ACERO`, `DUREZA`, `PROVEEDOR` | Catalogs for tooling materials |
| `posicion` | `Piso` | `PISO` | PK: `pi_IdPiso`, Code: `pi_NumeroPiso` |
| `posicion` | `Estanteria` | `ESTANTERIA` | PK: `es_IdEstanteria`. FK to `Piso` |
| `posicion` | `UbicacionHerramental` | `UBICACIONHERRAMENTAL` | PK: `uh_IdUbicacionHerr`. Unique `(uh_NumeroFila, uh_NumeroColumna, uh_NumeroPosicion)` |
| `produccion` | `Maquina` | `MAQUINA` | PK: `ma_IdMaquina`. FKs to `EstadoMaquina`, `TipoMaquina` |
| `produccion` | `Actividad` | `ACTIVIDAD` | PK: `ac_IdActividad`. FK to `Usuario` |
| `usuarios` | `Usuario` | `USUARIO` | PK: `us_IdUsuario`. FKs to `TipoUsuario`, `Cargo` |
| `documents` | `Imagen` | `IMAGEN` | PK: `im_IdImagen`, Field: `im_RutaRelativa` |
| `ipsl` | `OrdenProduccionForja` | `v_plantaVirtual` (View) | PK: `Orden de Produccion` (`consecutivo_op`) |
| `temp` | `DataQRFile` | `sabana_qr_files` | PK: `MOLDE` (`molde`) |

---

### B. Summary API Contracts Table

| Method | Endpoint Path | Description | Query / Body Parameters | Response Code |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/api/herramental_especifico/` | List all specific tooling records | `search`, `ordering` | `200 OK` |
| `POST` | `/api/herramental_especifico/` | Create specific tooling record with auto code | `{ hesp_IdHerramental, hesp_IdTipoHerramental, hesp_IdFamilia, ... }` | `201 Created` / `409 Conflict` |
| `GET` | `/api/herramental/next-consecutive` | Preview calculated code & next consecutive | `?h=<id>&t=<id>&f=<id>` | `200 OK` / `400 Bad Request` |
| `GET` | `/api/propiedades-herramental/` | Consolidated catalog (Steel, Hardness, Supplier) | None | `200 OK` |
| `GET` | `/api/diesets/` | List / CRUD Die Sets | standard DRF filters | `200 OK` |
| `GET` | `/api/documents/` | List uploaded files & metadata | None | `200 OK` |
| `POST` | `/api/documents/` | Upload document file | `multipart/form-data` (`ruta_relativa`, `nombre_imagen`) | `201 Created` |
| `GET` | `/api/documents/<id>/` | Retrieve document details by ID | None | `200 OK` / `404 Not Found` |
| `GET` | `/api/pisos/` | List warehouse floors | None | `200 OK` |
| `GET` | `/api/estanterias/` | List shelving units | None | `200 OK` |
| `GET` | `/api/ubicaciones/` | List row/column/position coordinates | None | `200 OK` |
| `GET` | `/api/maquinas/` | List plant machines | `search`, `ordering`, `estado`, `tipo` | `200 OK` |
| `GET` | `/api/usuarios/` | List business users | `search`, `ordering` | `200 OK` |
| `POST` | `/api/auth/login/` | Request JWT token pair *(Pending implementation in auth_app)* | `{ "user": "...", "password": "..." }` | `200 OK` / `401 Unauthorized` |
| `POST` | `/api/auth/refresh/` | Refresh access token *(Pending implementation)* | `{ "refresh": "..." }` | `200 OK` / `401 Unauthorized` |

---

## 6. Architecture Patterns & Guidelines for Plan Integration

When planning future features or refactoring modules in this codebase, adhere to the following established conventions:

1. **Unmanaged ORM Rules (`managed = False`):**
   - Do **NOT** run `python manage.py makemigrations` to modify DB schema.
   - Any database column addition, type change, or new table MUST be executed directly in SQL Server first, then updated in the corresponding Django `models.py` class with explicit `db_column='...'`.
2. **Read vs. Write Serializer Separation (`get_serializer_class`):**
   - Override `get_serializer_class(self)` in ViewSets to supply a `ReadSerializer` for `['list', 'retrieve']` (exposing nested objects or `ReadOnlyField` source aliases) and a flat `WriteSerializer` for `['create', 'update', 'partial_update']` accepting integer Foreign Keys.
3. **Consolidated API Endpoint Pattern:**
   - For form initialization dropdowns, consolidate related small catalogs into a single GET endpoint (`APIView`) returning a dictionary of lists to optimize mobile/web UI latency.
4. **Optimistic Code Calculation & Collision Safeguards:**
   - High-concurrency creation endpoints must calculate sequential values server-side inside `create()` method and perform explicit `.exists()` checks before persisting, returning standard `HTTP 409 Conflict` on collisions.
5. **Path & Environment Variable Sanitization:**
   - Always reference external file directories via `django.conf.settings` or `os.getenv()`. Never hardcode local drive letters like `E:/...` directly inside python source files.

---

## 7. DevOps Evaluations & Security Vulnerability Assessment

> [!CAUTION]
> **CRITICAL SECURITY RISKS IDENTIFIED IN CURRENT BACKEND CODEBASE**

### Critical Security Vulnerabilities:
1. **Plain-Text Password Storage (`usuarios/models.py`):**
   - `Usuario.password` is mapped to `us_Password` with `max_length=20`. Passwords are being read/written in plain text.
   - **Remediation:** Implement PBKDF2, Argon2, or BCrypt hashing using Django's `make_password` / `check_password` before storing passwords.
2. **Global Permissive Access Control (`settings.py`):**
   - `REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES']` is set to `['rest_framework.permissions.AllowAny']`.
   - `permission_classes = [IsAuthenticated]` is commented out in almost all ViewSets (`HerramentalViewSet`, `UsuarioViewSet`, `MaquinaViewSet`, etc.).
   - **Remediation:** Enforce `IsAuthenticated` globally in `REST_FRAMEWORK` settings and selectively use `@permission_classes([AllowAny])` on public login endpoints.
3. **Overly Permissive CORS Configuration (`settings.py`):**
   - `CORS_ALLOW_ALL_ORIGINS = True` is enabled in `settings.py`. This ignores `CORS_ALLOWED_ORIGINS` and opens the API to cross-site request forgery/abuse.
   - **Remediation:** Bind `CORS_ALLOW_ALL_ORIGINS` to `DEBUG` mode only or remove it entirely in favor of explicit domain whitelist.
4. **Hardcoded Debug Mode & Secret Key Fallbacks:**
   - `DEBUG = True` is hardcoded on line 31 of [settings.py](file:///c:/Users/tdigital/OneDrive%20-%20FORJAS%20BOLIVAR/Documentos/Backend%20GHFB/AplicacionMoldesBackEnd/backend/backend/settings.py#L31).
   - `SECRET_KEY` loads from `.env` without validation if empty.
5. **Incomplete Auth Module (`app.auth_app`):**
   - [settings.py](file:///c:/Users/tdigital/OneDrive%20-%20FORJAS%20BOLIVAR/Documentos/Backend%20GHFB/AplicacionMoldesBackEnd/backend/backend/settings.py#L246) lists `'app.auth_app.backends.UsuarioNegocioBackend'` in `AUTHENTICATION_BACKENDS`, but `backends.py`, `views.py`, and `serializers.py` inside `app/auth_app` are 0-byte empty files. JWT authentication is broken or non-functional.
6. **Hardcoded Media Storage Path:**
   - `MEDIA_ROOT = 'E:/FileServer/media'` in `settings.py` hardcodes a specific Windows drive letter. This breaks containerized deployment (Docker) or Linux server hosting.

### Code Quality & Architectural Technical Debt:
1. **Duplicate Model Definitions:**
   - `Piso`, `Estanteria`, and `UbicacionHerramental` models are declared in **both** [app/herramental/models.py](file:///c:/Users/tdigital/OneDrive%20-%20FORJAS%20BOLIVAR/Documentos/Backend%20GHFB/AplicacionMoldesBackEnd/backend/app/herramental/models.py#L118) and [app/posicion/models.py](file:///c:/Users/tdigital/OneDrive%20-%20FORJAS%20BOLIVAR/Documentos/Backend%20GHFB/AplicacionMoldesBackEnd/backend/app/posicion/models.py#L3).
   - **Remediation:** Consolidate warehouse location models under `app/posicion` and import them in `herramental`.
2. **Missing Unit & Integration Test Suite:**
   - `tests.py` in all app subdirectories are empty stubs (`63 bytes`).
3. **Wildcard Imports:**
   - `from .models import *` and `from .serializers import *` used in `herramental/views.py`.

---

## 8. Tasks to be Done (Prioritized Roadmap)

### Phase 1: High Priority (P0) — Security & Authentication Fixes
- [ ] **Complete `app/auth_app` Implementation:**
  - Implement `UsuarioNegocioBackend` in [auth_app/backends.py](file:///c:/Users/tdigital/OneDrive%20-%20FORJAS%20BOLIVAR/Documentos/Backend%20GHFB/AplicacionMoldesBackEnd/backend/app/auth_app/backends.py) to authenticate against `USUARIO` table using hashed passwords.
  - Implement Custom JWT Token Serializers and Views (`LoginView`, `RefreshTokenView`, `LogoutView`, `MeView`).
  - Wire `/api/auth/` routes in [auth_app/urls.py](file:///c:/Users/tdigital/OneDrive%20-%20FORJAS%20BOLIVAR/Documentos/Backend%20GHFB/AplicacionMoldesBackEnd/backend/app/auth_app/urls.py).
- [ ] **Password Hashing Migration:**
  - Update `Usuario` creation/update logic to hash passwords using Django `make_password`.
  - Create a migration script to hash existing plain-text passwords in SQL Server `USUARIO`.
- [ ] **Lock Down API Permissions & CORS:**
  - Switch `DEFAULT_PERMISSION_CLASSES` in `settings.py` to `IsAuthenticated`.
  - Uncomment `permission_classes = [IsAuthenticated]` on protected ViewSets.
  - Set `CORS_ALLOW_ALL_ORIGINS = False` in production environment.

### Phase 2: Medium Priority (P1) — Architecture & Refactoring
- [ ] **Eliminate Model Duplication:**
  - Remove duplicate `Piso`, `Estanteria`, and `UbicacionHerramental` definitions from `app/herramental/models.py` and import them directly from `app.posicion.models`.
- [ ] **Refactor Hardcoded Configurations:**
  - Replace hardcoded `MEDIA_ROOT = 'E:/FileServer/media'` with configurable environment variable `os.getenv('MEDIA_ROOT', BASE_DIR / 'media')`.
  - Move `DEBUG` setting to environment variable (`DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() == 'true'`).
- [ ] **Clean Up Wildcard Imports:**
  - Replace `from .models import *` in `herramental/views.py` and `serializers.py` with explicit class imports.

### Phase 3: Low Priority (P2) — Testing & DevOps Improvements
- [ ] **Build Automated Test Suite:**
  - Write unit tests for `_construir_codigo()` edge cases (missing IDs, consecutivo rollover, invalid characters).
  - Write integration tests for API endpoints (`HerramentalEspecificoViewSet`, `DocumentoUploadView`).
- [ ] **DevOps & Containerization:**
  - Add `Dockerfile` and `docker-compose.yml` configured with `gunicorn` / `waitress` and Microsoft ODBC Driver 17/18 for SQL Server.
  - Create a sample `.env.example` file detailing required environment parameters (`DATABASE_SERVER`, `DATABASE_BD`, `DATABASE_USER`, `DATABASE_PASSWORD`, `SECRET_KEY`, `MEDIA_ROOT`).
