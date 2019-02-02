import config as config # Importa el archivo config

db = config.db # Crea un objeto DB del objeto DB creado en config

'''
Metodo para seleccionar todos los registros de la tabla clientes
'''
def select_clientes():
    try:
        return db.select('clientes') # Selecciona todos los registros de la tabla clientes
    except Exception as e:
        print "Model select_clientes Error {}".format(e.args)
        print "Model select_clientes Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el nombre dado
'''

def select_nombre(nombre):
    try:
        return db.select('clientes', where='nombre=$nombre', vars=locals())[0] # Selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre Error {}".format(e.args)
        print "Model select_nombre Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro en clientes
'''
def insert_cliente(nombre, apellido_pat, apellido_mat, edad, telefono):
    try:
        return db.insert('clientes', nombre=nombre, apellido_pat=apellido_pat, apellido_mat=apellido_mat, edad=edad, telefono=telefono) # Inserta un registro en clientes
    except Exception as e:
        print "Model insert_clientes Error {}".format(e.args)
        print "Model insert_clientes Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el nombre recibido
'''
def delete_cliente(nombre):
    try:
        return db.delete('clientes', where='nombre=$nombre', vars=locals()) # Borra un registro de clientes
    except Exception as e:
        print "Model delete_clientes Error {}".format(e.args)
        print "Model delete_clientes Message {}".format(e.message)
        return None

'''
Metodo para actualizar los datos de clientes, segun lo recibido del formulario
'''
def update_cliente(nombre, apellido_pat, apellido_mat, edad, telefono): # Actualiza los datos de clientes que coincidan con el nombre
    try:
        return db.update('clientes',
            apellido_pat=apellido_pat,
            apellido_mat=apellido_mat,
            edad=edad,
            telefono=telefono,
            where='nombre=$nombre',
            vars=locals())
    except Exception as e:
        print "Model update_clientes Error {}".format(e.args)
        print "Model update_clientes Message {}".format(e.message)
        return None
