import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre):
        cliente = config.model_clientes.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.update_cliente(cliente) # Envia el registro y renderiza update_cliente.html (clientes)

    def POST(self, apellido_pat, apellido_mat, edad, telefono):
        formulario = web.input() # Almacena los datos del formulario
        nombre = formulario['nombre'] # Almacena el nombre escrito en el input
        apellido_pat = formulario['apellido_pat']
        apellido_mat = formulario['apellido_mat']
        edad = formulario['edad']
        telefono = formulario['telefono']
        config.model_clientes.update_cliente(nombre, apellido_pat, apellido_mat, edad, telefono) # Llama al metodo update_cliente y actualiza los datos
        raise web.seeother('/clientes') # Redirecciona al index_clientes.html
