# FoodKeeper API

Python (Flask) API for USDA FSIS FoodKeeper data (<https://www.fsis.usda.gov/shared/data/EN/foodkeeper.json>)


### About the Project
In Spring 2022, I participated in creating an API to access Foodkeeper data in Javascript. The goal was to then deploy using AWS and Kubernetes so the Libre Food Pantry network could use it for food storage information, but the project hit many roadbumps and not all goals were completed.

This project and my contributions can be found at <https://gitlab.com/LibreFoodPantry/common-services/foodkeeper>.

I am learning Flask and thought rebuilding this API end-to-end would be a good project. This is the result of that work.

I plan future work, such as creating a front-end interface for retrieving data.


### Application Download and Build
```
$ git clone https://github.com/ctshadis/fsis-foodkeeper-api.git fsis-foodkeeper-api
$ cd fsis-foodkeeper-api

If in Bash (Windows):
$ . env/Scripts/activate
$ python main.py

If in Command Prompt (Windows):
>env\Scripts\activate.bat
>python main.py

Navigate to localhost:5000/ and the application should be running.
```
# FoodKeeper Backend

Foodkeeper data from the FSIS accessible through a Python Flask API.


## REST API Endpoints

| Method | Endpoint  | Return | Note |
| -----  | --------- | ------ | ---- |
| GET   | /products | | Returns list of all products |
| GET    | /products/*id* | {<br>"id": *id*, "name": *"name"*, "subtitle": *"subtitle"*, "keywords": *"keywords"*, <br>"pantryLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"pantryAfterOpeningLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"refrigeratorLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"refrigrateAfterOpeningLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"refrigerateAfterThawingLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"freezerLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"dop_pantryLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"dop_refrigeratorLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"dop_freezerLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*} <br>} | Returns product with given id |
| GET   | /products/*id*/name |  *{"Name": name}* | Returns name for this product id |
| GET   | /products/category/*categoryId* | | Returns all products with the given category id |
| GET   | /categories | | Returns list of all categories |
| GET   | /categories/*id* | {"id": *id*, "name": *"name"*, "subcategory": *"subcategory"*} | Returns category with given id |
| GET   | /cookingMethods | | Returns list of all cooking methods |
| GET   | /cookingMethods/*id* | {"id": *id*, "method": *"method"*, "measureFrom": *measureFrom*, "measureTo": *measureTo*, "sizeMetric": *"sizeMetric"*, "cookingTemp", *"cookingTemp"*, "timingFrom": *timingfrom*, "timingTo": *timingTo*, "timingMetric": *"timingMetric"*, "timingPer": *"timingPer"*, "productId": *productId*} | Returns cooking method with given id |
| GET   | /cookingTips | | Returns list of all cooking tips |
| GET   | /cookingTips/*id* | {"id": *id*, "tips": *"tips"*, "safeMinTemp": *safeMinTemp*, "restTime": *restTime*, "restTimeMetric": *"restTimeMetric"*} | Returns cooking tip with given id |


### Querying API

| Method | Endpoint | Sample HTTP Call |
| -----  | --------- | ------ |
| GET | category | GET http://127.0.0.1:5000/category HTTP/1.1|
| GET | category/:id | GET http://127.0.0.1:5000/category?id=1 HTTP/1.1|
| GET | product | GET http://127.0.0.1:5000/product HTTP/1.1|
| GET | product/:id | GET http://127.0.0.1:5000/product?id=1 HTTP/1.1|
| GET | product/:name | GET http://127.0.0.1:5000/product?name=dips HTTP/1.1|
| GET | cookingMethod | GET http://127.0.0.1:5000/cookingMethod HTTP/1.1|
| GET | cookingMethod/:id | GET http://127.0.0.1:5000/cookingMethod?id=1 HTTP/1.1|
| GET | cookingTip | GET http://127.0.0.1:5000/category HTTP/1.1|
| GET | cookingTip/:id | GET http://127.0.0.1:5000/cookingTip?id=1 HTTP/1.1|


### Class Representation of Food Keeper Data

1. Category
	* ID: Integer
	* Category_Name: String
	* Subcategory_Name: String
2. Product
	* ID: Integer (of Product)
	* Category_ID: Integer (related to Category)
	* Name: String
	* Name_subtitle: String
	* Keywords: String
	* Pantry_Min: Integer (These can be null)
	* Pantry_Max: Integer
	* Pantry_Metric: String 
		* (Days, Weeks, Months, When Ripe, Indefinitely, Not Recommended)
	* Pantry_tips: String
	* DOP\_Pantry_Min: Integer
	* DOP\_Pantry_Max: Integer
	* DOP\_Pantry_Metric: String
		* (Days, Weeks, Months, When Ripe, Indefinitely, Not Recommended)
	* DOP\_Pantry_tips: String
	* Pantry\_After\_Opening_Min: Integer
	* Pantry\_After\_Opening_Max: Integer
	* Pantry\_After\_Opening_Metric: String
		* (Days, Weeks, Months, When Ripe, Indefinitely, Not Recommended)
	* Refrigerate_Min: Integer
	* Refrigerate_Max: Integer
	* Refrigerate_Metric: String
		* (Days, Weeks, Months, When Ripe, Indefinitely, Not Recommended)
	* Refrigerate_tips: String
	* DOP\_Refrigerate_Min: Integer
	* DOP\_Refrigerate_Max: Integer
	* DOP\_Refrigerate_Metric: String
		* (Days, Weeks, Months, When Ripe, Indefinitely, Not Recommended)
	* DOP\_Refrigerate_tips: String
	* Refrigerate\_After\_Opening_Min: Integer
	* Refrigerate\_After\_Opening_Max: Integer
	* Refrigerate\_After\_Opening_Metric: String
		* (Days, Weeks, Months, When Ripe, Indefinitely, Not Recommended, Package use-by date)
	* Refrigerate\_After\_Thawing_Min: Integer
	* Refrigerate\_After\_Thawing_Max: Integer
	* Refrigerate\_After\_Thawing_Metric: String
		* (Days, Weeks, Months, When Ripe, Indefinitely, Not Recommended)
	* Freeze_Min: Integer
	* Freeze_Max: Integer
	* Freeze_Metric: String
		* (Days, Weeks, Months, When Ripe, Indefinitely, Not Recommended)
	* Freeze_Tips: String
	* DOP\_Freeze_Min: Integer
	* DOP\_Freeze_Max: Integer 
	* DOP\_Freeze_Metric: String
		* (Days, Weeks, Months, When Ripe, Indefinitely, Not Recommended)
	* DOP\_Freeze_Tips: String
3. CookingTip
	* ID: Integer
	* Product_ID: Integer
	* Tips: String
	* Safe\_Minimum_temperature: Integer
	* Rest_Time: Integer
	* Rest\_Time_metric: String
4. CookingMethod
	* ID: Integer
	* Product_ID: Integer
	* Cooking_Method: String (e.g. Skillet or Oven, etc.)
	* Measure_from: Decimal
	* Measure_to: Decimal
	* Size_metric: String
		* Pounds, Ounces, Inches
	* Cooking_Temperature: String
	* Timing_from: Decimal
	* Timing_to: Decimal
	* Timing_metric: String
		* Hours, Minutes, Seconds
	* Timing_per: String
		* Pound, Ounce, Inch



---
Copyright &copy; 2022 Christian Shadis. This work is licensed
under the Creative Commons Attribution-ShareAlike 4.0 International License.
To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/4.0/.
