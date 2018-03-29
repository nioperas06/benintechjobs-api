from .settings import *
import dj_database_url

ALLOWED_HOSTS += ['benintechjobs-api.herokuapp.com']

DEBUG = False

SECRET_KEY = '$jz&q54#+1kxfo927x_u-o*2qmqk=3@&n(arz!m4#u0dy&c=z0'

DATABASES['default'] = dj_database_url.config(default='postgres://ueuxlbahahfzde:d834461fb36d394d713ae5e973f85d68035dd078e7a731e0ae62331de0554be6@ec2-54-235-109-37.compute-1.amazonaws.com:5432/d80ft02v463v9l')
