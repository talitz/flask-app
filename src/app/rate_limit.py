import logging

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


def create_limiter(app):
    try:
        limiter_ret = Limiter(
            app=app,
            key_func=get_remote_address,
            default_limits=["200 per day", "50 per hour"]
        )
        return limiter_ret
    except Exception as e:
        logging.getLogger().error("An exception occurred while creating limiter object", repr(e))
