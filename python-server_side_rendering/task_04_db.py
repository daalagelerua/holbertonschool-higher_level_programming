import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Fonction pour charger les données JSON
def load_data_from_json():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Fonction pour charger les données CSV
def load_data_from_csv():
    try:
        with open("products.csv", newline="") as file:
            reader = csv.DictReader(file)
            return [
                {"id": int(row["id"]), "name": row["name"], "category": row["category"], "price": float(row["price"])}
                for row in reader
            ]
    except FileNotFoundError:
        return []

# Fonction pour charger les données SQLite
def load_data_from_sqlite():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        conn.close()

        # Transformation des lignes en format dictionnaire
        return [
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
            for row in rows
        ]
    except sqlite3.Error as e:
        return []

# Route principale pour afficher les produits
@app.route('/products')
def products():
    # Récupère les paramètres de la requête
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)

    # Vérifie la source et charge les données
    if source == "json":
        products = load_data_from_json()
    elif source == "csv":
        products = load_data_from_csv()
    elif source == "sql":
        products = load_data_from_sqlite()
    else:
        return render_template("product_display.html", error="Wrong source. Use 'json', 'csv' or 'sql'.")

    # Filtre les produits par id si fourni
    if product_id:
        products = [p for p in products if p["id"] == product_id]
        if not products:
            return render_template("product_display.html", error="Product not found.")

    # Affiche les produits dans la template
    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)