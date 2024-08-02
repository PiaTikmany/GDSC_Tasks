# Import necessary modules from Flask
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Define a route for GET requests to '/api/endpoint1'
@app.route('/api/endpoint1', methods=['GET'])
def get_sample_data():
    # Create a sample dictionary with various data types
    sample_data = {
        "name": "pia"
    }
    # Return the sample data as a JSON response
    return jsonify(sample_data)

# Define a route for POST requests to '/api/endpoint2'
@app.route('/api/endpoint2', methods=['POST'])
def post_data():
    # Check if the incoming request contains JSON data
    if request.is_json:
        # If it does, get the JSON data
        data = request.get_json()
        # Prepare a response dictionary
        response = {
            "message": "Data received successfully",
            "data": data
        }
        # Return the response as JSON with a 201 (Created) status code
        return jsonify(response), 201
    else:
        # If the request doesn't contain JSON data, return an error
        return jsonify({"error": "Request must be in JSON format"}), 400

# Check if this script is being run directly (not imported)
if __name__ == '__main__':
    # If so, start the Flask development server
    app.run()
