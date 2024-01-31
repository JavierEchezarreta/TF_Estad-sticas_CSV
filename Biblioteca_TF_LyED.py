import csv 

with open('snic-provincias.csv', encoding='utf-8', newline='') as archivo:
        datos = csv.reader(archivo, delimiter = ',')

def crear_lista_lineas (datos):
    with open('snic-provincias.csv', encoding='utf-8', newline='') as archivo:
        datos = csv.reader(archivo, delimiter = ',')
        'Crea una lista de lineas donde los valores numéricos son convertidos de Str a Integer y los valores faltantes son asignados con cero'
        lista_lineas = []
        for x in datos:
            lista_lineas.append(x)
        for x in lista_lineas[1:]:
            if x[6] == '':
                x[6] = 0
            if x[5] == '':
                x[5] = 0
            if x[0] == '':
                x[0] = 0
            if x[1] == '':
                x[1] = 0   
            if x[3] == '':
                x[3] = 0         
            x[0] = int(x[0])
            x[1] = int(x[1])
            x[3] = int(x[3])
            x[5] = int(x[5])
            x[6] = int(x[6])
    return lista_lineas

def filtrar_provincia (nombre_provincia):
    'Toma como argumento nombre de provincia y devuelve una lista con las lineas que involucran dicha provincia'
    lineas_provincia = []
    lista_lineas = crear_lista_lineas(datos)
    for x in lista_lineas:
        if nombre_provincia in x:
            lineas_provincia.append(x)
    return lineas_provincia

# print (filtrar_provincia('Chaco'))
# print (filtrar_provincia('Salta'))

def delitos_totales_por_provincia (nombre_provincia):
    'Toma como argumento el nombre de la provincia y devuelve una diccionario con todos los delitos y su cantidad de hechos/víctimas'
    delitos_totales = {}
    provincia = filtrar_provincia(nombre_provincia)
    for x in provincia:
        if x[4] not in delitos_totales:
            delitos_totales[x[4]] = [x[5], x[6]]
        else:
            valores = delitos_totales.get(x[4])
            cantidad_hechos = valores[0] + x[5]
            cantidad_victimas = valores[1] + x[6]
            delitos_totales[x[4]] = [cantidad_hechos, cantidad_victimas]
    return delitos_totales

#print (delitos_totales_por_provincia('Chaco'))

def top5_delitos (nombre_provincia):
    'Toma como argumento el nombre de la provincia y devuelve una diccionario con un top 5 de delitos por provincia'
    top5_delitos_lista = {}
    delitos_totales = delitos_totales_por_provincia(nombre_provincia)
    for x in range (5): 
        delito_mas_comun = max(delitos_totales, key= delitos_totales.get)
        top5_delitos_lista[delito_mas_comun] = delitos_totales[delito_mas_comun]
        del delitos_totales[delito_mas_comun]
    delitos_totales = delitos_totales_por_provincia(nombre_provincia)
    return top5_delitos_lista

# print (top5_delitos('Ciudad Autónoma de Buenos Aires'))


def filtrar_anio (anio):

    'Toma como argumento el año y devuelve una lista con las lineas que involucran dicho año'
    lineas_por_anio = []
    lista_lineas = crear_lista_lineas(datos)
    for x in lista_lineas:
        if anio == x[0]:
            lineas_por_anio.append(x)
    return lineas_por_anio

#print(filtrar_anio(2014))

def total_delitos_por_provincia (anio):
    'Toma como argumento el año y devuelve un diccionario con los delitos totales de cada provincia'
    lineas_por_anio = filtrar_anio(anio) 
    total_delitos_provincia = {}
    for x in lineas_por_anio:
        if x[2] not in total_delitos_provincia:
            total_delitos_provincia[x[2]] = x[5], x[6]
        else:
            valores = total_delitos_provincia.get(x[2])
            cantidad_hechos = int(valores[0]) + int(x[5])
            cantidad_victimas = int(valores[1]) + int(x[6])
            total_delitos_provincia[x[2]] = [cantidad_hechos, cantidad_victimas]

    return total_delitos_provincia

#print(total_delitos_por_provincia(2014))

