import os
import pytest
import json
from utils.db_utils import execute_sql_file
from pages.test_utils import load_cases

def test_import_happy_path(api_client, db_connection):
    """
    Test del caso exitoso (happy path) que valida:
    1. Envío de personId a la API
    2. Respuesta exitosa (200)
    3. Verificación en base de datos
    4. Reporte de resultados
    """
    person_id = 111
    
    response = api_client.post_import(person_id)
    
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"

    sql_template_path = os.path.join("utils", "sql_files", "select_personId.sql")
    result = execute_sql_file(db_connection, sql_template_path, (person_id,))
    
    # PASO 4: Validar que el personId se encontró en la BD
    assert len(result) > 0, f"El personId {person_id} no existe en la base de datos"
    assert result[0]['personId'] == person_id, f"El personId encontrado no coincide"

    print("test_happy_path Passed")
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")
    print(f"DB Result: {result}")


@pytest.mark.parametrize("person_id, expected_status", load_cases("negative_validation_cases.json", arg="argumento"))
def test_import_sad_paths(api_client, person_id, expected_status):
    """
    Test de casos negativos (sad paths) que valida:
    1. Envío de personId inválido a la API
    2. Respuesta con código de error esperado
    3. Reporte de resultados del error
    """
    response = api_client.post_import(person_id)

    print(f"Testing sad path with personId={person_id}")
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
    
    assert response.status_code == expected_status, \
        f"Expected status {expected_status}, got {response.status_code}"