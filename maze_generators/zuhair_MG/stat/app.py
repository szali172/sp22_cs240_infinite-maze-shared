from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)


# Route for maze generation
@app.route('/generate', methods=["GET"])
def GET_static_maze_segment():
    
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    geom = ["9ae3aac", "59ae9c5", "559a655", "0260a41", "5ba2c55", "5906575", "36b02a6"]
    return jsonify({'geom' : geom, 'Content-Type': 'application/json', 'Cache-Control' : 'max-age=3600', 'Age' : 0}), 200


# Route for registering my MG to the middleware
@app.route('/registerMG', methods=["PUT"])
def register_MG():

    # Middleware requests name, url, author and an optional weight(0 to 1)
    json = {'name' : 'zuhair_static_MG', 'url' : request.host_url, 'author' : "Zuhair Ali"}
        
    # Middleware requesting the data is running on <API_URL>
    response = requests.put('http://localhost:5000/addMG', json=json)
    
    return response.text, response.status_code