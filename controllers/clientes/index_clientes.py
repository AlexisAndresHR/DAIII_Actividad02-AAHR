import web
import config as config


class IndexC:
    def __init__(self):
        pass

    def GET(self):
        clientes = config.model_clientes.select_clientes().list() # Selecciona todos los registros de Clientes
        return config.render.index_clientes(clientes) # Envia todos los registros y renderiza index_clientes.html
