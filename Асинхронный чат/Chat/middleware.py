from aiohttp import web
from aiohttp.web import middleware
from aiohttp_session import get_session
from settings import *


@middleware
async def authorize(request,handler):
    def check_path(path):
        result = True
        for r in ['/login','/static/','/signin','/signout','/_bedugtoolbar/']:
            if path.startswith(r):
                result = False
        return result
    
    session = await get_session(request)
    if session.get('user'):
        return await handler(request)
    elif check_path(request.path):
        url = 'login' #request.app.router['login']
        raise web.HTTPFound(url)
        return handler(request.path)
    else:    
        return await handler(request)
    