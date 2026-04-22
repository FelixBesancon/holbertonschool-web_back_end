#!/usr/bin/env python3
"""
Module that inserts a new document in a collection
based on kwargs and returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
