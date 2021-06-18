import requests

class Lista:
    __response=None
    __dic=dict()

    def getLista(self):
        self.__response = requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
        self.__dic = self.__response.json()
        lista = []
        for x in self.__dic:
            for k, v in x.items():
                nombre = v["nombre"]
                if nombre.startswith("Dolar"):
                    lista.append([v["nombre"], v["compra"], v["venta"]])
        return lista