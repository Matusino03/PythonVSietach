#!/usr/bin/env python3
from flask import Flask, jsonify, request

MOVIES = list()
MOVIES.append({"id": 0 ,"title": "Matrix", "genre": "sci-fi/document"})
my_next_id = 1

app = Flask(__name__)

@app.route("/api/")
def index():
    return "Ahoj z API :)"

@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(MOVIES)

@app.route("/api/movies", methods=["POST"])
def add_movies():
    movie = request.json
    global my_next_id
    movie["id"] = my_next_id
    my_next_id += 1

    MOVIES.append(movie)
    return jsonify(movie), 201

@app.route("/api/movies/<id>", methods=["DELETE"])
def del_movie(id):
    for movie in MOVIES:
        if movie[id] == int(id):
            temp = movie
            MOVIES.remove(movie)
            return jasonify(temp), 200
        else:
            return jasonify({"error": "ID not found"}), 404
        
@app.route("/api/movies/<id>", methods=["PUT"])
def edit_movie(id):
    movie_edit = request.json
    for movie in MOVIES:
        if movie[id] == int(id):
            if "title" in movie_edit.keys():
                movie["title"] = movie_edit["title"]
            if "genre" in movie_edit.keys():
                movie["genre"] = movie_edit["genre"]
            return jasonify(movie), 200
        else:
            return jasonify({"error": "ID not found"}), 404
            

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

