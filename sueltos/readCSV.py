import pandas as pd

df = pd.read_csv('data.csv', header = 0)

# Estas dos lineas hacen lo mismo, mostrar el valor de la columna 'Country Code' de la fila 0
# print(df.loc[0].at['Country Code'])

# Estas dos lineas hacen lo mismo, mostrar el valor de la columna 4 de la fila 0
# print(df.iat[0, 4])

buscar = input('Ingrese pais a buscar: ').title()
while buscar != '0':
  encontrado = df[df['Canonical Name'] == buscar]
  print(encontrado)
  buscar = input('Ingrese pais a buscar o 0 para finalizar: ').capitalize()
