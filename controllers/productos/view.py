import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, nombre):
        producto = config.model_productos.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.view_producto(producto) # Envia el registro y renderiza view_producto.html
