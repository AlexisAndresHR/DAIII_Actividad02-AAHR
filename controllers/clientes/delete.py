import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, nombre):
        clientes = config.model_clientes.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.delete_cliente(clientes) # Envia el registro y renderiza delete_cliente.html

    def POST(self, nombre):
        formulario = web.input() # Crea un objeto formulario con los datos enviados con el formulario
        nombre = formulario['nombre'] # Obtiene el nombre almacenado en el formulario
        config.model_clientes.delete_cliente(nombre) # Borra el registro del nombre seleccionado
        raise web.seeother('/clientes') # Renderiza a raiz
