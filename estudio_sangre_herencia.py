#-*-coding:utf-8-*-
try:
    from Tkinter import*
except:
    from tkinter import*

class BASE(): #ESTA ES LA CLASE BASE QUE USE PARA QUE HAGA TODO Y ASI HEREDAR LO DE ESRA CLASE PADRE A LAS HIJAS
    def __init__(self):
        self.titulo="ESTUDIOS SANGÍNEOS"    #FUNCION QUE HICE PARA PODER DARLE UN TITULO POR SEPARADO A CADA ESTUDIO

    def pedir_datos(self): #FUNCION PARA PEDIR LOS DATOS QUE EL USUARIO METERÁ
        self._mglucosa = DoubleVar()
        self._macido = DoubleVar()
        self._mcolesterol = DoubleVar()         
        self._murea = DoubleVar()
        self._mtri = DoubleVar()
        self._mcrea = DoubleVar()           #HASTA AQUI HAGO LA DECLARACION DE MIS VARIABLES QUE UTILIZARE PARA REALIZAR LA CONVERSION DE TIPO DOUBLE
        self.ventana = Toplevel(ventana)    #REALIZO UNA INSTANCIA LLAMADA VENTANA 
        self.ventana.title(self.titulo)     #CON LA VENTANA HAGO EL TITULO DE LA VENTANA  
        self.ventana.geometry("800x600")   #ASIGNO EL TAMAÑO DE LA VENTANA DONDE SE VERA EL PROGRAMA

        Label(self.ventana, text = "ESTUDIOS SANGUINEOS", font = ("Arial", 24), fg = "red").place(x=200, y = 50) 
        # ES EL TITULO QUE SE VERA COMO SANGRIA DE NUESTRA VENTANA EN LA PARTE DE ARRIBA
        
        Label(self.ventana, text = "Indica la glucosa en mmol/L", font = ("Arial", 10), fg = "blue").place(x=100, y = 150)
        Entry(self.ventana, textvariable = self._mglucosa, font = ("Arial", 10)).place(x=550, y =150)
        Label(self.ventana, text = "Indica el ácido urico en mmol/L", font = ("Arial", 10), fg = "blue").place(x=100, y = 170)
        Entry(self.ventana, textvariable = self._macido, font = ("Arial", 10)).place(x=550, y =170)
        Label(self.ventana, text = "Indica el colesterol en mmol/L", font = ("Arial", 10), fg = "blue").place(x=100, y = 190)
        Entry(self.ventana, textvariable = self._mcolesterol, font = ("Arial", 10)).place(x=550, y =190)
        Label(self.ventana, text = "Indica la urea en mmol/L", font = ("Arial", 10), fg = "blue").place(x=100, y = 210)
        Entry(self.ventana, textvariable = self._murea, font = ("Arial", 10)).place(x=550, y =210)
        Label(self.ventana, text = "Indica los Trigliceridos en mmol/L", font = ("Arial", 10), fg = "blue").place(x=100, y = 230)
        Entry(self.ventana, textvariable = self._mtri, font = ("Arial", 10)).place(x=550, y =230)
        Label(self.ventana, text = "Indica la creatinina en mmol/L", font = ("Arial", 10), fg = "blue").place(x=100, y = 250)
        Entry(self.ventana, textvariable = self._mcrea, font = ("Arial", 10)).place(x=550, y =250)
        # EN EL BLOQUE DE CODIGO ANTERIOR LO QUE VOY HACIENDO ES PRIMERO PONER UN LABEL PARA QUE EL USUARIO SEPA LO QUE SE LE ESTA PIDIENDO, CADA LABEL, ES UN 
        # REQUERIMIENTO DIFERENTE PARA EL CALCULO DEL ESTUDIO SANGUINEO QUE SE HAYA INDICADO.
        # CADA ENTRY LO USO PARA GUARDAR EL RESULTADO DE LO QUE PONGA EL USUARIO EN LA VARIABLE QUE LE CORRESPONDA A LO QUE SE PIDIO.
        # LO DEMAS ESCRITO DE FONT, FG O PLACE ES PARA DARLE FORMA, COLOR Y SE COLOQUE EN LA POSICION ADECUADO DE ACUERDO A LOS EJES DE LAS X y Y.

        Button(self.ventana, text = "Calcular", font = ("Arial", 14), width = 15, height = 2, fg = "blue", command = self.calcular_estudio).place(x=550, y = 300)
        # AGREGUE UN BOTON PARA CALCULAR, QUE LO VINVULO CON LA FUNCION CALCULAR_ESTUDIO PARA QUE HAGA TODOS LOS CALCULOS NECESARIOS

