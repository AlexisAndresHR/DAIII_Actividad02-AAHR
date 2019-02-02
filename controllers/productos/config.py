import web # Importa la libreria web.py
import application.models.model_productos as model_productos # Importa el model_productos


render = web.template.render('application/views/productos/', base='master') # Configura la ubicacion de las vistas