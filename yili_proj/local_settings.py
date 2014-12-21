
# -*- coding: utf-8 -*-
import os
from settings import BASE_DIR

default_db = {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db3.sqlite3'),
     }


HOST_NAME = "http://127.0.0.1:8000"
