# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 08:33:27 2022

@author: artur

"""
import operator

#Función 1:
def cargar_canciones(archivo:str)->list:
    """ implementa una función que reciba como parámetro el nombre de un archivo que contiene la
    #información de canciones y la cargue en el programa bajo la forma de una lista de diccionarios."""
    l_d_canciones = []
    canciones = open(archivo,"r")
    line = canciones.readline()
    line = canciones.readline()
    while line != "":
        values = line.split(",")
        l_d_canciones.append({'posicion':int(values[0]),'nombre_cancion': values[1],'nombre_artista':values[2],'anio':int(values[3]),'letra':values[4]})
        line = canciones.readline()
    canciones.close()
    return l_d_canciones
#Funcion 2: 
def buscar_cancion(canciones:list,nombre_cancion:str,year:int)->dict:
    """implementa una función que reciba como parámetro la lista completa de canciones (diccionarios), el
    #nombre de una canción y el año del ranking al cual pertenece dicha canción y retorne un diccionario con toda la
    #información de dicha canción. En caso de que no se encuentre la canción, esta función debe retornar el valor
    #None."""
    song_info = None
    for i in range(len(canciones)):
       cancion=canciones[i]
       nombre = cancion['nombre_cancion']
       anio = cancion['anio']
       if nombre == nombre_cancion and anio == year:
           song_info = {'posicion':cancion['posicion'],'nombre_cancion':cancion['nombre_cancion'],
                             'nombre_artista':cancion['nombre_artista'],'anio':cancion['anio'],
                             'letra':cancion['letra']}
           break;
    return song_info
#Función 3: 
def canciones_anio(canciones:list,year:int)->list:
    """implementa una función que reciba por parámetro la lista completa de canciones (diccionarios) y un
    #año y retorne una nueva lista de diccionarios con la información de las canciones que pertenecen al año que
    #entra por parámetro. Cada diccionario debe guardar la información de una canción, exceptuando su letra. En
    #caso de que no haya ninguna canción en el año que se recibe por parámetro, la función debe retornar una lista
    #vacía"""
    l_c_anio=[]
    for i in range(len(canciones)):
        cancion=canciones[i]
        anio=cancion['anio']
        if anio==year:
            res=cancion.copy()
            del res['letra']
            l_c_anio.append(res)
            
    return l_c_anio
#Función 4:
def canciones_artista_periodo(canciones:list, n_artista:str, anio_i,anio_f:int)->list:
    """ implementa una función que reciba por parámetro la lista completa de canciones (diccionarios), el
    #nombre de un artista, un año inicial y un año final y retorne una nueva lista de diccionarios con la información
    #de las canciones del artista dado por parámetro en el periodo de tiempo definido por los parámetros año inicial
    #y año final. Cada diccionario debe guardar la información de una canción, exceptuando su letra. En caso de que
    #no haya ninguna canción del artista en ese periodo de tiempo, la función debe retornar una lista vacía."""
    artista_periodo=[]
    for i in range(len(canciones)):
        cancion = canciones[i]
        artista = cancion['nombre_artista']
        anio= cancion['anio']
        if artista==n_artista and anio>=anio_i and anio_f>=anio:
            res=cancion.copy()
            del res['letra']
            artista_periodo.append(res)
    return artista_periodo
#Función 5: 
def todas_canciones_artista(canciones:list, n_artista:str)->list:
    """implementa una función que reciba por parámetro la lista completa de canciones (diccionarios) y el
#nombre de un artista y retorne una nueva lista de diccionarios con la información de las canciones que
#pertenecen al artista que entra por parámetro. Cada diccionario debe guardar la información de una canción,
#exceptuando su letra. En caso de que no se encuentre el artista, la función debe retornar una lista vacía"""
    canciones_artista=[]
    for i in range(len(canciones)):
        cancion=canciones[i]
        nombre_artista=cancion['nombre_artista']
        if nombre_artista==n_artista:
            res=cancion['nombre_cancion']
            canciones_artista.append(res)
    return canciones_artista
#Función 6:
def todos_artistas_cancion(canciones:list,n_cancion:str)->list:
    """implementa una función que reciba por parámetro la lista completa de canciones (diccionarios) y el
   #nombre de una canción y retorne una lista de strings con los nombres de los artistas que han interpretado la
   #canción que entra por parámetro. En caso de que no se encuentre la canción, la función debe retornar una lista
   #vacía."""
    lista_artistas=[]
    for i in range(len(canciones)):
        artista=canciones[i]
        nombre_cancion=artista['nombre_cancion']
        if nombre_cancion==n_cancion:
            res=artista['nombre_artista']
            lista_artistas.append(res)
    return lista_artistas
            
