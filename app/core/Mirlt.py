#!/usr/bin/env /home/comcopco/virtualenv/ptr8/3.6/bin/python3
# -*- coding: utf-8 -*-

#import logCMP
#import render
#! /home/comcopco/virtualenv/plex/3.6/bin/python3
#comcop 2020
#import nanositios
import os, sys
from datetime import datetime
import mysql.connector
#from bottle import template, route
import time
from dotenv import load_dotenv
import logging

# Configuración básica
logging.basicConfig(
    filename='app.log',  # Nombre del archivo donde se guardarán los logs
    level=logging.INFO,  # Nivel de registro (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato de los mensajes
)

load_dotenv()  # Cargar variables desde el archivo .env

class Globales(object):
        def __init__(self ,llave="", *args, **kwargs):
                super(Globales, self).__init__(*args, **kwargs)
                self.PI = 3.14159265358979323846
                self.TMP = "i4533r4264i3445s7656"
                self.CLAVE= llave
                #Aceleracion debida a la atracción terrestre - g
                self.G=9.80665 # m.sec-2
                #Carga elemental - e
                self.e=1.60219 * -19# C
                #Constante de Avogadro - NA
                self.NA=6.02217 * 1023# mol-1
                #Constante de Boltzmann - k
                self.k=1.38062 * 1023 #J.K-1
                #Constante de Faraday - F
                self.Faraday=9.64867 * 104# C.mol-1
                #Constante de los gases ideales - R
                self.Gas=8.31434# J.mol-1.K-1
                #Constante de gravitación universal - G
                self.G=6.6732 * -11# N.m2.kg-2
                #Constante de Planck - h
                self.h=6.6262 * -34# J.sec
                #Permitividad del vacío - ε0
                self.E=8.85419 * -12# C.v-1.m-1
                #Equivalente mecánico del calor - j
                self.J=4.184# j.calc-1
                #Masa del electrón en reposo - me
                self.me=9.10956 * -31# kg
                #Masa del neutrón en reposo - mn
                self.N=1.67492 * -27# kg
                #Masa del protón en reposo - mp
                self.P=1.67261 * -27# kg
                #Punto de congelación del agua a 1 atm - T0
                self.FRIO=273.15# K
                #Velocidad de la luz - c
                self.C=2.99793 * 108 #m.s-1
                #Volumen molar de un gas ideal a TPN - Vm
                self. V=22.4136 #L.mol-1
                #load_dotenv()  # Cargar variables desde el archivo .env
                self.DB_DRIVER=  os.getenv('DB_DRIVER')
                self.DB_HOST= os.getenv('DB_HOST')
                self.DB_USER =os.getenv('DB_USER')
                self.DB_PASS=os.getenv('DB_PASS')
                self.DB_DATA=os.getenv('DB_DATA')
                self.DB_PORT=os.getenv('DB_PORT')
                self.DB_PREFIX=os.getenv('DB_PREFIX')

class Basicas(Globales):
 def suma(*args):
     value = 0
     for n in args:
         value += n
     return value

#usabilidad: x= Literaria(resumen="sobre un dinosaurio";p="3+2", r="5", tipo="cuento")
#            x.arquitectura() -> "IND"
class Literaria(Globales):
        def __init__(self, resumen="",tipo="",r="",p="", *args, **kwargs):
                super(Literaria, self).__init__(*args, **kwargs)
                self.resumen=resumen
                self.p=p
                self.r=r
                self.tipo=tipo
        def arquitectura(self):
                sw=1
                if self.tipo=="Cuento":
                     sw=0
                     return "['Estructura':{CMPX:{I:CMPI,N:CMPN,D:CMPD}}]" #Inicio , nudo , desenlace
                if self.tipo== "adivinanza":
                     sw=0
                     return "['Estructura':{CMPX:{I=CMPI,D=CMPD},CMPY:{N:CMPN}}]"
                if self.tipo=="Estante":
                     sw=0
                     return "[Estructura:{CMPX={B=CMPB,E=CMPE,P=CMPP,C=CMPC}}]" #Banner, estante, promociones, carrito
                if sw==1:
                     return "['Estructura':{CMPX:CMPnull}]"

class prueba( Literaria):
        def __init__(self, criterio, filtro, organizacion, tokens, *args, **kwargs):
                super(prueba, self).__init__(*args, **kwargs)
                self.organizacion=organizacion
                self.criterio=criterio
                self.tokens=tokens
                self.filtro=filtro
        def imprimirmsj(self):
                salida=""
                salida=salida+"Hola mundo"+str(self.criterio)
                #os.system("echo "+ salida +">>~/public_html/orcat/"+self.TMP+"/v.css.cmp")
        def logicasimple ():
                5==5
        def filosofia():
                0==0

class Poligono(Literaria):
    """
    Define un polígono según su base y su altura.
    """
    def __init__(self, b, h ,nombre , *args, **kwargs):
        super(Poligono, self).__init__(*args, **kwargs)
        self.b=b
        self.h=h
        self.nombre=nombre

