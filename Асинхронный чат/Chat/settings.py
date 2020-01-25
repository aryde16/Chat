from os.path import isfile
from envparse import env
import logging


log = logging.getLogger("app")
log.setLevel(logging.DEBUG)

f = logging.Formatter('[L:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',datefmt= '%d-%m-%Y %H:%M:%S')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(f)
log.addHandler(ch)

if isfile('.evn'):
    env.read_evnfile('.evn')

DEBUG = env.bool('DEBUG', default = False)

SITE_HOST = env.str('HOST', default = False)
SITE_PORT = env.int('PORT', default = False)
SECRET_KEY = env.str('SECRET_KEY',default = False)
MONGO_HOST = env.str('MONGO_HOST', default = 'localhost:27017')
MONGO_DB_NAME = env.str('MONGO_DB_NAME',default = 'chat_test')

MESSAGES = 'messages'
USER_COLLECTION = 'users'
