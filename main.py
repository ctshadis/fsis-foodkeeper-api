
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)
url = 'https://www.fsis.usda.gov/shared/data/EN/foodkeeper.json'

def get_data():
    r = requests.get(url)
    js = r.json()['sheets']
    return js

@app.route("/")
def root():
    return render_template('readme.html'), 200

# Return all or by-id food categories
@app.route("/category")
def get_categories():
    js = get_data()
    categories = js[1]
    cat_dict = {}
    cat_list = {}
    if(request.args.get('id') == None):
        return categories, 200
    else:
        id = request.args.get('id')
        categories = categories['data']
        
        for cat in categories:
            cat_dict = {}
            for el in cat:
                cat_dict.update(el)
            if(cat_dict['ID']== float(id)):
                cat_list = cat_dict
                break
    if(len(cat_list) != 0):
        return cat_list, 200
    else: 
        return "Resource Not Found", 404


# Return all or by name or by id food products
@app.route("/product")
def get_products():
    js = get_data()
    products = js[2]
    prods_list = {}

    # No queries
    if(request.args.get('id') == None and request.args.get('name') == None):
        return products, 200
    if(request.args.get('id') != None and request.args.get('name') != None):
        return "Bad request, too many query parameters", 400
    # ID query
    elif(request.args.get('id') != None):
        id = request.args.get('id')
        products = products['data']
        for prod in products:
            prod_dict = {}
            for el in prod:
                prod_dict.update(el)
            if(prod_dict['ID']== float(id)):
                prods_list = prod_dict
                break
    # Name Query
    elif(request.args.get('name') != None):
        name = request.args.get('name')
        products = products['data']
        for prod in products:
            prod_dict = {}
            for el in prod:
                prod_dict.update(el)
            if(prod_dict['Name'].lower()== name.lower()):
                prods_list = prod_dict
                break
    if(len(prods_list) != 0):
        return prods_list, 200
    else: 
        return "Resource Not Found", 404


@app.route("/product/<ID>/name")
def get_product_name(ID):
    js = get_data()
    products = js[2]['data']
    prods_list={}
    for prod in products:
            prod_dict = {}
            for el in prod:
                prod_dict.update(el)
            if(prod_dict['ID']== float(ID)):
                prods_list = prod_dict
                break
    if(len(prods_list) != 0):
        return {"Name": prod_dict['Name']}, 200
    else: 
        return "Resource Not Found", 404
    

@app.route("/product/<ID>/category")
def get_product_category(ID):
    js = get_data()
    products = js[2]['data']
    prods_list = {}
    for prod in products:
            prod_dict = {}
            for el in prod:
                prod_dict.update(el)
            if(prod_dict['ID']== float(ID)):
                prods_list = prod_dict
                break
    if(len(prods_list) != 0):
        return {"Category_ID": prods_list['Category_ID']}, 200
    else: 
        return "Resource Not Found", 404
    

# Get all products in specific category id
@app.route("/product/category/<ID>")
def get_category_products(ID):
    js = get_data()
    list_of_prods = []
    products = js[2]['data']
    for prod in products:
            prod_dict = {}
            for el in prod:
                prod_dict.update(el)
            if(prod_dict['Category_ID']== float(ID)):
                products = prod_dict
                list_of_prods.append(products)
    
    if(len(list_of_prods) != 0):
        return {"Products": list_of_prods}, 200
    else: 
        return "Resource Not Found", 404


@app.route("/cookingMethod")
def get_cooking_methods():
    js = get_data()
    cookingMethods = js[4]
    methods_dict = {}
    methods_list = {}
    if(request.args.get('id') == None):
        return cookingMethods, 200
    else:
        id = request.args.get('id')
        cookingMethods = cookingMethods['data']
        
        for method in cookingMethods:
            methods_dict = {}
            for el in method:
                methods_dict.update(el)
            if(methods_dict['ID']== float(id)):
                methods_list = methods_dict
                break
    if(len(methods_list) != 0):
        return methods_list, 200
    else: 
        return "Resource Not Found", 404


@app.route("/cookingTip")
def get_cooking_tips():
    js = get_data()
    cookingTips = js[3]
    tips_dict = {}
    tips_list = {}
    if(request.args.get('id') == None):
        return cookingTips, 200
    else:
        id = request.args.get('id')
        cookingTips = cookingTips['data']
        
        for tip in cookingTips:
            tips_dict = {}
            for el in tip:
                tips_dict.update(el)
            if(tips_dict['ID']== float(id)):
                tips_list = tips_dict
                break
    if(len(tips_list) != 0):
        return tips_list, 200
    else: 
        return "Resource Not Found", 404

if __name__ == '__main__':
    app.run(debug=False)