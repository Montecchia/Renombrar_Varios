import os

directorio = input("Ingrese el directorio: ")
if not os.path.exists(directorio):
    exit("El directorio no existe")

nombre = input("Ingrese el nombre para los archivos: ")

archivos = os.listdir(directorio)

for archivo in archivos:
    posible_archivo = directorio + "/" + archivo

    if not os.path.isdir(posible_archivo):
        numero = " - "
        extension = "."
        escribir_extension = False

        for letra in archivo:
            if escribir_extension:
                extension += letra
            else:
                if letra.isdigit():
                    numero += letra
                if letra == ".":
                    escribir_extension = True
        numero = numero[0:5]
        nuevo_nombre = directorio + "/" + nombre + numero + extension
        os.rename(posible_archivo, nuevo_nombre)
