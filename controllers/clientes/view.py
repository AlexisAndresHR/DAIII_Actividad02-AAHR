import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, nombre):
        cliente = config.model_clientes.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.view_cliente(cliente) # Envia el registro y renderiza view_cliente.html
