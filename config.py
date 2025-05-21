import os

class Config:
    """
    Configuración principal para la aplicación Flask.
    """

    # Clave secreta para sesiones y formularios
    SECRET_KEY = 'proyecto-abdiel123clave-unica'

    # URI para conectar a MySQL local con XAMPP (sin contraseña)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/publicacion_articulos'

    # Desactiva el seguimiento de cambios (recomendado)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
