import os
import pandas as pd

# Carga del archivo al dataframe de trabajo
file_path = "C:/Users/jodam/Downloads/EstudiantesExtemporaneos2024-1.xlsx"

if not os.path.isfile(file_path):
  raise FileNotFoundError(f"{file_path} not found.")

piam20241 = pd.read_excel(file_path)

# Obtener información descriptiva de los registros en cada columna
info_duplicados = {}
info_unicos = {}


def obtener_info(columna):

  #Verificar registros duplciados por columna
  duplicados = piam20241[piam20241[columna].duplicated(keep=False)]
  duplicados_por_valor = duplicados[columna].value_counts()

  # Concatenar información de duplicados y valores duplicados
  info_concatenada = duplicados_por_valor.apply(lambda x: f"{x} duplicados: {', '.join(duplicados[duplicados[columna] == x].index.astype(str))}")
  info_duplicados[columna] = info_concatenada

  #Valores unicos por cada columna
  unicos = piam20241[columna].unique()
  info_unicos[columna] = unicos

# Ejecutar obtener_info para todas las columnas del DataFrame
for columna in piam20241.columns:
  obtener_info(columna)

# Funciones para cada opción
def opcion_1():
    print("****************************************************************************")
    print(' Información general del DataFrame:')
    piam20241.info()

def opcion_2():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(' Información descriptiva del DataFrame:')
    print(piam20241.describe(include="all"))

def opcion_3():
    print("============================================================================")
    print(' Información de duplicados y valores únicos de todas las columnas:')
    for columna in piam20241.columns:
      print(f"Información de la columna '{columna}':")
      print(f"Valores únicos: {info_unicos[columna]}")
      print(f"Valores duplicados: {info_duplicados[columna]}")
      print("----------------------")

def opcion_4():
    columna = input("Ingrese el nombre de la columna para mostrar información: ")
    if columna in piam20241.columns:
        print("---------------------------------------------------------------------------")
        print(f"Información de la columna '{columna}':")
        print(piam20241[columna].describe())
        print(f"Valores únicos: {info_unicos[columna]}")
        print(f"Valores duplicados: {info_duplicados[columna]}")
        print("----------------------")
        print()
    else:
        print("La columna especificada no existe.")
        print()
# Switch case
opcion = input("MENU ANALISIS\n 1. Informacion general del DataFrame\n 2. Información descriptiva del DataFrame:\n 3. Información de duplicados y valores únicos de todas las columnas\n 4. Informacion por columna particular: \n Ingrese la opcion:")
if opcion == "1":
    opcion_1()
elif opcion == "2":
    opcion_2()
elif opcion == "3":
    opcion_3()
elif opcion == "4":
    opcion_4()
else:
    print("Opción no válida.")