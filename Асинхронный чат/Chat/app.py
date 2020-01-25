import asyncio
import aiohttp_jinja2
import aiohttp_debugtoolbar
import jinja2
from aiohttp_session import session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from aiohttp import web
from routes import routes
from middleware import authorize
from motor import motor_asyncio as ma
from settings import *
import hashlib


async def on_shutdown(app):
    for ws in app['websockets']:
        await ws.close(code = 1001,message = "Server shutdown.")

middle = [
    session_middleware(EncryptedCookieStorage(hashlib.sha256(bytes('lkjhgfdfghnjmk,l','utf-8')).digest())),
    authorize,
]
if DEBUG:
    middle.append(aiohttp_debugtoolbar.middleware)
app = web.Application(middlewares = middle)




aiohttp_jinja2.setup(app,loader= jinja2.FileSystemLoader('templates'))


for route in routes:
    app.router.add_route(route[0],route[1],route[2], name=route[3])
app['static_root_url'] = '/static'
app.router.add_static('/static','static',name= 'static')


app.client = ma.AsyncIOMotorClient(MONGO_HOST)
app.db = app.client[MONGO_DB_NAME]

app.on_cleanup.append(on_shutdown)
app['websockets']  = []

log.debug('Start server')
web.run_app(app)
log.debug('Stop server end')

