# incomplete on purpose - check `final` branch

from pymongo import errors


# fix local imports
# import db_client


def create_ts(name="rating_over_time"):
    """
    Create a new time series collection
    """
    # 1. get a mongodb client
    # 2. get a mongodb database
    try:
        # 3. create a collection
        pass
    except errors.CollectionInvalid as e:
        print(f"{e}. Continuing")


def drop(name="rating_over_time"):
    """
    Drop any given collection by name
    """
    # 1. get a mongodb client
    # 2. get a mongodb database
    try:
        # 3. Drop a collection
        pass
    except errors.CollectionInvalid as e:
        print(f"Collection error:\n {e}")
        raise Exception("Cannot continue")
