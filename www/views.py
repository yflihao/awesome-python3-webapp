from aiohttp import web

async def index(request):
    return web.Response(body=b'<h1>Python Web App</h1>', content_type='text/html')