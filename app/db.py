from blacksheep import Application
from piccolo.engine import engine_finder


def configure_db(app: Application):
    async def open_database_connection_pool(application: Application):
        try:
            engine = engine_finder()
            if engine is None:
                raise Exception("No engine found")
            await engine.start_connection_pool()
        except Exception:
            print("Unable to connect to the database")

    async def close_database_connection_pool(application: Application):
        try:
            engine = engine_finder()
            if engine is None:
                raise Exception("No engine found")
            await engine.close_connection_pool()
        except Exception:
            print("Unable to connect to the database")

    app.on_start += open_database_connection_pool
    app.on_stop += close_database_connection_pool
