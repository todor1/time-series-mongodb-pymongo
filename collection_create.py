from pymongo import errors

import db_client  # created above


def create_ts(name="rating_over_time"):
    """
    Create a new time series collection
    """
    client = db_client.get_db_client()
    db = client.business
    try:
        db.create_collection(
            name,
            timeseries={
                "timeField": "timestamp",
                "metaField": "metadata",
                "granularity": "seconds",
            },
        )
    except errors.CollectionInvalid as e:
        print(f"{e}. Continuing")


def drop(name="rating_over_time"):
    """
    Drop any given collection by name
    """
    client = db_client.get_db_client()
    db = client.business
    try:
        db.drop_collection(name)
    except errors.CollectionInvalid as e:
        print(f"Collection error:\n {e}")
        raise Exception("Cannot continue")
