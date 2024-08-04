import json
def conversion(dic):
    convert1=json.dumps(dic)
    print("Converted to JSON: ",convert1)
    convert2=json.loads(convert1)
    print("Converted Back: ", convert2)
dic='{"name": "Alice", "age": 30, "city": "Wonderland"}'
conversion(dic)