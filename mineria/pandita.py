import pandas as pd

#--------Carga y exploracion de datos----------------
df = pd.read_csv('ModalidadVirtual.csv')

print("--- Primeras 5 filas ---")
print(df.head())

print("\--- Resumen Estadístico ---")
print(df.describe())

# 3. Información del DataFrame
print("\--- Información General ---")
df.info()

#---------Limpieza de Datos---------------
# df.isnull().sum()
# isnull() marca con un "True" cada celda vacía.
# sum() suma esos "True", dándote el total de datos faltantes por columna.

# Muestra la cantidad de valores nulos y eliminar valores faltantes
print("\n--- Cantidad de valores nulos por columna ---")
print(df.isnull().sum())


#. Rellenar valores faltantes: Rellena los valores faltantes con 0.
#fillna,coloca un 0 cuando0 encuentra un valor vacio 
df = df.fillna(0)
print("\n--- Nulos después de rellenar con 0 ---")
print(df.isnull().sum())


 #Eliminar columnas innecesarias: Elimina una columna que no sea relevante para el análisis.

 #df.drop(columns=[...]) borrar columna

 # Eliminar una columna por su nombre
 #En este caso se desea eliminar el sexo del personal ya que resulta irrelevante al analisis 
df = df.drop(columns=['sexo'])

print(df.columns)


#-----------Filtrado y Selección de Datos-------------
#Filtrar con múltiples condiciones: Filtra las filas que cumplan con múltiples condiciones.

#Para filtrar usamos los corchetes df[...]
#El símbolo &: Significa "Y" (se deben cumplir ambas condiciones al mismo tiempo).
#El símbolo |: Significa "O" (se puede cumplir una o la otra).

print("Queremos personas de 20 años y con horarios flexibles,vamo a explotarlas muajaja")
filtro_especifico = df[(df['edad'] > 20) & (df['positivo'] == 'Horario flexible.')]
print(f"Se encontraron {len(filtro_especifico)} registros que cumplen ambas condiciones.")
print(filtro_especifico.head())


#Seleccionar columnas: Selecciona solo ciertas columnas para un nuevo DataFrame.
#df[['Col1', 'Col2']]Para elegir columnas, pasamos una lista de nombres dentro de los corchetes:
columnas_interes = ['carrera', 'positivo', 'trabajo'] 
df_seleccionado = df[columnas_interes]
print("Lista de candidatos por carrera, puntos positivos y tipo de trabajo")
print(df_seleccionado.head())


#------------Operaciones y Agrupación---------

#Calcular Suma y Media de una columna
#mean es promedio/media
columna_num = 'edad'  
suma_total = df[columna_num].sum()
media_valor = df[columna_num].mean()

print(f"\n--- Estadísticas de {columna_num} ---")
print(f"Suma Total: {suma_total}")
print(f"Media (Promedio): {media_valor:.2f}")

# Agrupar datos (Media de Edad por Carrera/Modalidad)
# Esto responde: ¿Cuál es el promedio de edad en cada carrera?
#Agrupación (groupby)Primero indicas por qué columna quieres clasificar  y luego qué operación quieres hacer sobre otra columna 
agrupado = df.groupby('carrera')[columna_num].mean()
print(agrupado)

#Crear una Tabla Pivote (Resumen cruzado)
#values: La columna que quieres calcular (números).
#index: Lo que aparecerá en las filas.
#columns: Lo que aparecerá en las columnas superiores.
#aggfunc: La función (puede ser 'mean', 'sum', 'count').
tabla_pivote = df.pivot_table(values='edad', index='carrera', columns='acepta', aggfunc='mean')
print(tabla_pivote)


#----------------------------------Manipulación de Datos---------------

#by='Edad': Se indica el nombre de la columna que servirá como guía para el orden.
#ascending=False/True, False para orden descendente y True para orden Ascendente-

df_ordenado = df.sort_values(by='edad', ascending=False)

print("\n--- Datos Ordenados por edad (Mayor a Menor) ---")
print(df_ordenado.head())

#Fin :)