class COMCOP(Poligono, prueba):
    def __init__(self , *args, **kwargs):
       super(COMCOP,self).__init__( *args, **kwargs)
    def base(self):
       bandera=1
       #os.system("echo '["+  self.criterio +":{"+str(self.filtro)+":"+str(self.tokens)+"-"+self.organizacion+"}]'>>logURL")
       return '['+  self.criterio +':{'+str(self.filtro)+':'+str(self.tokens)+self.organizacion+'}]'

class acertijo(Literaria):
    def __init__(self , *args, **kwargs):
       super(acertijo,self).__init__( *args, **kwargs)
    def resolver(self):
       #Verificar si nombre existe en base de destos "NombreExiste"
       #Si nombre existe en bd y passwordR == passwordL retorne rango
       #os.system("echo 'p:"+self.p+" r:"+self.r+"'>>logMIRLT")
       if self.p=="Carlos" and self.r=="lallyxo92":
        return 4
       if self.p=="Carlos" and self.r=="y":
        return 2
       if self.p=="" and self.r=="":
        return 1
       return 0

class DB(acertijo):
    def __init__(self ,query,username, *args, **kwargs):
        super(DB,self).__init__( *args, **kwargs)
        self.query=query
        self.username=username

    def run_query(self, query=None, username=""):
        if query is None:
           query=self.query
        logging.info(f'query desde run_query@Mirlt: {query}')
        #os.system(('echo "CMP2" >> PgenesisMirlt').replace("CMP2",query))
        datos = [self.DB_HOST, self.DB_USER, self.DB_PASS, self.DB_DATA]
        #os.system("echo 'CMP' >> /home/comcopco/public_html/Arg/logCMP/PgenesisMirlt".replace("CMP",""))
        conn = mysql.connector.connect(host=self.DB_HOST, user=self.DB_USER, password=self.DB_PASS, database=self.DB_DATA)# Conectar a la base de datos 
        #os.system("echo 'Bases de datos: "+str(query)+"'>>logMIRLT")
        cursor = conn.cursor()         # Crear un cursor
        cursor.execute(query)          # Ejecutar una consulta
        #os.system(('echo "CMP2" >> /home/comcopco/public_html/Arg/logCMP/PgenesisMirlt').replace("CMP2",query).replace("`","\""))
        if query.upper().startswith('SELECT'):
            data = cursor.fetchall()   # Traer los resultados de un select
        else:
            conn.commit()              # Hacer efectiva la escritura de datos
            data = None
        cursor.close()                 # Cerrar el cursor
        conn.close()
        del conn
        #print(" Cerrar la conexión")
        return data

    def obtenerUE(self):
        query = f'SELECT * FROM occb_user WHERE user_id = "{self.username}"'
        logging.info(f"query desde obtenerUE@Mirlt:{query}")
        # Ejecutar la consulta y obtener los datos del usuario
        user = self.run_query(query=query)
        empresa = ""  # Inicializamos la variable empresa
        if user:
            # Si se encuentra al menos un usuario, logueamos la consulta
            logging.info(f"Ejecutando consulta para obtener datos de la empresa para el user_id: desde obtenerUE@Mirlt:{user[0][0]}")
            # Consulta para obtener la empresa asociada al usuario
            query_empresa = f'SELECT * FROM occb_empresa WHERE client_id= "{user[0][1]}"'
            empresa = self.run_query(query=query_empresa)
            # Si se encuentra la empresa, logueamos el resultado
            if empresa:
                logging.info(f"Datos de la empresa encontrados:desde obtenerUE@Mirlt: {empresa}")
            else:
                logging.warning(f"No se encontró la empresa asociada al usuario desde obtenerUE@Mirlt:{self.username}")

            return user, empresa
        else:
            # Si no se encuentra el usuario, retornamos el vector antibug
            return [[str(len("Hola")), "", "", "", "", "", "", "", ""]], ""

def hoy():
 now = datetime.now() # current date and time
 year = now.strftime("%Y")
 #print("year:", year);
 month = now.strftime("%m")
 #print("month:", month);
 day = now.strftime("%d")
 #print("day:", day);
 time = now.strftime("%H:%M:%S")
 #print("time:", time)
 date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
 return ("date and time: "+date_time)


	

