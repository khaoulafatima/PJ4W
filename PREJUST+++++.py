# Import necessary modules from Flask and rdflib
from flask import Flask, request, render_template
from rdflib import Graph

# Create a Flask application instance
app = Flask(__name__)

# Load RDF data into a graph
g = Graph()
# Parse the RDF data from the specified file. Adjust the file path and format as needed.
g.parse("PREJUS4KG.owl", format="xml")  # XML format is used; change if necessary

# Function to execute SPARQL queries on the RDF graph
def execute_sparql_query(query):
    result = g.query(query)  # Execute the query and store the result
    return result

# Route to render the index page
@app.route('/')
def index():
    return render_template('INDEX.html')  # Render the 'INDEX.html' template

# Route to handle SPARQL queries submitted via POST request
@app.route('/query', methods=['POST'])
def query():
    # Retrieve the SPARQL query from the POST request
    sparql_query = request.form['query']
    try:
        # Execute the SPARQL query
        result = execute_sparql_query(sparql_query)
        results = []  # List to store query results
        headers = result.vars  # Extract variable names (headers) from the result
        for row in result:
            # Convert each row of the result to a list of strings
            results.append([str(value) for value in row])
        # Render the 'RESULT.html' template with the query, headers, and results
        return render_template('RESULT.html', query=sparql_query, headers=headers, results=results)
    except Exception as e:
        # Handle exceptions by returning an error message
        return f"An error occurred: {str(e)}"

# Run the Flask application in debug mode if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
