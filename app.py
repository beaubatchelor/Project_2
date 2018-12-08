from flask import Flask, render_template, jsonify
from config import mongo_name, mongo_pass 
from flask_pymongo import PyMongo


app = Flask(__name__)

# mongo = PyMongo(app, uri = f'mongodb://{mongo_name}:{mongo_pass}@ds249818.mlab.com:49818/heroku_6lctns1z')

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
    trace1 = {
           "x" : [0,1,2,3,4,5],
           "y" : [0,1,5,16,1,3],
           mode: 'lines'
        }
    trace2 = {
           "x" : [0,1,2,3,4,5],
           "y" : [0,9,20,4,3,2],
           mode: 'lines'
        }
    month_data = [trace1, trace2]
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
    app.run()
