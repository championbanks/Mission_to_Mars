from flask import Flask, render_template, redirect
import pymongo
from scrape_mars  import scraper

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars
collection = db.mars
    
@app.route('/')
def index():
    # Store the entire team collection in a list
    # mars = list(collection.find({}))[-1]
    mars = collection.find_one()
    print(mars)
    print(client.list_database_names())
    print(db.list_collection_names)
    print(db.list_collection_names())
    print(list(collection.find()))
    print(collection.news_title)

    # Return the template with the teams list passed in
    return render_template('index.html', mars=mars)
    
    
@app.route('/scrape')
def scrape():

    data = scraper()

    collection.update({}, data, upsert=True)

    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)