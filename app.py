from flask import Flask,request
from db import stores,Items
import uuid

app = Flask(__name__)

# stores = [
#     {
#         "name":"ABC",
#         "Items":[
#             {
#                 "item_name":"laptop",
#                 "price" : 2500000
#             }
#         ]
#     }
# ]

@app.get('/stores')
def listStores():
    return {"response":list(stores.values())}

@app.post('/stores')
def addStores():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {**store_data,"id":store_id}
    stores[store_id] = new_store

    return { "message":"success","data":stores},200

@app.post('/items')
def addStoreItems(name):
    item_data = request.get_json()
    if item_data['storeId'] not in stores:
        return {"message":"store not found"},404
    item_id = uuid.uuid4().hex
    item = {**item_data,"id":item_id}
    Items[item_id] = item

    return item,200

# Previous code before UUID
# @app.post('/stores/<string:name>/Items')
# def addStoreItems(name):
#     request_data = request.get_json()
#     for item in stores
#         if item['name'] == name:
#             new_item = {"item_name":request_data["item_name"],"price":request_data["price"]}
#             item["Items"].append(new_item)
#             return {"message":"Successfully added items","data":stores},200

#     return { "message":"Invalid Name, Store not found"},404

@app.post('/stores/<string:store_id>')
def getIndivisdualStore(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message":"Invalid Name, Store not found"} 
    # Previous code before UUID
    # for item in stores:
    #     if item['name'] == name:
    #         return {"message":"Successfully added items","data":item},200

    # return { "message":"Invalid Name, Store not found"},404