def top5_provincias_delictivas (anio):
    'Toma como argumento el año y devuelve un diccionario con un top de 5 provincia con cantidad de hechos y cantidad de víctimas'
    total_delitos = total_delitos_por_provincia(anio)
    top5_provincias_delictivas = {}
    for x in range (5): 
        provincia_mas_comun = max(total_delitos, key= total_delitos.get)
        top5_provincias_delictivas[provincia_mas_comun] = total_delitos[provincia_mas_comun]
        del total_delitos[provincia_mas_comun]
    return top5_provincias_delictivas

#print(top5_provincias_delictivas(2014))


def top10_delitos_comunes_por_anio (anio):
    'Toma como argumento el año y devuelve un diccionario con un top 10 de delitos a nivel nacional con cantidad de hechos y cantidad de víctimas'
    delitos_anio = filtrar_anio(anio)
    total_delitos = {}
    top10_delitos_comunes = {}
    for x in delitos_anio:
        if x[4] not in total_delitos:
            total_delitos[x[4]] = x[5], x[6]
        else:
            valores = total_delitos.get(x[4])
            cantidad_hechos = int(valores[0]) + int(x[5])
            cantidad_victimas = int(valores[1]) + int(x[6])
            total_delitos[x[4]] = [cantidad_hechos, cantidad_victimas]
    for x in range (10):
        delito_mas_comun = max(total_delitos, key= total_delitos.get)
        top10_delitos_comunes[delito_mas_comun] = total_delitos[delito_mas_comun]
        del total_delitos[delito_mas_comun]

    return top10_delitos_comunes

#print (top10_delitos_comunes_por_anio(2014))

def top10_historico_provincias_delictivas ():
    'Devuelve un diccionario con un top 10 historico de provincias mas delictivas con cantidad de hechos y cantidad de víctimas'
    lista_lineas = crear_lista_lineas (datos)
    total_delitos_provincia = {}
    top5_historico_provincias = {}
    for x in lista_lineas[1:]:
        if x[2] not in total_delitos_provincia:
            total_delitos_provincia[x[2]] = x[5], x[6]
        else:
            valores = total_delitos_provincia.get(x[2])
            cantidad_hechos = valores[0] + x[5]
            cantidad_victimas = valores[1] + x[6]
            total_delitos_provincia[x[2]] = [cantidad_hechos, cantidad_victimas]
    for x in range (10):
        provincias_mas_delictiva = max(total_delitos_provincia, key= total_delitos_provincia.get)
        top5_historico_provincias[provincias_mas_delictiva] = total_delitos_provincia[provincias_mas_delictiva]
        del total_delitos_provincia[provincias_mas_delictiva]

    return top5_historico_provincias

#print (top5_historico_provincias_delictivas())

def top10_historico_delitos_comunes ():
    'Devuelve un diccionario con un top 10 historico de delitos más comunes con cantidad de hechos y cantidad de víctimas'
    lista_lineas = crear_lista_lineas(datos)
    total_delitos = {}
    top10_historico_delitos = {}
    for x in lista_lineas[1:]:
        if x[4] not in total_delitos:
            total_delitos[x[4]] = x[5], x[6]
        else:
            valores = total_delitos.get(x[4])
            cantidad_hechos = valores[0] + x[5]
            cantidad_victimas = valores[1] + x[6]
            total_delitos[x[4]] = [cantidad_hechos, cantidad_victimas]
    for x in range (10):
        delito_mas_comun = max(total_delitos, key= total_delitos.get)
        top10_historico_delitos[delito_mas_comun] = total_delitos[delito_mas_comun]
        del total_delitos[delito_mas_comun]
    return top10_historico_delitos

#print (top10_historico_delitos_comunes())

def filtrar_delito_total (delito):
    'Toma como argumento el nombre del delito y devuelve un diccionario con la cantidad total de hechos, por año y por provincia'
    cantidad_hechos_totales = {}
    lista_lineas = crear_lista_lineas(datos)
    resultado = {}
    for x in lista_lineas[1:]:
        if delito == x[4]:
            if x[4] in cantidad_hechos_totales:
                valor = cantidad_hechos_totales.get(x[4])
                cantidad_hechos_totales[x[4]] = valor + x[5]
            else:
                cantidad_hechos_totales[x[4]] = x[5]
    return cantidad_hechos_totales

