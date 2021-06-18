from tkinter import *
from tkinter import ttk
from datetime import datetime

class Aplicacion:
    __ventana=None
    __mainFrame=None
    __label=dict()

    def __init__(self,lista):
        self.__ventana=Tk()
        self.__ventana.title("Cotizacion")
        #self.__ventana.resizable(False,False)

        mainFrameStyle={'bg':"#85BB65",'borderwidth':2}
        self.__mainFrame=Frame(self.__ventana,**mainFrameStyle)
        self.__mainFrame.grid(column=0,row=0,sticky=(N,W,E,S))

        self.__label=dict()
        self.__opcion={"padx":30,"pady":5}

        opcion=self.__opcion

        #TITULO
        labelTitulo=Label(self.__mainFrame,text="COTIZACION DEL DOLAR",anchor="n",width=40,foreground="#fff",bg="#85BB65",font=("Arial",20)).grid(row=0)

        #MARCO-FONDO
        marco=Frame(self.__mainFrame,bg="#E4E8D1")
        marco.grid(row=4,column=0)

        self.construir(lista,marco)

        #BOTONES
        style=ttk.Style()
        self.__botonSalir=ttk.Button(marco,text="Salir",command=self.__ventana.destroy)
        self.__botonSalir.grid(row=45,column=0,columnspan=2)
        self.__botonActualizar=ttk.Button(marco,text="Actualizar")
        self.__botonActualizar.grid(row=47,column=0,columnspan=2,rowspan=4)
        style.configure("BW.TLabel",width=20)

        #FECHA Y HORA
        self.__fechaHora = StringVar() #Guarda la fecha y hora, se enlaza a un label
        self.__fechaHora.set(self.getFecha())
        self.__fecha = ttk.Label(marco, textvariable=self.__fechaHora, width=18, foreground="#85BB65",background="#F0F0F2",font=("Arial",13))
        self.__fecha.grid(row=47,column=2,pady=18,rowspan=1)
        
        #CONSTRUIR LISTAS
    def construir(self,lista,marco):
        fila=5
        columna=0
        filAux=6
        columnAux=6
        opcs=self.__opcion
        style=ttk.Style()
        style.configure("BW.TLabel",foreground="#85BB65",background="#F0F0F2",font=("Arial",13))

        ttk.Label(marco,text="MONEDA",foreground="#fff",background="#85BB65",font=("Arial",13)).grid(row=3,column=0,**opcs,columnspan=2,rowspan=2)
        ttk.Label(marco,text="COMPRA",foreground="#fff",background="#85BB65",font=("Arial",13)).grid(row=3,column=5,**opcs,columnspan=2,rowspan=2)
        ttk.Label(marco,text="VENTA",foreground="#fff",background="#85BB65",font=("Arial",13)).grid(row=3,column=7,**opcs,columnspan=2,rowspan=2)

        for x in lista:
            nombre=x[0]
            self.__label[nombre]=[Label(marco,text=nombre[0:19],foreground="black",bg="#E4E8D1",font=("Arial",13)),
                                    ttk.Label(marco,text=x[1],style="BW.TLabel"),
                                    ttk.Label(marco,text=x[2],style="BW.TLabel")]#Se usa el diccionario para acceder a los labels en un futuro
            
            self.__label[nombre][0].grid(row=fila,column=columna,**opcs,columnspan=2,rowspan=2)
            self.__label[nombre][1].grid(row=filAux, column=columnAux, **opcs)
            self.__label[nombre][2].grid(row=filAux, column=columnAux+1, **opcs)

            #Para que esten uno debajo del otro
            filAux+=5
            fila+=5

    #Actualiza los labels de los precios del dolar y la fecha
    def actualizar(self,lista):
        for x in lista:
            nombre=x[0]
            self.__label[nombre][1].config(text=x[1])
            self.__label[nombre][2].config(text=x[2])

        fecha=self.getFecha()
        self.__fechaHora.set(fecha)


    #GETTERS
    def getFecha(self):
        return "{}".format(str(datetime.now())[0:19]) #Hasta 19 para no mostrar milesimas de segundos

    def getVentana(self):
        return self.__ventana

    def getButtonAct(self):
        return self.__botonActualizar