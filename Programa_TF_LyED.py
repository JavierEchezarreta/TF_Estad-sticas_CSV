from Biblioteca_TF_LyED import *
import os
import time

while True:
    menu_principal()
    opcion = input("Ingrese una opcion: ")

    if opcion == '1':
        os.system('clear')
        prYellow(f"        Top 5 delitos más comunes según provincia")
        menu_provincias()
        while True:
            print()
            try:
                print()
                nombre_provincia = input("Escriba el nombre de la provincia o presione enter para volver al menu principal: ")
                if nombre_provincia == '':
                    os.system('clear')
                    break
                print()
                resultado = top5_delitos(nombre_provincia).items()
                prYellow(f"        Top 5 delitos más comunes en {nombre_provincia}")
                print()
                numero= 1
                for x, y in resultado:
                    print(f"{numero}- Delito: {x} - Cantidad de hechos: {'{:,}'.format(y[0])} - Cantidad de víctimas: {'{:,}'.format(y[1])} ")
                    numero += 1
                
            except:
                os.system('clear')
                print("Nombre inválido, intente nuevamente")
                time.sleep(3)
                os.system('clear')
                prYellow(f"        Top 5 delitos más comunes según provincia")
                menu_provincias()    

    elif opcion == '2':
        os.system('clear')
        prYellow('          Top 5 provincias más delictivas')
        menu_anios()
        while True:
            print()
            try:
                print()
                anio = input("Escriba el año o presione enter para volver al menu principal: ")
                if anio == '':
                    os.system('clear')
                    break
                print()
                resultado = top5_provincias_delictivas(int(anio)).items()
                prYellow(f"        Top 5 provincias más delictivas en {anio}")
                print()
                numero= 1
                for x, y in resultado:
                    print(f"{numero}- Provincia: {x} - Cantidad de hechos: {'{:,}'.format(y[0])} - Cantidad de víctimas: {'{:,}'.format(y[1])} ")
                    numero += 1
            
            except:
                os.system('clear')
                print("Año inválido, intente nuevamente")
                time.sleep(3)
                os.system('clear')
                prYellow('          Top 5 provincias más delictivas')
                menu_anios() 

    elif opcion == '3':
        os.system('clear')
        prYellow('            Top 10 delitos más comunes')
        menu_anios()
        while True:
            print()
            try:
                print()
                anio = input("Escriba el año o presione enter para volver al menu principal: ")
                if anio == '':
                    os.system('clear')
                    break
                print()
                resultado = top10_delitos_comunes_por_anio(int(anio)).items()
                prYellow(f"        Top 10 delitos más comunes en {anio}")
                print()
                numero= 1
                for x, y in resultado:
                    print(f"{numero}- Provincia: {x} - Cantidad de hechos: {'{:,}'.format(y[0])} - Cantidad de víctimas: {'{:,}'.format(y[1])} ")
                    numero += 1
            
            except:
                os.system('clear')
                print("Año inválido, intente nuevamente")
                time.sleep(3)
                os.system('clear')
                prYellow('            Top 10 delitos más comunes')
                menu_anios() 

    elif opcion == '4':
        os.system('clear')
        while True:
            print()
            try:
                print()
                resultado = top10_historico_provincias_delictivas().items()
                prYellow(f"        Top 10 histórico de provincias más delictivas")
                print()
                numero= 1
                for x, y in resultado:
                    print(f"{numero}- Provincia: {x} - Cantidad de hechos: {'{:,}'.format(y[0])} - Cantidad de víctimas: {'{:,}'.format(y[1])} ")
                    numero += 1

                print()
                anio = input("Presione enter para volver al menu principal ")
                if anio == '':
                    os.system('clear')
                    break
            
            except:
                os.system('clear')
                print("Año inválido, intente nuevamente")
                time.sleep(3)
                os.system('clear')
                menu_anios() 
                
    elif opcion == '5':
        os.system('clear')
        while True:
            print()
            try:
                print()
                resultado = top10_historico_delitos_comunes().items()
                prYellow(f"        Top 10 histórico de delitos más comunes")
                print()
                numero= 1
                for x, y in resultado:
                    print(f"{numero}- Delito: {x} - Cantidad de hechos: {'{:,}'.format(y[0])} - Cantidad de víctimas: {'{:,}'.format(y[1])} ")
                    numero += 1

                print()
                anio = input("Presione enter para volver al menu principal ")
                if anio == '':
                    os.system('clear')
                    break
            
            except:
                os.system('clear')
                print("Año inválido, intente nuevamente")
                time.sleep(3)
                os.system('clear')
                menu_anios() 

    elif opcion == '6':
        os.system('clear')
        prYellow(f"        Rastreo por texto (estadísticas por delito)")
        while True:
            print()
            try:
                print()
                delito = input("Escriba un delito o presione enter para volver al menu principal: ")
                if delito == '':
                    os.system('clear')
                    break
                resultado1 = filtrar_delito_total(delito).items()
                resultado2 = filtrar_delito_provincia(delito).items()
                resultado3 = filtrar_delito_anio(delito).items()
                print()
                prYellow(f"        Datos históricos por delito")
                print()
                for x, y in resultado1:
                    print(f"Delito: {x} - Total histórico de hechos: {'{:,}'.format(y)}")
                for x, y in resultado2:
                    print(f"La Provincia donde más se cometió este delito fue {x}. Un total de {'{:,}'.format(y)} veces.")
                for x, y in resultado3:
                    print(f"El año donde más se repitió este delito fue en {x}. Un total de {'{:,}'.format(y)} veces.")
            
            except:
                os.system('clear')
                print("Delito inválido, intente nuevamente")
                time.sleep(3)
                os.system('clear') 
                print(f"        Rastreo por texto (estadísticas por delito)")


    elif opcion == '0':
        print()
        print (f"       GRACIAS POR USAR  EL PROGRAMA       ")
        print()
        break
            

    else:
        os.system('clear')
        print("Opción inválida, intente nuevamente")
        time.sleep(3)
        os.system('clear')