import config as config # Importa el archivo config

db = config.db # Crea un objeto DB del objeto DB creado en config

'''
Metodo para seleccionar todos los registros de la tabla productos
'''
def select_productos():
    try:
        return db.select('productos') # Selecciona todos los registros de la tabla productos
    except Exception as e:
        print "Model select_productos Error {}".format(e.args)
        print "Model select_productos Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el nombre dado
'''

def select_nombre(nombre):
    try:
        return db.select('productos', where='nombre=$nombre', vars=locals())[0] # Selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre Error {}".format(e.args)
        print "Model select_nombre Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro en productos
'''
def insert_producto(nombre, marca, precio, categoria, descripcion):
    try:
        return db.insert('productos', nombre=nombre, marca=marca, precio=precio, categoria=categoria, descripcion=descripcion) # Inserta un registro en productos
    except Exception as e:
        print "Model insert_productos Error {}".format(e.args)
        print "Model insert_productos Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el nombre recibido
'''
def delete_producto(nombre):
    try:
        return db.delete('productos', where='nombre=$nombre', vars=locals()) # Borra un registro de productos
    except Exception as e:
        print "Model delete_productos Error {}".format(e.args)
        print "Model delete_productos Message {}".format(e.message)
        return None

'''
Metodo para actualizar los datos de productos, segun lo recibido del formulario
'''
def update_producto(nombre, marca, precio, categoria, descripcion): # Actualiza los datos de productos que coincidan con el nombre
    try:
        return db.update('productos',
            marca=marca,
            precio=precio,
            categoria=categoria,
            descripcion=descripcion,
            where='nombre=$nombre',
            vars=locals())
    except Exception as e:
        print "Model update_producto Error {}".format(e.args)
        print "Model update_producto Message {}".format(e.message)
        return None