class sanguineo3 (BASE): # PRIMER CLASE HIJA QUE HEREDA DE LA CLASE PADRE
    def __init__(self, titulo):         # EN ESTA FUNCION PRINCIPAL VUELVO A DECLARAR LAS VARIABLES QUE UTILIZARE PARA ESTA CLASE DE ESTUDIO3
        self.titulo=titulo
        self._mglucosa = DoubleVar()       # LAS TENGO QUE VOLVER A DECLARAR DOUBLE VAR COMO EN UN PRINCIPIO PARA QUE ACTUEN COMO DEBE SER
        self._macido = DoubleVar()
        self._mcolesterol = DoubleVar()

    def calcular_estudio(self):     # EN ESTA OTRA FUNCION ES DONDE HARE LOS CALCULOS PARA SU CONVERSION 

        Label(self.ventana, text = "Tu cantidad en mg/dL de Glucosa es de: ", font = ("Arial", 13), fg = "blue").place(x=100, y = 410)
        Label(self.ventana, text = str( self._mglucosa.get() * 18.02), font = ("Arial", 13), fg = "blue").place(x=450, y = 410)

        Label(self.ventana, text = "Tu cantidad en mg/dL de Acido Urico es de: ", font = ("Arial", 13), fg = "blue").place(x=100, y = 430)
        Label(self.ventana, text = str( self._macido.get() * 0.02), font = ("Arial", 13), fg = "blue").place(x=450, y = 430)

        Label(self.ventana, text = "Tu cantiad en mg/dL de Colesterol es de: ", font = ("Arial", 13), fg = "blue").place(x=100, y = 450)
        Label(self.ventana, text = str( self._mcolesterol.get() * 380.66), font = ("Arial", 13), fg = "blue").place(x=450, y = 450)
        # EN EL BLOQUE DE CODIGO ANTERIOR LO HAGO PARA ESCRIBIR LOS RESULTADOS YA CONEVRTIDOS.
        # PRIMERO PONGPO QUE "LA CANTIDAD DE GLUCOSA ES:" PARA QUE EL USUARIO SEPA CUANTO TIENE EN SU CONVERSION A mg/dL
        # CON EL 2DO LABEL LO QUE HAGO ES EL CALCULO DE LA MEDIDA INGRESADA POR SU CANTIDAD DE ACUERDO A LA CONVERSION DE LO QUE VALE CADA MEDIDA POR SI SOLA
        # LO DEMAS ESCRITO DE FONT, FG O PLACE ES PARA DARLE FORMA, COLOR Y SE COLOQUE EN LA POSICION ADECUADO DE ACUERDO A LOS EJES DE LAS X y Y.

