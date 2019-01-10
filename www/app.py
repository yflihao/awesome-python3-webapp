import logging; logging.basicConfig(level=logging.INFO)

from aiohttp import web

from settings import config
from routes import setup_routes

app = web.Application()
setup_routes(app)
app['config'] = config
web.run_app(app, host=app['config']['postgres']['host'], port=int(app['config']['postgres']['port']))