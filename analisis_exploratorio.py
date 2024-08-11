import pandas as pd

# Leer el archivo Excel sin encabezados
df = pd.read_excel('Movie Data.xlsx', header=None)
# Separar los datos en columnas usando la coma como separador
# Solo separamos a partir de la segunda fila (índice 1)
df[['Movie Title', 'Release Year', 'Budget (millions $)', 'Rotten Tomatoes Score', 'Genre']] = df[0].str.split(',', expand=True)
# Eliminar la columna original
df = df.drop(columns=[0])
# Eliminar la primera fila que contenía los encabezados originales
df = df.iloc[1:]
# Reiniciar los índices
df.reset_index(drop=True, inplace=True)
# Mostrar el DataFrame resultante
print(df)

# Mostrar la cantidad de filas y columnas
print(df.shape)
# Mostrar las columnas del DataFrame
print(df.columns)
# Mostrar las primeras filas del DataFrame
print(df.head())
# Mostrar información del DataFrame
print(df.info())
# Mostrar estadísticas del DataFrame
print(df.describe())

# Mostrar la cantidad de categorías y sus valores únicos para cada columna
for column in df.columns:
    unique_categories = df[column].nunique()
    categories = df[column].unique()
    print(f"Columna: {column}")
    print(f"Cantidad de categorías: {unique_categories}")
    print(f"Categorías: {', '.join(map(str, categories))}")
    print()

    # Contar el total de cada categoría en la columna
    category_counts = df[column].value_counts()
    print(f"Total de cada categoría en la columna {column}:")
    print(category_counts)
    print()
