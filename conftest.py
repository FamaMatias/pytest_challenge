import pytest
import sys
import os
from pages.import_api import ImportApi
from utils.db_utils import get_connection, close_connection

@pytest.fixture(scope="session", autouse=True)
def setup_path():
    """
    Configura el path para que Pytest encuentre los tests en la carpeta tests/.
    """
    tests_path = os.path.join(os.path.dirname(__file__), 'tests')
    if tests_path not in sys.path:
        sys.path.insert(0, tests_path)

@pytest.fixture
def api_client():
    """
    Fixture que proporciona una instancia de ImportApi configurada para tests.
    """
    return ImportApi("test")

@pytest.fixture
def auth_token():
    """
    Fixture que retorna un token de autenticación válido.
    """
    api = ImportApi("test")
    return api.get_token()

@pytest.fixture
def db_connection():
    """
    Fixture que proporciona una conexión a la base de datos y la cierra automáticamente.
    """
    connection = get_connection()
    yield connection
    close_connection(connection)
