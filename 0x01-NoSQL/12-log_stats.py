#!/usr/bin/env python3

"""
  A Python script that provides some stats
  about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
nginx_collection = client.logs.nginx

total_doc = nginx_collection.count_documents({})
print("{} logs".format(total_doc))

list_method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")
for method in list_method:
    count = nginx_collection.count_documents(
            {"method": method})
    print("\t method {}: {}".format(method, count))
query = {"method": "GET", "path": "/status"}
count_status = nginx_collection.count_documents(query)
print("{} status check".format(count_status))
