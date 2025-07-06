import requests
import json
import os
from config.env_config import get_env_config

class ImportApi:

    def __init__(self, env):
        """
        Inicializa la clase ImportApi con la configuración del ambiente seleccionado.
        Obtiene las URLs base y de autenticación según el ambiente.
        """
        config = get_env_config(env)
        self.base_url = config["base_url"]
        self.auth_url = config["auth_url"]
        self.token = self.get_token()

    def get_token(self):
        """
        Realiza una petición al endpoint de autenticación usando las credenciales del .env
        y retorna el token de acceso recibido en la respuesta.
        """
        username = os.getenv('USER_AUTH')
        password = os.getenv('PASS_AUTH')
        with open("pages/auth_data.json", "r") as f:
            template = f.read()
        body = template.replace("{usuario}", username).replace("{clave}", password)
        data = json.loads(body)
        try:
            response = requests.post(self.auth_url, json=data)
            response.raise_for_status()
            token = response.json().get("access_token")
            return token
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def post_import(self, person_id):
        """
        Realiza una petición POST al endpoint de importación con el personId indicado.
        Usa el token de autenticación obtenido previamente.
        Retorna la respuesta del servicio.
        """
        token = self.get_token()
        body = [{"personId": person_id}]
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        try:
            import_url = f"{self.base_url}/import"
            response = requests.post(import_url, json=body, headers=headers)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None
