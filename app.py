from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs": 6,
        "category": "Indian City know as the Pink City",
        "word": "Jaipur"
    },
    {
        "inputs": 9,
        "category": "Indian City know as the Boston of India",
        "word": "Ahmedabad"
    },
    {
        "inputs": 5,
        "category": "Indian City know as the Diamond city of India",
        "word": "Surat"
    },
    {
        "inputs": 7,
        "category": "Indian City know as The City of Nawabs",
        "word": "Lucknow"
    },
    {
        "inputs": 6,
        "category": "Indian City know as the Leather City of the World",
        "word": "Kanpur"
    },
    {
        "inputs": 6,
        "category": "Indian City know as the Gateway of India",
        "word": "Mumbai"
    },
    {
        "inputs": 6,
        "category": "Indian City know as the Wine Capital of India",
        "word": "Nashik"
    },
    {
        "inputs": 9,
        "category": "Indian City know as the Garden city of India",
        "word": "Bangalore"
    },
    {
        "inputs": 9,
        "category": "Indian City know as the Silicon Valley of India",
        "word": "Bangalore"
    },
    {
        "inputs": 5,
        "category": "Indian City know as the Scotland of India",
        "word": "Coorg"
    },
    {
        "inputs": 6,
        "category": "Indian City know as the Sandalwood city",
        "word": "Mysore"
    },
    {
        "inputs": 9,
        "category": "Indian City know as the City of Pearls",
        "word": "Hyderabad"
    },
    {
        "inputs": 7,
        "category": "Indian City know as The City of Festivals or Athens of the East",
        "word": "Madurai"
    },
    {
        "inputs": 7,
        "category": "Indian City know as the Detroit of Asia",
        "word": "Chennai"
    },
    {
        "inputs": 11,
        "category": "Indian City know as the Paris of the East",
        "word": "Pondicherry"
    },
    {
        "inputs": 10,
        "category": "Indian City know as the Steel city of India",
        "word": "Jamshedpur"
    },
    {
        "inputs": 12,
        "category": "Indian City know as the Temple city of India",
        "word": "Bhubaneshwar"
    },
]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run()
