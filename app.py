from flask import Flask,request

app = Flask(__name__)

stores = [
    {
        "name":"ABC",
        "Items":[
            {
                "item_name":"laptop",
                "price" : 2500000
            }
        ]
    }
]

@app.get('/stores')
def listStores():
    return {"response":stores}

@app.post('/stores')
def addStores():
    request_data = request.get_json()
    new_store = { "name":request_data["name"],"Items":[]}
    stores.append(new_store)

    return { "message":"success","data":stores},200

@app.post('/stores/<string:name>/Items')
def addStoreItems(name):
    request_data = request.get_json()
    for item in stores:
        if item['name'] == name:
            new_item = {"item_name":request_data["item_name"],"price":request_data["price"]}
            item["Items"].append(new_item)
            return {"message":"Successfully added items","data":stores},200

    return { "message":"Invalid Name, Store not found"},404