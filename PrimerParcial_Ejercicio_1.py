print('*** Bienvenido al sistema de generacion de email del TECBA')
nombre = input('Cual es tu nombre?: ')
nombre_2 = nombre[0:3]
#nombre = nombre.lower()
apellido = input('Cual es tu apellido?: ')
# Generamos el emai
email_generado = f'{nombre_2.lower()}.{apellido.lower()}@tecba.com'
#print(email_generado)
print(f'''
Tu nuevo email generado por el sistema es:
    {email_generado}
    *** Felicidades ***
''')