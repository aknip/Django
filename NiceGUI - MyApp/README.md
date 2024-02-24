
docker-compose up
http://localhost

- This runs 'main.py'
- For execuitng a different .py-file use: APP=form-demo.py docker-compose up
- Single page app router (no reload) based on https://github.com/zauberzeug/nicegui/tree/main/examples/single_page_app 

# Open in gitpod.io:
https://gitpod.io/#https://github.com/aknip/Python-Webdev-Django-Streamsync


# Infos
- Browser hot reload => Change in .py file reloads browser automatically
- Works in Docker and locally
- Uses a customized Docker config for pip install etc.


# Run tests
- In second terminal: docker-compose exec nicegui bash
- pytest --disable-pytest-warnings

# Application architecture
- Single page app, routing is client side (see helper_functions.py and router_frame.js)
- router (link/new url) calls tabs.set_value('Home') to switch to new page
- ui/DOM element for single page app routing "router.frame()" needs to rendered (empty) to make the router work, see example https://github.com/zauberzeug/nicegui/tree/main/examples/single_page_app   
- URLs are 
    /
    /app1
    /settings
- Main navigation names (tabs) and URLs are defined in settings_data['main-nav']    
- main.py: Initializes everything: global settings, routing, logging, sourrounding HTML (header, footer...)
- app_home.py: Homepage, as separate .py file (alternative: page desing inside of main.py, see example 'App1', end of main.py)
- app_settings.py: Settings page
- helper_functions: functions for router, settings, logging
- settings.json (optional): persisted settings file

# Application flow
- init logging, setttings, routing
- navigation by click-events on tabs which call router-functions (not standard NiceGUI tab navigation!)  
    ui.tab('Home').on('click', lambda: router.open(show_home)) 
- router (link/new url) calls tabs.set_value('Home') to switch to new page
- logtexts are stored in app.storage.general
- settings_data (dict, defined inside main) for all application settings

# How to customize the app
- app_home.py: Can be deleted/replaced by other page => change router settings accordingly
- change texts of main navigation:
    - change texts in settings_data['main-nav'] , see helper_functions.py
- new page: 
    1. Add tab in settings_data['main-nav'] and new tab ui-element (main.py)
    2. Add router config in main.py 
    2. Add .py file (as for "HOME" and app_home.py)


