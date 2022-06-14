# FoodKeeper API

API for USDA FSIS FoodKeeper data (<https://www.fsis.usda.gov/shared/data/EN/foodkeeper.json>)


### Application Download and Build
```
$ git clone https://gitlab.com/LibreFoodPantry/FoodKeeper-API.git
$ cd FoodKeeper-API

$ ./gradlew build
$ ./gradlew bootrun

Navigate to localhost:8080/ and the application should be running.
```
# FoodKeeper Backend

Project hosting for the refactoring of the FoodKeeper API Backend in Javascript.

### Application Download and Build
To avoid dependency conflicts across projects, and to reduce variance
between development platforms, we use VS Code devcontainers.

New to VS Code devcontainers? Start here
https://code.visualstudio.com/docs/remote/containers 
and follow its installation instructions. Be sure to install and
configure Git too.

Now download, install, and run this project and its devcontainer as
follows.

1. Navigate to this project on GitLab and select
    `Clone -> Open in your IDE -> Visual Studio Code (HTTPS)`.
2. Select location to store the project.
3. Select "Reopen in container" when option is provided.


### Prepare Enviorment

- cd into src: `cd src`
- Install node packages: `npm i`

### Run Server in Docker

- Start Development Docker Container: `npm run docker-dev`
- Start Production Docker: `npm run docker`

### Updating Bundle Process

Paste Open API Bundle into /lib
rename file to openapi.yaml

### 1.2. Prepare envionment 

```
bin/down.sh
bin/up.sh
```

### 1.3. Rebuild and Test

```
bin/retest.sh
```




## REST API Endpoints

| Method | Endpoint  | Body  | Return | Note |
| -----  | --------- | ----- | ------ | ---- |
| GET   | /products | | | Returns list of all products |
| GET    | /products/*id* | | {<br>"id": *id*, "name": *"name"*, "subtitle": *"subtitle"*, "keywords": *"keywords"*, <br>"pantryLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"pantryAfterOpeningLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"refrigeratorLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"refrigrateAfterOpeningLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"refrigerateAfterThawingLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"freezerLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"dop_pantryLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"dop_refrigeratorLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*}, <br>"dop_freezerLife": {"min": *min*, "max": *max*, "metric": *"metric"*, "tips": *"tips"*} <br>} | Returns product with given id |
| GET   | /products/*id*/name | | *name* | Returns name for this product id |
| GET   | /products/category/*categoryId* | | | Returns all products with the given category id |
| GET   | /categories | | | Returns list of all categories |
| GET   | /categories/*id* | | {"id": *id*, "name": *"name"*, "subcategory": *"subcategory"*} | Returns category with given id |
| GET   | /cookingMethods | | | Returns list of all cooking methods |
| GET   | /cookingMethods/*id* | | {"id": *id*, "method": *"method"*, "measureFrom": *measureFrom*, "measureTo": *measureTo*, "sizeMetric": *"sizeMetric"*, "cookingTemp", *"cookingTemp"*, "timingFrom": *timingfrom*, "timingTo": *timingTo*, "timingMetric": *"timingMetric"*, "timingPer": *"timingPer"*, "productId": *productId*} | Returns cooking method with given id |
| GET   | /cookingTips | | | Returns list of all cooking tips |
| GET   | /cookingTips/*id* | | {"id": *id*, "tips": *"tips"*, "safeMinTemp": *safeMinTemp*, "restTime": *restTime*, "restTimeMetric": *"restTimeMetric"*} | Returns cooking tip with given id |


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
