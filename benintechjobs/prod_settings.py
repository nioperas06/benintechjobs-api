from .settings import *
import dj_database_url

ALLOWED_HOSTS += ['benintechjobs-api.herokuapp.com']

DEBUG = False

SECRET_KEY = '$jz&q54#+1kxfo927x_u-o*2qmqk=3@&n(arz!m4#u0dy&c=z0'

DATABASES['default'] = dj_database_url.config(default='postgres://oclwlticjzoqnt:1394f86a64e63aef27b9c3768b0957af952ee5ff120ef1d047103b1d6d18b827@ec2-23-21-121-220.compute-1.amazonaws.com:5432/datvsjjaf1bp76')
