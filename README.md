# 🚀 Proyecto de Automatización de API

## 📋 Descripción

Este proyecto implementa **pruebas automatizadas** para una API de importación de datos siguiendo las mejores prácticas de **QA Automation**. Utiliza **Pytest** como framework de testing y sigue el patrón **Page Object Model (POM)** para mantener el código organizado y escalable.

## 🏗️ Estructura del Proyecto

```
Artekium/
├── 📁 config/
│   └── env_config.py              # Configuración de ambientes (test/dev)
├── 📁 utils/
│   ├── db_utils.py                # Utilidades para conexión a BD
│   └── sql_files/
│       └── select_personId.sql    # Consultas SQL parametrizadas
├── 📁 pages/
│   ├── import_api.py              # Clase principal de la API (POM)
│   ├── test_utils.py              # Utilidades para tests
│   └── auth_data.json             # Template de autenticación
├── 📁 tests/
│   ├── 📁 data/
│   │   └── negative_validation_cases.json  # Casos de prueba negativos
│   ├── 📁 test_suites/            # Organización futura de tests
│   └── test_import.py             # Tests principales
├── 📁 reports/                    # Reportes de ejecución
├── conftest.py                    # Configuración de Pytest y fixtures
├── requirements.txt               # Dependencias del proyecto
├── .env                          # Variables de entorno
└── README.md                     # Este archivo
```

## 🚀 Instalación y Configuración

### 1. **Requisitos Previos**

- **Python 3.8+** desde [python.org](https://www.python.org/downloads/)
- **MySQL Server** configurado y funcionando
- **Editor de código** (VS Code, PyCharm, etc.)

### 2. **Instalación**

```bash
# Clonar el proyecto
git clone [<url-del-repositorio>](https://github.com/FamaMatias/pytest_challenge)

# Crear entorno virtual (recomendado)
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt
```

### 3. **Configuración de Variables de Entorno**

Crear archivo `.env` en la raíz del proyecto:

```env
# Configuración de Base de Datos MySQL
DB_HOST=localhost
DB_USER=tu_usuario_mysql
DB_PASSWORD=tu_password_mysql
DB_NAME=test_worldsys

# Configuración de Autenticación API
USER_AUTH=usuario_demo
PASS_AUTH=clave_demo
```

**⚠️ Importante:** Reemplaza con tus credenciales reales.

## 🧪 Ejecución de Tests

### **Comando de Ejecución**
```bash
# Ejecutar el test de importación
pytest test_import.py
```


## 📊 Funcionalidades del Proyecto

### **1. Autenticación Automática**
- **Método**: `ImportApi.get_token()`
- **Archivo**: `pages/auth_data.json`
- **Proceso**: Obtiene token Bearer para autenticación

### **2. Importación de Datos**
- **Método**: `ImportApi.post_import(person_id)`
- **Endpoint**: Configurado por ambiente
- **Headers**: Bearer token + Content-Type JSON

### **3. Validación de Base de Datos**
- **Archivo**: `utils/sql_files/select_personId.sql`
- **Función**: `execute_sql_file()` con parámetros
- **Verificación**: Confirmar que los datos se guardaron correctamente

### **4. Tests Parametrizados**
- **Archivo**: `tests/data/negative_validation_cases.json`
- **Función**: `load_cases()` para cargar casos de prueba
- **Cobertura**: Validaciones de casos negativos (sad paths)

## **📁 config/env_config.py**
```python
# Configuración de ambientes disponibles
configs = {
    "test": {
        "base_url": "https://api.test.worldsys.ar",
        "auth_url": "https://api.auth.test.ar"
    },
    "dev": {
        "base_url": "https://api.dev.worldsys.ar", 
        "auth_url": "https://api.auth.dev.ar"
    }
}
```

## 🎯 Casos de Prueba

### **Happy Path Test (Caso Exitoso)**
El test de caso exitoso valida el flujo completo cuando todo funciona correctamente:

1. **Envío de datos**: Se envía un personId válido a la API
2. **Validación de respuesta**: Se verifica que la API responda con código 200 (éxito)
3. **Verificación en base de datos**: Se consulta la BD para confirmar que el registro se guardó
4. **Validación de datos**: Se confirma que el personId existe y coincide exactamente con el enviado

### **Sad Path Tests (Casos Negativos - Parametrizados)**
Los tests de casos negativos validan el comportamiento cuando se envían datos inválidos:

1. **Envío de datos inválidos**: Se envían personIds que no deberían ser aceptados
2. **Validación de errores**: Se verifica que la API responda con el código de error esperado
3. **Reporte de resultados**: Se muestran los detalles del error para análisis



## 🛠️ Dependencias

```txt
pytest                    # Framework de testing
requests                  # Cliente HTTP para APIs
mysql-connector-python    # Driver MySQL
python-dotenv            # Variables de entorno
```



