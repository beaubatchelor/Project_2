from flask import Flask, render_template, jsonify, request 
from flask_pymongo import PyMongo
from config import (mongo_name, mongo_pass)


app = Flask(__name__)

mongo = PyMongo(app, uri = f'mongodb://{mongo_name}:{mongo_pass}@ds249818.mlab.com:49818/heroku_6lctns1z') 

@app.route("/")
def index():
    # sales = mongo.heroku_6lctns1z.sales_data.find({},{'_id':False})
   # """Return the homepage."""
    return render_template("index.html")

@app.route("/scatter_b")
def scatter():

    return render_template("beau_page.html")

@app.route("/scatter_data")
def scatter_data():
    user_input = "Accessories".replace(" ", "_")
    line = mongo.db.line_graph.find_one({ f"{user_input}" : { "$exists" : True}}, {'_id': False})
    line_data = line[user_input]
    year2014 = line_data["2014"] 
    year2015 = line_data["2015"]
    year2016 = line_data["2016"]
    month_data = [year2014, year2015, year2016]
    return jsonify(month_data)

@app.route("/prod_by_city_m")
def prod_by_city():

    return render_template("prod_by_city.html")
@app.route("/table_s")
def table():

    return render_template("sai_page.html")

@app.route("/data")
def data():

    return render_template("sai_page.html")


if __name__ == "__main__":
    app.run(debug=True)
