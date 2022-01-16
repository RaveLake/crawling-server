import os

from src.util.network import get_local_domain

SCRAPY_SETTINGS_MODULE = 'src.service.crawler.crawler.settings'
DEBUG = False
DATABASE_URI = os.environ['DATABASE_URI']
LOCAL_DOMAIN = get_local_domain()
