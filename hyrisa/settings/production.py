# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['hyrisa.perimetro20.com', '138.197.202.211']

STATIC_ROOT = os.path.join(BASE_DIR, "../static/")