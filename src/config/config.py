import os

SCRAPY_SETTINGS_MODULE = 'src.service.crawler.crawler.settings'
DEBUG = False
DATABASE_URI = os.environ['DATABASE_URI']
