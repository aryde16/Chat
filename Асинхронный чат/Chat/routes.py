from chat.views import ChatList, WebSocket
from auth.views import Login,SingIn,SingOut

routes = [
    ('GET','/',         ChatList,   'main'),
    ('GET','/ws',       WebSocket,  'chat'),
    ('*',  '/login'     Login,      'login'),
    ('*',  '/singin'    SingIn,     'singin'),
    ('*','/singout'     SingOut,    'singout'),
]