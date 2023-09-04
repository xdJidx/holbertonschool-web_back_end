#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    provides some stats about Nginx logs stored in MongoDB
    """
    # Connect to the MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the 'logs' database and 'nginx' collection
    db = client.logs
    collection = db.nginx

    # Get the total number of logs
    total_logs = collection.count_documents({})

    # Get the counts for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents(
        {"method": method}) for method in methods}

    # Get the count of logs with method=GET and path=/status
    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"})

    # Print the results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}:", method_counts[method])
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
