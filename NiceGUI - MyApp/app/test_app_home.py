import pytest
import asyncio
import sys
from loguru import logger
import logging.handlers as handlers

import app_home
from helper_functions import init_settings

# pip install pytest pytest-asyncio

# GLoabal vars
SETTINGS_FILE_PATH = '/app/settings.json' # needs to be global, is needed BEFORE loading settings_data
settings_data = init_settings(SETTINGS_FILE_PATH)

# setup logging
pytest_plugins = ('pytest_asyncio',)
logger.remove()  # Remove all handlers added so far, including the default one.
logger.add(sys.stderr, level="TRACE", format="{time:HH:mm:ss} | <level>{level: <10}</level> | {message}")
logger.add('.' + "/log_all.log", level="TRACE", format="{time:HH:mm:ss} | {level: <10} | {message}")
#logger.add(handlers.RotatingFileHandler(filename="./log_all.log", mode='a', backupCount=5, maxBytes=1000, encoding="utf-8", delay=True), level="TRACE", format="{time:HH:mm:ss} | {level: <10} | {message}", enqueue=True, backtrace=True)
#logger.add(handlers.TimedRotatingFileHandler(filename="./log_all.log", when="s", interval=5, backupCount=5, delay=False), level="TRACE", format="{time:HH:mm:ss} | {level: <10} | {message}", enqueue=True, backtrace=True)

def inc(x):
    print('inc')
    return x + 1

def test_answer():
    assert inc(3) == 4

@pytest.mark.asyncio
async def test_screenshot():
    #logger.info("Start scraping test")
    await app_home.runScraper(settings_data)
    #logger.info("Finished scraping test")
