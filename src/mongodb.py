from pymongo import MongoClient


def connect():
    mongo_url = "mongodb://127.0.0.1:27017"
    client = MongoClient(mongo_url)
    db = client.coffee

    # collections for waiter
    collection_open_order = db.open_order
    collection_acting_order = db.acting_order
    collection_close_order = db.close_order
    information_about = db.information_about
    # collections for guest
    # collection_order = db.order

    data = {
        "donut": "information about donut",
        "tiramisu": "information about tiramisu",
        "muffin": "information about muffin",
        "cheesecake": "information about cheesecake",
        "croissant": "information about croissant",
        "tea": "information about tea",
        "ruf": "information about ruf",
        "latte": "information about latte",
        "cappucino": "information about cappucino",
        "espresso": "information about espresso",
    }

    #information_about.insert_one(data)

    for collection in information_about.find({}):
        print(collection)
    
    for document in information_about

    #print(db.collection_names({}))
    #db.information_about.drop()


connect()

