from flask import Flask, render_template, request, jsonify
import pandas as pd
import re

app = Flask(__name__)

# Read the Excel file without headers
df = pd.read_excel('Movie Data.xlsx', header=None)

# Split the data into columns using the comma as a separator
# We only split from the second row (index 1)
df[['Movie Title', 'Release Year', 'Budget (millions $)', 'Rotten Tomatoes Score', 'Genre']] = df[0].str.split(',', expand=True)

# Remove the original column
df = df.drop(columns=[0])

# Remove the first row that contained the original headers
df = df.iloc[1:]

# Reset the indices
df.reset_index(drop=True, inplace=True)

# Convert columns to appropriate types
df['Release Year'] = df['Release Year'].astype(int)
df['Budget (millions $)'] = df['Budget (millions $)'].astype(float)
df['Rotten Tomatoes Score'] = df['Rotten Tomatoes Score'].astype(float)

def parse_query(query):
    filters = {}

    # Detect the year
    year_match = re.search(r'\b(2017|2018|2019|2020|2021|2022)\b', query)
    if year_match:
        filters['Release Year'] = int(year_match.group())

    # Detect budget
    budget_match = re.search(r'\b(?:budget|cost|costo)\s*(?:of)?\s*(\d+)', query)
    if budget_match:
        filters['Budget (millions $)'] = float(budget_match.group(1))

    # Detect Rotten Tomatoes score
    score_match = re.search(r'above\s*(\d+)', query)
    if score_match:
        filters['Rotten Tomatoes Score'] = float(score_match.group(1))

    # Detect genre
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

    # Apply filters to the DataFrame
    results = df.copy()

    # Filter by release year if provided
    if 'Release Year' in filters:
        results = results[results['Release Year'] == filters['Release Year']]
        print(f"Filtered by Release Year: {filters['Release Year']}")

    # Filter by budget if provided
    if 'Budget (millions $)' in filters:
        results = results[results['Budget (millions $)'] <= filters['Budget (millions $)']]
        print(f"Filtered by Budget: {filters['Budget (millions $)']}")

    # Filter by Rotten Tomatoes score if provided
    if 'Rotten Tomatoes Score' in filters:
        results = results[results['Rotten Tomatoes Score'] > filters['Rotten Tomatoes Score']]
        print(f"Filtered by Rotten Tomatoes Score: {filters['Rotten Tomatoes Score']}")

    # Filter by genre if provided
    if 'Genre' in filters:
        results = results[results['Genre'] == filters['Genre']]
        print(f"Filtered by Genre: {filters['Genre']}")

    # Show the results in the console for debugging
    print("Filtered Results:", results.to_dict(orient='records'))

    return jsonify(results.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
