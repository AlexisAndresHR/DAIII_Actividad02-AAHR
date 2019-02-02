import web # Importa la libreria web.py
import application.models.model_clientes as model_clientes # Importa el model_clientes


render = web.template.render('application/views/clientes/', base='master') # Configura la ubicacion de las vistas
