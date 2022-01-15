import functools
import sqlalchemy.exc
from fastapi import status, HTTPException


def catch_db_exceptions(function):
    """A general decorator function"""

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except sqlalchemy.exc.IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="The request violates constraint integrity. "
                                       "It can be: existence of a resource with the same properties, "
                                       "check constraint violation, null value.")
        except sqlalchemy.exc.DatabaseError:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="An error occurred, but it's our fault. Sorry!")
        return result

    return wrapper
