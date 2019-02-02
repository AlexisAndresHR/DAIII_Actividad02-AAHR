import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, nombre):
        productos = config.model_productos.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.delete_producto(productos) # Envia el registro y renderiza delete.html

    def POST(self, nombre):
        formulario = web.input() # Crea un objeto formulario con los datos enviados con el formulario
        nombre = formulario['nombre'] # Obtiene el nombre almacenado en el formulario
        config.model_productos.delete_producto(nombre) # Borra el registro del nombre seleccionado
        raise web.seeother('/productos') # Renderiza a raiz
