import os
diccionario = {}
sw = True

def fnt_agregar(dicionario, placa_vehiculo, descripcion_vehiculo, nombre_conductor, contacto_conductor, ruta, descripcion_carga):
    if placa_vehiculo == '' or descripcion_vehiculo == '' or nombre_conductor == '' or contacto_conductor == '' or ruta == '' or descripcion_carga == '':
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        dicionario[placa_vehiculo] = {'descripcion_vehiculo': descripcion_vehiculo, 'nombre_conductor': nombre_conductor, 'contacto_conductor': contacto_conductor, 'ruta': ruta, 'descripcion_carga': descripcion_carga}
        enter = input(f'\nLa persona {nombre_conductor} ha sido registrada con éxito <ENTER>')
    
def fnt_selector(op):
    if op == '1':
        os.system ('cls')
        nombre_conductor = input('Nombre: ')
        placa_vehiculo = input('Placa: ')
        descripcion_vehiculo = input('Descripcion: ')
        contacto_conductor = input('Contacto: ')
        ruta = input('Ruta: ')
        descripcion_carga = input('Descripcion de carga: ')
        fnt_agregar(diccionario, placa_vehiculo, descripcion_vehiculo, nombre_conductor, contacto_conductor, ruta, descripcion_carga)

while sw == True:
    os.system('cls')
    print(' ---¡MENU!--- ')
    opcion = input('1. Registrar\n2. Mostrar\n3. Salir\n- >  ')
    if opcion == '1':
        fnt_selector(opcion)
    elif opcion == '2':
        os.system('cls')
        print('¡¡MENU DE REGISTROS!!')
        print('\nCantidad de registros: ',len(diccionario),'\n')
        for clave, valor in diccionario.items():
            print(f"{clave}: {valor}")
        enter = input('\n\nPresione ENTER para continuar...')
    elif opcion == '3':
        sw = False