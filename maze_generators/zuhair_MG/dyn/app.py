from flask import Flask, render_template, request, jsonify
import requests, random

from rotate import rotate_maze


app = Flask(__name__)


# Route for maze generation
@app.route('/generate', methods=["GET"])
def GET_dynamic_maze_segment():

    geom = ["9ae3aac", "59ae9c5", "559a655", "0260a41", "5ba2c55", "5906575", "36b02a6"]
    rotated_maze = geom
    r = random.randint(0, 3) 

    for x in range(r):
        rotated_maze = rotate_maze(rotated_maze)
    
    return jsonify({'geom' : rotated_maze, 'Content-Type': 'application/json'}), 200

  
# Route for registering my MG to the middleware
@app.route('/registerMG', methods=["PUT"])
def register_MG():

    # Middleware requests name, url, author and an optional weight(0 to 1)
    json = {'name' : 'zuhair_dynamic_MG', 'url' : request.host_url, 'author' : "Zuhair Ali_"}
        
    # Middleware requesting the data is running on <API_URL>
    response = requests.put('http://localhost:5000/addMG', json=json)
    
    return response.text, response.status_code