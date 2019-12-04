from pymongo import MongoClient


def connect():
    mongo_url = "mongodb://127.0.0.1:27017"
    client = MongoClient(mongo_url)
    db = client.coffee

    # collections for waiter
    collection_open_order = db.open_order
    collection_acting_order = db.acting_order
    collection_close_order = db.close_order

    # collections for guest
    collection_order = db.order

    for collection in collection_order.find({}):
        print(collection)


connect()

