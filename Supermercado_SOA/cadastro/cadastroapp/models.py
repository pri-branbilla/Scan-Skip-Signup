from __future__ import unicode_literals

from django.db import models
from mongoengine import connect

connect(
    name='admin',
     username='admin',
     password='admin123',
     host='mongodb://admin:qwerty@localhost/27017'
)
# Create your models here.

