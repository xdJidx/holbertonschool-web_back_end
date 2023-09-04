#!/usr/bin/env python3
"""
Changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: A pymongo collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics approached in the school.

    Returns:
        None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
