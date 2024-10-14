# Documentation for SPARQL Endpoint

## Overview
This documentation provides an overview of a Flask web application designed to execute SPARQL queries on RDF data. The application uses the rdflib library to handle RDF data and perform SPARQL queries.

## Prerequisites
Before running this application, ensure you have the following installed:
* Python 3.x <br>
* Flask <br>
* rdflib
## Application Structure
* Flask Application: The main web application instance.
* RDF Graph: The RDF graph loaded from an OWL file.
* SPARQL Query Execution:  A function to execute SPARQL queries on the RDF graph.
* Routes:<br>
	/: The home page rendering INDEX.html. <br>
	/query: Endpoint to handle SPARQL query submission and display results.
### HTML Templates
* **INDEX.html** 
This template contain a form for users to submit their SPARQL queries. Example:
* **RESULT.html** 
This template display the query results.
## Conclusion
This documentation outlines the structure and functionality of the RDF SPARQL Query web application. It explains how to set up, run, and use the application to execute SPARQL queries on RDF data.


