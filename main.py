# from fastapi import Body, FastAPI
from flask import Flask, request
import requests
import json

app = Flask(__name__)
url = 'https://www.fsis.usda.gov/shared/data/EN/foodkeeper.json'

@app.route("/")
def root():
    
    return {"message": "hello world"}

@app.route("/category")
def get_categories():
    r = requests.get(url)
    js = r.json()['sheets']
    categories = js[1]
    if(request.args.get('category_id') == None):
        return categories
    else:
        id = request.args.get('category_id')
        categories = categories['data']
        for cat in categories:
            cat_dict = {}
            for el in cat:
                cat_dict.update(el)
            if(cat_dict['ID']== float(id)):
                categories = cat_dict


    return categories

# TODO /products/:id

@app.route("/product")
def get_products():
    r = requests.get(url)
    js = r.json()['sheets']
    products = js[2]
    return products

# TODO /products/:id/name

@app.route("/product/category")
def get_product_category():
    return {"product": "something",
            "category": "vagueries"}

# TODO /product/category/:id


# TODO /category/:id


@app.route("/cookingMethod")
def get_cooking_methods():
    r = requests.get(url)
    js = r.json()['sheets']
    cookingMethods = js[4]
    return cookingMethods

# TODO /cookingMethod/:id


@app.route("/cookingTip")
def get_cooking_tip():
    r = requests.get(url)
    js = r.json()['sheets']
    cookingTips = js[3]
    return cookingTips
    
# TODO /cookingTip/:id

if __name__ == '__main__':
    app.run(debug=True)