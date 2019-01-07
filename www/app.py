import logging; logging.basicConfig(level=logging.INFO)

from aiohttp import web

async def index(request):
    return web.Response(body=b'<h1>Python Web App</h1>', content_type='text/html')

app = web.Application()
app.add_routes([web.get('/', index)])
web.run_app(app)