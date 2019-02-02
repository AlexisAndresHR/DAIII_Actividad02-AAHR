import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre):
        producto = config.model_productos.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.update_producto(producto) # Envia el registro y renderiza update_producto.html (productos)

    def POST(self, marca, precio, categoria, descripcion):
        formulario = web.input() # Almacena los datos del formulario
        nombre = formulario['nombre'] # Almacena el nombre escrito en el input
        marca = formulario['marca']
        precio = formulario[precio]
        categoria = formulario['categoria']
        descripcion = formulario['descripcion']
        config.model_productos.update_producto(nombre, marca, precio, categoria, descripcion) # Llama al metodo update_producto y actualiza los datos
        raise web.seeother('/productos') # Redirecciona al index_productos.html
