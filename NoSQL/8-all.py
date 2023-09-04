#!/usr/bin/env python3
"""
Lists all documents in a collection
"""


def list_all(mongo_collection):
    """list all mongo collection
    
    Args : 
    
    mongo_collection (dictionnary) : Key:Value

    Return 
    List of all element in mongo_collection
    """
    return list(mongo_collection.find())
