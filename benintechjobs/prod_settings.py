from .settings import *
import dj_database_url

ALLOWED_HOSTS += ['benintechjobs-api.herokuapp.com']

DEBUG = False

SECRET_KEY = '$jz&q54#+1kxfo927x_u-o*2qmqk=3@&n(arz!m4#u0dy&c=z0'

DATABASES['default'] = dj_database_url.config(default='postgres://spzkaskyeltuxx:f97d829558c33071384a873a1df772de0ea2d55356a64da5f976e4aeecbb83c5@ec2-23-21-121-220.compute-1.amazonaws.com:5432/d24gsbaho305ck')
