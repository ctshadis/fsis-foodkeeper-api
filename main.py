from fastapi import Body, FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello world"}

@app.get("/category")
def get_categories():
    return {"category": "something"}

# TODO /products/:id

@app.get("/product")
def get_products():
    return {"product": "something"}

# TODO /products/:id/name

@app.get("/product/category")
def get_product_category():
    return {"product": "something",
            "category": "vagueries"}

# TODO /product/category/:id

@app.post("/category")
def create_category(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"Category: {payLoad['category']}, Subcategory: {payLoad['subcategory']}, Name: {payLoad['name']}"}


# TODO /category/:id


@app.get("/cookingMethod")
def get_cooking_method():
    return {"cooking method": "cook it"}

# TODO /cookingMethod/:id


@app.get("/cookingTip")
def get_cooking_tip():
    return {"cooking tip": "cook it more"}
    
# TODO /cookingTip/:id

