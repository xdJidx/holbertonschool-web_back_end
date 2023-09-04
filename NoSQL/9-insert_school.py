#!/usr/bin/env python3
"""
inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection based on kwargs.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: Key-value pairs representing the document attributes.

    Returns:
        The new _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