#Función 7:
def artistas_mas_populares(canciones:list, num_canciones:int)->dict:
    """ implementa una función que reciba por parámetro la lista completa de canciones (diccionarios) y un
    #valor entero que determina una cantidad mínima de canciones y retorne un diccionario cuyas llaves son los
    #nombres de los artistas que han tenido un número total de canciones (a lo largo de todos los años) superior a la
    #cantidad recibida por parámetro y cuyos valores son la cantidad de canciones que ha tenido cada uno de los
    #artistas. Si un artista tiene la misma canción en 2 años diferentes esta se deberá contar dos veces. En caso de
    #que ningún artista haya tenido un número de canciones superior al valor recibido por parámetro, la función debe
    #retornar un diccionario vacío."""
    populares={}
    busqueda_artistas={}
    
    for i in range(len(canciones)):
        cancion=canciones[i]
        artista=cancion['nombre_artista'] 
        
        if artista in busqueda_artistas:
            busqueda_artistas[artista]+=1
        elif artista not in busqueda_artistas:
            busqueda_artistas[artista]=1
    for llave in busqueda_artistas:
        
        if int(busqueda_artistas[llave])>int(num_canciones):
               populares[llave]=busqueda_artistas[llave]
    artistas_populares=sorted(populares.items(), key=operator.itemgetter(1))#esta funcion, permite que la lista salga ordenada de manera ascendente, según la cantidad de canciones
    
    return artistas_populares
#Función 8:
def artista_estrella(canciones:list)->dict:
    """implementa una función que reciba por parámetro la lista completa de canciones (diccionarios) y
   #retorne un diccionario cuya llave es el nombre del artista que ha tenido el mayor número de canciones a lo largo
   #de todos los años en el Billboard y cuyo valor es la cantidad de canciones que ha tenido dicho artista. Si un artista
   #tiene la misma canción en 2 años diferentes esta se deberá contar dos veces. """
    busqueda_artistas={}
    max_canciones=0
    
    for i in range(len(canciones)):
        cancion=canciones[i]
        artista=cancion["nombre_artista"] 

        if artista in busqueda_artistas:
            busqueda_artistas[artista]+=1
        elif artista not in busqueda_artistas:
            busqueda_artistas[artista]=1

    for llave in busqueda_artistas:
        if busqueda_artistas[llave]>max_canciones:
               artistas_popular={}
               max_canciones = busqueda_artistas[llave]
               artistas_popular[llave]=busqueda_artistas[llave]
                    
    return artistas_popular
#Función 9:
def artistas_y_sus_canciones(canciones:list)->dict:
    """implementa una función que reciba por parámetro la lista completa de canciones (diccionarios) y
   #retorne un diccionario cuyas llaves son los nombres de los artistas y los valores son la lista de canciones de cada
   #artista. Si una canción de un artista aparece más de una vez en la lista de Billboard, esta se debe incluir una sola
   #vez en el diccionario de retorno."""
    canciones_artistas={}
    c_c={}
    for i in range(len(canciones)):
        cancion=canciones[i]
        c_artista=cancion['nombre_artista']
        a_cancion=cancion['nombre_cancion']
        if c_artista in canciones_artistas:
            c_c=canciones_artistas[c_artista]
            if a_cancion not in canciones_artistas:
               canciones_artistas[c_artista]=c_c
        elif c_artista not in canciones_artistas:
           canciones_artistas[c_artista]=a_cancion
    return canciones_artistas
   
   
   
   
   
#Función 10: implementa una función que reciba por parámetro la lista completa de canciones (diccionarios) y
#retorne la cantidad promedio de canciones que los artistas tienen en el listado de Billboard. Esto es:
#Canciones promedio por artista = cantidad total de canciones diferentes / cantidad de artistas diferentes
#Nota que, al calcular la cantidad total de artistas, hay que tener cuidado para que se cuente una sola vez cada
#artista diferente. Es decir que si un artista aparece varias veces, sólo debe contarse una vez. Así mismo, las
#canciones de un artista que aparecen más de una vez asociadas al artista, deben contarse una sola vez. 

def promedio_canciones_por_artista(canciones:list)->int:
    
    numero_artistas=len(artistas_y_sus_canciones(canciones))
    canciones_artistas={}
    for i in range(len(canciones)):
         cancion=canciones[i]
         artista=cancion['nombre_artista']
         numero_canciones=0
         lista_canciones_artista=[]
         for llave in range(len(canciones)):
             n_canciones=canciones[llave]
             n_artista=n_canciones['nombre_artista']
             if artista==n_artista and n_canciones['nombre_cancion'] not in lista_canciones_artista:
                 lista_canciones_artista.append(n_canciones['nombre_cancion'])
                 numero_canciones+=1
         canciones_artistas[artista]=numero_canciones
    total_canciones=sum(canciones_artistas.values())
    promedios_artistas=total_canciones/numero_artistas
    return promedios_artistas