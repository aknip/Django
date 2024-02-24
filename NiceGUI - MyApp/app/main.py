from nicegui import app, ui
from nicegui.events import ValueChangeEventArguments
import json
import sys, os, shutil
from loguru import logger

from helper_functions import Router, show, init_logger, init_settings

from app_home import app_home
from app_app1 import app_app1
from app_settings import app_settings

# Global vars & settings
SETTINGS_FILE_PATH = '/app/settings.json' # needs to be global, is needed BEFORE loading settings_data
app.storage.general['global_logs'] = {'loguru': ''} # see https://nicegui.io/documentation/section_action_events#storage

# static files, eg. for css
app.add_static_files('/static', 'static')

@ui.page('/')  # normal index page (e.g. the entry point of the app)
@ui.page('/{_:path}')  # all other pages will be handled by the router but must be registered to also show the SPA index page


def main():
    # list of all 'global vars': vars scoped "global" and "main"
    global settings_file_path

    init_logger()

    settings_data = init_settings(SETTINGS_FILE_PATH)

    # single page router, see https://github.com/zauberzeug/nicegui/tree/main/examples/single_page_app
    router = Router()
    
    @router.add('/')
    def show_home():
        tabs.set_value(settings_data['main-nav'][0])  
        
        
    @router.add('/app1')
    def show_app1():
        tabs.set_value(settings_data['main-nav'][1]) # or: panels.set_value('App1')
        #ui.label('Content One').classes('text-2xl'). # change content of "router.frame()" => see below

    @router.add('/settings')
    def show_settings():
        tabs.set_value(settings_data['main-nav'][2])      
    
    # Add css file / styling    
    ui.add_head_html('<link rel="stylesheet" type="text/css" href="static/styles.css">')    

    #ui.dark_mode().enable()
    ui.colors(primary='#64748b')

    with ui.header().classes(replace='row items-center') as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
        with ui.tabs() as tabs:
            ui.tab(settings_data['main-nav'][0]).on('click', lambda: router.open(show_home)) 
            ui.tab(settings_data['main-nav'][1]).on('click', lambda: router.open(show_app1)) 
            ui.tab(settings_data['main-nav'][2]).on('click', lambda: router.open(show_settings)) 
         

    with ui.footer(value=False) as footer:
        ui.label('Footer')

    with ui.left_drawer().classes('bg-gray-100').props('width=300') as left_drawer:
        #ui.label('Side menu')
        ui.switch('Debug', value=True, on_change=show).bind_value(settings_data, 'debug_mode')
        with ui.column().bind_visibility_from(settings_data["debug_mode"], 'value'):
            with ui.tabs() as log_tabs:
                ui.tab('All logs')
                ui.tab('Main logs')
            with ui.tab_panels(log_tabs, value='All logs').classes('loguru_panel'): 
                with ui.tab_panel('All logs'):    
                    global_logs_display = ui.html().bind_content_from(app.storage.general['global_logs'], 'loguru').style('height: max(200px, 40vh); overflow-y: auto;')
                with ui.tab_panel('Main logs'):    
                    global_logs_display2 = ui.html().bind_content_from(app.storage.general['global_logs'], 'loguru').style('height: max(100px, 20vh); overflow-y: auto;')
        ui.slider(min=1, max=3)
        ui.toggle({1: 'A', 2: 'B', 3: 'C'})
        ui.number()

    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle, icon='contact_support').props('fab')

    # **************************************************************************
    # this places the content which should be displayed, see https://github.com/zauberzeug/nicegui/tree/main/examples/single_page_app 
    # not used in this app (content empty), but necessary for rendering (?)
    router.frame() 
    # **************************************************************************
    
    with ui.tab_panels(tabs, value=settings_data['main-nav'][0]).classes('w-full'): # default Tab is 'Marketing'
        with ui.tab_panel(settings_data['main-nav'][0]):
            app_home(ui, settings_data)

        with ui.tab_panel(settings_data['main-nav'][1]):
            ui.label('App1: wget') 
            app_app1(ui, settings_data)

        with ui.tab_panel(settings_data['main-nav'][2]):
            app_settings(ui, settings_data)
           
ui.run()