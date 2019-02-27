from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/app"
mongo = PyMongo(app)

@app.route("/")
def index():
    # Find one record of data from the mongo database
    mars_info = mongo.db.mars_info.find_one()
    # Return template and data
    return render_template("index.html", mars_info=mars_info)

@app.route("/scrape")
def scraper():
    mars_info = mongo.db.mars_info
    mars_info_data = scrape_mars.scrape()
    mars_info.update({},mars_info_data, upsert = True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
    
