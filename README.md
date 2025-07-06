# 🚀 Proyecto de Automatización de API - Artekium

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
├── .env                          # Variables de entorno (crear)
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
git clone <url-del-repositorio>
cd Artekium

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

## 🔧 Componentes Principales

### **📁 config/env_config.py**
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

### **📁 pages/import_api.py**
Clase principal que implementa el **Page Object Model**:
- **`__init__(env)`**: Inicializa con configuración del ambiente
- **`get_token()`**: Autenticación automática
- **`post_import(person_id)`**: Envío de datos a la API

### **📁 utils/db_utils.py**
Utilidades para conexión a base de datos:
- **`get_connection()`**: Conexión MySQL con variables de entorno
- **`execute_sql_file()`**: Ejecución de consultas SQL parametrizadas
- **`close_connection()`**: Cierre seguro de conexiones

### **📁 conftest.py**
Configuración de Pytest y fixtures:
- **`api_client`**: Instancia de ImportApi para tests
- **`db_connection`**: Conexión a BD con cleanup automático
- **`auth_token`**: Token de autenticación reutilizable

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

### **Parametrización con load_cases()**
La función `load_cases()` permite cargar múltiples casos de prueba desde un archivo JSON:

- **Carga automática**: Lee todos los casos de prueba del archivo JSON
- **Flexibilidad**: Permite agregar nuevos casos sin modificar el código del test
- **Reutilización**: Se puede usar para diferentes tipos de validaciones
- **Organización**: Separa los datos de prueba de la lógica del test

**Ejemplos de casos de prueba:**
- PersonId muy grande → Error 404
- PersonId vacío → Error 400  
- PersonId con letras → Error 422

## 📈 Reportes y Resultados

### **Salida de Consola**
```
test_happy_path Passed
Status Code: 200
Response Body: {"status": "success", "message": "Data imported"}
DB Result: [{'personId': 111, 'name': 'John Doe', ...}]
```


## 🛠️ Dependencias

```txt
pytest                    # Framework de testing
requests                  # Cliente HTTP para APIs
mysql-connector-python    # Driver MySQL
python-dotenv            # Variables de entorno
```

## 🎨 Patrones de Diseño

### **Page Object Model (POM)**
- **`ImportApi`**: Encapsula interacciones con la API
- **Separación**: Lógica de negocio vs tests
- **Reutilización**: Métodos compartidos entre tests

### **Fixtures de Pytest**
- **Setup/Teardown**: Automático con `yield`
- **Scope**: `session` para configuración global
- **Inyección**: Dependencias automáticas en tests

### **Parametrización**
- **Datos externos**: JSON para casos de prueba
- **Flexibilidad**: Fácil agregar nuevos casos
- **Mantenimiento**: Separación de datos y lógica



