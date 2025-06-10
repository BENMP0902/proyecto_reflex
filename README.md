# 🚀 Proyecto_reflex

Aplicación web creada con [Reflex](https://reflex.dev/) que implementa un sistema de inicio de sesión seguro, manejo de autenticación con JWT y conexión a una base de datos PostgreSQL. 
Este proyecto forma parte de una práctica didáctica para aprender programación avanzada en Python.

## 🧩 Tecnologías utilizadas

- 🔧 **Python 3.10+**
- 🎨 **Reflex** (Frontend + Backend)
- 🛡 **JWT (JSON Web Tokens)** para autenticación
- 🔐 **bcrypt** para encriptación de contraseñas
- 🗃 **PostgreSQL** como base de datos relacional
- ⚙️ **SQLModel** como ORM
- 🐘 **Alembic** para migraciones de base de datos
- 📦 **dotenv** para manejar variables de entorno

---

## 🧪 Funcionalidades principales

- ✅ Registro e inicio de sesión de usuarios
- ✅ Encriptación segura de contraseñas
- ✅ Generación y verificación de tokens JWT
- ✅ Interfaz protegida por autenticación (`/dashboard`)
- ✅ Manejo de sesiones mediante cookies seguras
- ✅ Variables sensibles fuera del código en `.env`

---

## ⚙️ Configuración inicial

### 1. Clonar el repositorio

```bash
git clone https://github.com/BENMP0902/Proyecto_reflex.git
cd Proyecto_reflex
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto con este contenido:

```env
DATABASE_URL=postgresql+psycopg2://postgres:TU_PASSWORD@localhost:'tu_puerto'/proyecto_reflex
SECRET_KEY='tu_clave_secreta'
```

### 5. Ejecutar migraciones

```bash
alembic upgrade head
```

## 🚀 Ejecutar el proyecto

```bash
reflex run
```

Abre el navegador en http://localhost:3000

## 📂 Estructura del proyecto

```bash
Proyecto_reflex/
├── Proyecto_reflex/
│   ├── auth.py
│   ├── models/
│   ├── pages/
│   ├── __init__.py
│   └── rxconfig.py
├── alembic/
├── assets/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 🛡 Seguridad

- Las credenciales de conexión y la clave secreta se almacenan en `.env`, que está ignorado por Git.
- Nunca subas tus credenciales personales al repositorio.

## ✍️ Autor

Ben, estudiante de Ingeniería en Software 👨‍💻
