from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_products():
    with open("products.json", "r") as f:
        return json.load(f)

def read_csv_products():
    products = []
    with open("products.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ("json", "csv"):
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=[]
        )

    try:
        if source == "json":
            products = read_json_products()
        else:
            products = read_csv_products()
    except Exception:
        return render_template(
            "product_display.html",
            error="Error reading data file",
            products=[]
        )

    # Filter by id if provided
    if product_id is not None:
        try:
            product_id = int(product_id)
            products = [p for p in products if p["id"] == product_id]
            if not products:
                return render_template(
                    "product_display.html",
                    error="Product not found",
                    products=[]
                )
        except ValueError:
            return render_template(
                "product_display.html",
                error="Invalid product id",
                products=[]
            )

    return render_template(
        "product_display.html",
        products=products,
        error=None
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
