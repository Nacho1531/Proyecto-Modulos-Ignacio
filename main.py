# Proyecto: [Módulos Y Funciones Python]
# Estudiante: [Ignacio Masís Cascante]
# Fecha de Inicio: [22/08/2025]
# Fecha de Entrega: [25/09/2025]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.
#from analisis_datos.carga_datos import generar_lista_compras
#from analisis_datos.estadisticas import media

from analisis_datos import*

def saludar():
    print('Hola desde la función')
    
if __name__ == '__main__':
   compras = generar_lista_compras()
   print(compras)
   mediana = mediana(list(compras.values()))
   print('Promedio de costo por artículo :',mediana)