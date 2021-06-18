from Aplicacion import Aplicacion
from Lista import Lista

class Controlador:
    __app=None
    __lista=None

    def __init__(self):
        self.__lista=Lista()
        self.__app=Aplicacion(self.__lista.getLista())
        self.actualizar()
        self.__app.getVentana().mainloop()

    def actualizar(self):
        funcion=self.__app.actualizar
        argumento=self.__lista.getLista()
        self.__app.getButtonAct().config(command= lambda: funcion(argumento))
        