import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):
        return config.render.insert_cliente() # Renderiza la pagina insert_cliente.html

    def POST(self):
        formulario = web.input() # Almacena los datos del formulario
        nombre = formulario['nombre'] # Almacena el nombre escrito en el input
        apellido_pat = formulario['apellido_pat']
        apellido_mat = formulario['apellido_mat']
        edad = formulario['edad']
        telefono = formulario['telefono']
        config.model_clientes.insert_cliente(nombre, apellido_pat, apellido_mat, edad, telefono) # Llama al metodo insert_cliente y le pasa los datos guardados
        raise web.seeother('/clientes') # Redirecciona al index_clientes.html
