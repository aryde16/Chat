from aiohttp import web
from aiohttp_session import get_session
import aiohttp_jinja2


class Login(web.View):
    @aiohttp_jinja2.template('auth/login.html')
    async def get(self):
        session = await get_session(self.request)
        if session.get('user'):
            url =  request.app.router['main'].url()
            raise web.HTTPFound(url)
        return "Please enter login and password."
    