import json
import os

def load_cases(json_filename, arg="argumento", status_name="expected_status"):
    """
    Carga casos de un archivo JSON y retorna una lista (argumento, expected_status).
    Permite reutilizar la función para diferentes tipos de validaciones.
    """
    json_path = os.path.join(os.path.dirname(__file__), "..", "tests", "data", json_filename)
    with open(json_path, "r") as f:
        return [(case[arg], case[status_name]) for case in json.load(f)] 