#print(filtrar_delito_total('Homicidios dolosos'))

def filtrar_delito_anio (delito):
    lista_lineas = crear_lista_lineas(datos)
    cantidad_hechos_por_anio = {}
    resultado = {}
    for x in lista_lineas[1:]:
        if delito == x[4]:
            if x[0] in cantidad_hechos_por_anio:
                valor = cantidad_hechos_por_anio.get(x[0])
                cantidad_hechos_por_anio[x[0]] = valor + x[5]
            else:
                cantidad_hechos_por_anio[x[0]] = x[5]
    anio_mas_comun = max(cantidad_hechos_por_anio, key= cantidad_hechos_por_anio.get)
    resultado[anio_mas_comun] = cantidad_hechos_por_anio[anio_mas_comun]
    return resultado

#print(filtrar_delito_anio('Homicidios dolosos'))

def filtrar_delito_provincia (delito):
    lista_lineas = crear_lista_lineas(datos)
    cantidad_hechos_por_provincia = {}
    resultado = {}
    for x in lista_lineas[1:]:
        if delito == x[4]:
            if x[2] in cantidad_hechos_por_provincia:
                valor = cantidad_hechos_por_provincia.get(x[2])
                cantidad_hechos_por_provincia[x[2]] = valor + x[5]
            else:
                cantidad_hechos_por_provincia[x[2]] = x[5]
    provincia_mas_comun = max(cantidad_hechos_por_provincia, key= cantidad_hechos_por_provincia.get)
    resultado[provincia_mas_comun] = cantidad_hechos_por_provincia[provincia_mas_comun]
    return resultado

#Funciones para printear en colores

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

def menu_principal():
    print("                                                          ")
    print("                                                          ")
    prYellow("          BIEVENIDO A REGISTRO DE DELITOS 1.0            ")
    print("                                                          ")
    prGreen("                     OPCIONES                             ")
    print("                                                          ")
    prCyan("  1- Top 5 de delitos más comunes según provincia         ")
    prCyan("  2- Top 5 de provincias más delictivas  según año        ")
    prCyan("  3- Top 10 de delitos más comunes según año              ")
    prCyan("  4- Top 10 histórico de provincias más delictivas        ")
    prCyan("  5- Top 10 histórico de delitos más comunes              ")
    prCyan("  6- Rastreo por texto (estadísticas por delito)          ")
    prCyan("  0- Salir del programa                                   ")
    print("                                                          ")
    print() 

def menu_provincias():
    print("                                                          ")
    print("                                                          ")
    prGreen("                     OPCIONES                             ")
    print("                                                          ")
    prCyan("  1- Ciudad Autónoma de Buenos Aires        13- Mendoza                       ")
    prCyan("  2- Buenos Aires                           14- Misiones               ")
    prCyan("  3- Catamarca                              15- Neuquén               ")
    prCyan("  4- Córdoba                                16- Río Negro               ")
    prCyan("  5- Corrientes                             17- Salta              ")
    prCyan("  6- Chaco                                  18- San Juan              ")
    prCyan("  7- Chubut                                 19- San Luis              ")
    prCyan("  8- Entre Ríos                             20- Santa Cruz              ")
    prCyan("  9- Formosa                                21- Santa Fe               ")
    prCyan("  10- Jujuy                                 22- Santiago del Estero              ")
    prCyan("  11- La Pampa                              23- Tierra del Fuego              ")
    print() 

def menu_anios():
    print("                                                         ")
    print("                                                         ")
    prGreen("                     OPCIONES                             ")
    print("                                                          ")
    prCyan("  1- 2014                                                 ")
    prCyan("  2- 2015                                                 ")
    prCyan("  3- 2016                                                 ")
    prCyan("  4- 2017                                                 ")
    prCyan("  5- 2018                                                 ")
    prCyan("  6- 2019                                                 ")
    prCyan("  7- 2020                                                 ")
    prCyan("  8- 2021                                                 ")
    print("                                                         ")