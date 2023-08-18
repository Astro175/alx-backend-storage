#!/usr/bin/env python3

"""
  A Python module that lists all documents in a collection
"""

def list_all(mongo_collection):
    """
       a Python function that lists all
       documents in a collection
    """
    collection = []

    for doc in mongo_collection.find():
        collection.append(doc)
    return collection