def Inicializador(response="", filtro="", tokens="", menu="",pag=""):
	#organizacion ha sido renombrado menu 
	#logCMP.mk("desde Mirlt1-->", " response=" +response+" filtro="+filtro +" tokens="+tokens +" menu="+menu )
	tokens=str(tokens)
	y="'"+filtro.replace("CMP2PASS","','")+"'"
	z=eval(y)

	plano=menu[0:4]
	user=[("","")]
	mensaje="bebe00003 "
	#logCMP.mk("desde Mirlt2-->", " response " +response+ " user "+ " plano "+plano+ " tokens "+tokens+" mensaje "+mensaje+" menu[5] "+menu[4])
	#return [tokens, user, plano, actual, mensaje, menu[5]]
	if response =="f04":
		#logCMP.mk("\tf4=Comprobar usuario y generar sesion:", "" )
		consulta=DB(query="SELECT `user_group_id` FROM `occb_user` WHERE username ='"+z[0]+"' and password='"+z[1]+"'")
		#print("Se va a crear token para "+"SELECT `user_group_id` FROM `occb_user` WHERE username ='carlos' and 
		#logCMP.mk("\t+2:", "" )
		session=[("","")]
		tokens2=consulta.run_query()
		#logCMP.mk("\t+3:", "" )
		consulta=DB(query="SELECT `user_id`,`user_group_id`,`username`,`password`,`salt`,`firstname`,`lastname`,`email`,`image`,`code`,`ip`,`status`,`date_added`  FROM `occb_user` WHERE username ='"+z[0]+"' and password='"+z[1]+"'")
		#consulta2=DB(query="")
		#logCMP.mk("\t+4:", "" )
		user=consulta.run_query()
		if len(user)<1:
			user=[("","1","CMPInvitado")]
		else: 
			consulta2=DB(query="")
			sesion=consulta2.run_query()
		#print(user)
		#logCMP.mk("\t+6:", "" )
		if len(str(tokens2))<3:
			tokens="1"
			#logCMP.mk("\t+8:", "" )
		else:
			tokens=(str(tokens2))[2]
		try:
			pass#logCMP.mk("\tComprobado-->",str(len(user[0])))
		except:
			pass#logCMP.mk("\tComprobado-->","Error de autenticación")
		#render.render(session[0][0], user)
		user="CMPSECUREF=$Ac"
		session=""
'''
        if response=="rm":
                time.sleep(0.05)
                os.system("rm ../public_html/clicar/index.php")
                os.system("cp ../public_html/clicar/login.php ../public_html/clicar/index.php")
                return ["Se ha generado un nuevo portal"]
                user=[("","","")]
        else:  
		if "f4" in response or "CMPS" in response or "f9" in response or "f01" in response or "f03" in response or "f04" in response :
			#y="'"+organizacion.replace("CMPPASS","','")+"'"
			#z=eval(y)
			consulta=DB(query="SELECT `user_id`,`user_group_id`,`username`,`password`,`salt`,`firstname`,`lastname`,`email`,`image`,`code`,`ip`,`status`,`date_added`,`saldo`,`pesos` FROM  `occb_user` WHERE username ='"+z[0]+"' and password='"+z[1]+"'")
			user=consulta.run_query()

			if len((user))<4:
				tokens="1"
			else:
				tokens=user[0][1]
			if "f9" in response:
				True
				#print(nanositios.Excel2array())
			#if "f03" in response :
			#	mensaje=nanositios.modSaldo(response[3:], user[0])
			#if "f04" in response:
			#	mensaje=nanositios.aggsaldo(user[0])
		
		if "f3" in response:
			#?f3cail@mail.comCMPT300987887CMPtYarumal&pepeCMPPASSjunior$65567&5
			mail=response[2:int(response.index("CMPT"))]
			tel=response[(response.find("CMPT"))+4:(response.find("CMPt"))]
			ub=response[int(response.index("CMPt")+4):]
			y="'"+organizacion.replace("CMPPASS","','")+"'"
			z=eval(y)
			if len(Mirlt.DB("SELECT * FROM `occb_user` WHERE `username` LIKE '"+z[0]+"'   AND `salt` LIKE '3f2b4445'").run_query())==0:
				if len(Mirlt.DB("SELECT * FROM `occb_user` WHERE `email` LIKE '"+mail+"'  AND `salt` LIKE '3f2b4445'").run_query())==0:
					os.system("cout '"+mail+tel+ub+z[0]+z[1]+"'>>logCMP")
					insertar=DB("INSERT INTO `occb_user` (`user_id`, `user_group_id`, `username`, `password`, `salt`,`firstname`,`lastname`, `email`, `image`, `code`, `ip`, `status`, `date_added`) VALUES (NULL, '2', '"+z[0]+"', '"+z[1]+"', '3f2b4445', '', '', '"+mail+"', '', '', '"+ub+tel+"', '1', '"+datetime.now().isoformat(timespec='minutes').replace("T"," ") +"')")
					insertar.run_query()
					mensaje="okok00000 Exitoso"
				else:
					mensaje="usex00001"# Correo electrónico existe"
			else:
				mensaje="emax00002"# usuario existe"
			#print(mensaje)
			tokens="1"
			user=[("","","")]

		#if "f8" in response:
			#crea sitio
			#l mapa de la pagina està entre CMPA y una P
			#plano=response[response.index("B"):response.index("D")]
			#tokens ="1"
	 #print("resumen=sobre un dinosaurio, tokens->"+str(tokens))

	respuesta = COMCOP(b=2,h=6,criterio=""+response, filtro=filtro, tokens=tokens,organizacion=organizacion, nombre=815, resumen = [{0.0},{6,7},{9,9}])
	#print("=====================Retorno de Mirlt=========================")
	print(tokens)
	#print(respuesta.base())
	#print(user)
	print(plano)
	print("A partir de ")
	print(response)
	print(filtro)
	print(organizacion)
	#return [tokens,respuesta.base(), user, plano, actual, mensaje]
'''
#Inicializador(response="hola",filtro="4",tokens="2",organizacion="si")
