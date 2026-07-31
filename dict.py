mobile = {
    "productname": "iphone",
    "version": 12,
    "price": 120000.0000,
    "is_true": True,
    "phonelist": ["samsung", "motorolla", "vivo"],
    "phonepricelist": (75000, 55000, 25000),
    "phoneidnumber": {3, 5, 9},
    "result": None
}

print(mobile)
# print(mobile["version"])
# print(mobile.get("productname"))
# print(mobile.keys())
# print(mobile.values())
mobile["colour"] = "blue"
print(mobile)
del mobile["result"]
print(mobile)