class sanguineo6 (BASE):    #SEGUNDA CLASE HIJA QUE HEREDA DE LA CLASE PADRE LLAMADA BASE
    def __init__(self, titulo):     # EN ESTA FUNCION PRINCIPAL VUELVO A DECLARAR LAS VARIABLES QUE UTILIZARE PARA ESTA CLASE DE ESTUDIO6
        self.titulo=titulo
        self._mglucosa = DoubleVar()        
        self._macido = DoubleVar()
        self._mcolesterol = DoubleVar() # LAS TENGO QUE VOLVER A DECLARAR DOUBLE VAR COMO EN UN PRINCIPIO PARA QUE ACTUEN COMO DEBE SER
        self._murea = DoubleVar()
        self._mtri = DoubleVar()        # A DIFERENCIA DE LA OTRA CLASE HIJA, AHORA SI PUSE TODAS LAS VARIABLES PORQUE EN ESTE CASO SI USARE TODAS
        self._mcrea = DoubleVar()
        
    def calcular_estudio(self): # EN ESTA OTRA FUNCION ES DONDE HARE LOS CALCULOS PARA SU CONVERSION 

        Label(self.ventana, text = "Tu cantidad en mg/dL de Glucosa es de: ", font = ("Arial", 13), fg = "blue").place(x=100, y = 410)
        Label(self.ventana, text = str( self._mglucosa.get() * 18.02), font = ("Arial", 13), fg = "blue").place(x=445, y = 410)

        Label(self.ventana, text = "Tu cantidad en mg/dL de Acido Urico es de: ", font = ("Arial", 13), fg = "blue").place(x=100, y = 430)
        Label(self.ventana, text = str( self._macido.get() * 0.02), font = ("Arial", 13), fg = "blue").place(x=445, y = 430)

        Label(self.ventana, text = "Tu cantiad en mg/dL de Colesterol es de: ", font = ("Arial", 13), fg = "blue").place(x=100, y = 450)
        Label(self.ventana, text = str( self._mcolesterol.get() * 380.66), font = ("Arial", 13), fg = "blue").place(x=445, y = 450)

        Label(self.ventana, text = "Tu cantidad en mg/dL de Urea es de: ", font = ("Arial", 13), fg = "blue").place(x=100, y = 470)
        Label(self.ventana, text = str( self._murea.get() * 6.01), font = ("Arial", 13), fg = "blue").place(x=445, y = 470)

        Label(self.ventana, text = "Tu cantiad en mg/dL de Trigliceridos es de: ", font = ("Arial", 13), fg = "blue").place(x=100, y = 490)
        Label(self.ventana, text = str( self._mtri.get() * 87.5), font = ("Arial", 13), fg = "blue").place(x=445, y = 490)

        Label(self.ventana, text = "Tu cantidad en mg/dL de Creatinina es de: ", font = ("Arial", 13), fg = "blue").place(x=100, y = 510)
        Label(self.ventana, text = str( self._mcrea.get() * 0.01), font = ("Arial", 13), fg = "blue").place(x=445, y = 510)
        # EN EL BLOQUE DE CODIGO ANTERIOR LO HAGO PARA ESCRIBIR LOS RESULTADOS YA CONEVRTIDOS.
        # PRIMERO PONGPO QUE "LA CANTIDAD DE GLUCOSA ES:" PARA QUE EL USUARIO SEPA CUANTO TIENE EN SU CONVERSION A mg/dL, ESTO CON CADA MEDIDA PARA CONVERTIRLAS
        # CON EL 2DO LABEL LO QUE HAGO ES EL CALCULO DE LA MEDIDA INGRESADA POR SU CANTIDAD DE ACUERDO A LA CONVERSION DE LO QUE VALE CADA MEDIDA POR SI SOLA
        # LO DEMAS ESCRITO DE FONT, FG O PLACE ES PARA DARLE FORMA, COLOR Y SE COLOQUE EN LA POSICION ADECUADO DE ACUERDO A LOS EJES DE LAS X y Y.

def cerrar():   #ESTA FUNCION LA TENGO PARA CUANDO LA MANDE LLAMAR CON LOS BOTONES SE CIERRE EL PROGRAMA POR COMPLETO
    ventana.destroy() # ESTO ES LO QUE HACE QUE SE DESTRUYA LA VENTANA 


ventana = Tk() # Creando una instancia
ventana.title("Estudios de sangre avanzados") # LE PONGO TITULO A LA VENTANA SECUNDARIA
ventana.geometry("700x420") # LE ASIGNO EL TAMAÑO A LA VENTANA
ventana.resizable(1,1) # ESTO ES PARA QUE PUEDA HACER DINAMICA LA VENTANA

sangre = sanguineo3("ESTUDIO SANGUINEO 3") # CREO LA INSTANCIA PARA EL ESTUDIO SANGUINEO 3
quimico = sanguineo6("ESTUDIO SANGUINEO 6") # CREO LA INSTANCIA PARA EL ESTUDIO SANGUINEO 6

ventana.configure(bg="pink") # PARA DARLE COLOR A LA VENTANA PRINCIPAL
Label (ventana, text = "Laboratorio de Análisis Clínicos DM", font = ("Arial", 24), fg="red", bg="yellow").place(x=100, y=50) 
# TEXTO PARA PONERLE DE TTITULO EL NOMBRE DEL LABORATORIO

Button (ventana, text = "Química Sanguínea 3", font =("Arial", 16), width = 20, height = 2, fg ="black", bg= "purple", command = sangre.pedir_datos).place(x = 100, y = 150)
Button (ventana, text = "Química Sanguínea 6", font =("Arial", 16), width = 20, height = 2, fg ="black", bg= "purple", command = quimico.pedir_datos).place(x = 100, y = 250)
Button (ventana, text = "CERRAR", font =("Arial", 16), width = 20, height = 2, fg ="red", bg= "purple", command = cerrar).place(x = 400, y = 200)
# LOS 3 DE ARRIBA SON BOTONES PARA QUE SE DIRIJA AL APARTADO DESEADO DE ACUERDO AL ESTUDIO QUE DESEA INGRESAR
# EL 3ER BOTON ES PARA QUE CIERRE POR COMPLETO EL PROGRAMA

mainloop() # SE REQUIERE PARA QUE FUNCIONE CORRECTAMENTE EL PROGRAMA Y VEA EN VENTANA