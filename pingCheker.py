from requests import get, exceptions

def comprobarConexion():
    
    while (True):

        try:
            print("""Comprobar el estado del sitio web
Ejemplo: https://duckduckgo.com""")
            web=input('ingrese la web: ')
            get(web, timeout = 5)
            print('Sitio WEB ONLINE')
        except exceptions.ConnectionError:
            print('Sitio WEB OFFLINE')

        print("<=>=<=>=<=>=<=><=>=<=><=>=<=><=>=<=><=>=<=><=>=<=><=>=<=><=>=<=>")

        print("Deseas continuar? S/N")
        op = input("Ingre →→→  ")
        if op == "s" or  op == "si" or  op == "yes" or  op == "YES" or  op == "Y" or  op == "y" or  op == "SI":
            print("Continuando...")
            continue
        elif op == "n" or  op == "no" or  op == "not" or  op == "NOT" or  op == "N" or  op == "n" or  op == "NO":
            print("Saliendo...")
            break

comprobarConexion()