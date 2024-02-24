import json
from loguru import logger
from nicegui import app, ui
from helper_functions import show

from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
import sys, os, shutil
import asyncio
import atexit
from datetime import datetime

def app_home(ui, settings_data):
    ui.label('Download data')
    ui.button('Start Scraper', on_click = lambda: runScraper(settings_data))


async def runScraper(settings_data):
    async with async_playwright() as p:
        logger.info("Scraping started")
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()
        #launch browserstack demo
        await page.goto("https://bstackdemo.com")
        logger.info('Title of page is: ' + await page.title())
        #await page.screenshot(path=proj_folder + "/screenshot.png")
        await my_screenshot(page, 'Screenshot Demopage')
        await browser.close()
        logger.info("Scraping finished")



# Create screenshot and log ("INFO")
async def my_screenshot(my_page, message):
    current_date_string = datetime.now().strftime("%Y%m%d-%H%M%S")
    shotfile = current_date_string + '-' + message + ".png"
    shotfile = "".join( x for x in shotfile.replace(' ', '_') if (x.isalnum() or x in "._-")) # cleanup filename
    await my_page.screenshot(path= "/app/" + shotfile)
    logger.info("Screenshot done: " + shotfile)




# SYNC version - WEG !!!!!!!!
def hello_world1():    
    playwright = sync_playwright().start()
    browser = p.chromium.launch()
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    #launch browserstack demo
    page.goto("https://bstackdemo.com")
    logger.info('Title of page is: ' + page.title())
    #await page.screenshot(path=proj_folder + "/screenshot.png")
    my_screenshot(page, 'Screenshot Demopage')
    browser.close()    