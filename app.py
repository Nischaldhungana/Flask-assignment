from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return "Welcome to my REST API!"

def get_cat():
    cat = [{
        "cat_id": "3",
        "name": "cat",
        "birthdate": "2025-10-19",
        "weight": 8,
        "owner": "nischal",
        "image": "https://www.pexels.com/photo/white-and-grey-kitten-on-brown-and-black-leopard-print-textile-45201/"
    }]
    return jsonify(cat)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)