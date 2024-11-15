# Importa la función create_app desde el módulo todor
from todor import create_app
#Verifica si el script se está ejecutando directamente
if __name__ == '__main__':
    #Crea una instancia de la aplicación Flask
    app = create_app()
    # este codigo ejecuta la app en el servidor
    app.run() 