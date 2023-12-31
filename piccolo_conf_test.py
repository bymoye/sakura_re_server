import os
from piccolo_conf import *  # noqa

DB = PostgresEngine(  # noqa
    config={
        "database": os.environ.get("PG_DATABASE", "test"),
        "user": os.environ.get("PG_USER", "postgres"),
        "password": os.environ.get("PG_PASSWORD", "postgres"),
        "host": os.environ.get("PG_HOST", "localhost"),
        "port": int(os.environ.get("PG_PORT", "5432")),
    }
)
