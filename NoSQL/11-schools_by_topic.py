#!/usr/bin/env python3
"""
Module that defines the function schools_by_topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have the specified topic.
    """
    return list(
        mongo_collection.find(
            {"topics": topic}
        )
    )
