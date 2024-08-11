from flask import Flask, render_template, request, jsonify
import pandas as pd
import re

app = Flask(__name__)

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

# Convertir las columnas a tipos apropiados
df['Release Year'] = df['Release Year'].astype(int)
df['Budget (millions $)'] = df['Budget (millions $)'].astype(float)
df['Rotten Tomatoes Score'] = df['Rotten Tomatoes Score'].astype(float)

def parse_query(query):
    filters = {}

    # Detectar el año
    year_match = re.search(r'\b(2017|2018|2019|2020|2021|2022)\b', query)
    if year_match:
        filters['Release Year'] = int(year_match.group())

    # Detectar presupuesto
    budget_match = re.search(r'\b(?:budget|cost|costo)\s*(?:of)?\s*(\d+)', query)
    if budget_match:
        filters['Budget (millions $)'] = float(budget_match.group(1))

    # Detectar puntuación de Rotten Tomatoes
    score_match = re.search(r'above\s*(\d+)', query)
    if score_match:
        filters['Rotten Tomatoes Score'] = float(score_match.group(1))

    # Detectar género
    genres = ['Action', 'Adventure', 'Comedy', 'Drama', 'Family', 'Fantasy', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller']
    for genre in genres:
        if genre.lower() in query.lower():
            filters['Genre'] = genre
            break

    return filters

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    filters = parse_query(query)

    # Aplicar los filtros al DataFrame
    results = df.copy()

    # Filtrar por año de lanzamiento si se proporciona
    if 'Release Year' in filters:
        results = results[results['Release Year'] == filters['Release Year']]
        print(f"Filtered by Release Year: {filters['Release Year']}")

    # Filtrar por presupuesto si se proporciona
    if 'Budget (millions $)' in filters:
        results = results[results['Budget (millions $)'] <= filters['Budget (millions $)']]
        print(f"Filtered by Budget: {filters['Budget (millions $)']}")

    # Filtrar por puntuación de Rotten Tomatoes si se proporciona
    if 'Rotten Tomatoes Score' in filters:
        results = results[results['Rotten Tomatoes Score'] > filters['Rotten Tomatoes Score']]
        print(f"Filtered by Rotten Tomatoes Score: {filters['Rotten Tomatoes Score']}")

    # Filtrar por género si se proporciona
    if 'Genre' in filters:
        results = results[results['Genre'] == filters['Genre']]
        print(f"Filtered by Genre: {filters['Genre']}")

    # Mostrar los resultados en la consola para depuración
    print("Filtered Results:", results.to_dict(orient='records'))

    return jsonify(results.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
