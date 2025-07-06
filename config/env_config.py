def get_env_config(env):
    """
    Retorna la configuración de URLs base y de autenticación según el ambiente seleccionado.
    Lanza ValueError si el ambiente no es reconocido.
    """
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
    if env not in configs:
        raise ValueError(f"Ambiente desconocido: {env}")
    return configs[env] 