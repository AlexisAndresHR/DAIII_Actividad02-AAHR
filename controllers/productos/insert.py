import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):
        return config.render.insert_producto() # Renderiza la pagina insert_producto.html

    def POST(self):
        formulario = web.input() # Almacena los datos del formulario
        nombre = formulario['nombre'] # Almacena el nombre escrito en el input
        marca = formulario['marca']
        precio = formulario['precio']
        categoria = formulario['categoria']
        descripcion = formulario['descripcion']
        config.model_productos.insert_producto(nombre, marca, precio, categoria, descripcion) # Llama al metodo insert_producto y le pasa los datos guardados
        raise web.seeother('/productos') # Redirecciona al index_productos.html
