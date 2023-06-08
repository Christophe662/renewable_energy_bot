# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 10:30:05 2023

@author: Christophe
"""

from flask import Flask, render_template, request, jsonify

from chat import get_response ,extract_city 

app= Flask(__name__)

if __name__ == '__main__':
    # Ligne pour spécifier le port
     app.run(host='0.0.0.0', port=8000)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text=request.get_json().get("message")
    city=extract_city(text)
    response= get_response(text,city)
    message={"answer": response}
    return jsonify(message)

if __name__=="__main__":
    app.run(debug=True)
