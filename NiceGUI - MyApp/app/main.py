from nicegui import ui
from nicegui.events import ValueChangeEventArguments
import json
import sys, os, shutil
from loguru import logger

# Global settings


# app.storage.general['my_var'] = app.storage.general['my_var'] + 1
# see https://nicegui.io/documentation/section_action_events#storage
settings_file_path = '/app/settings.json'
settings_data = {}
global_logs = {'loguru': ''}

# Logger

logger.remove()  # Remove all handlers added so far, including the default one.

# custom function as log handler - will be executed with every log call
def custom_function(msg):
  print('yoyo')
  msg_obj = json.loads(msg)
  message = msg_obj['record']['message'] #print(msg_obj['text'])
  level = msg_obj['record']['level']['name']
  #print('+++ FROM LOGGER: ' + message)
  global_logs['loguru'] = '<li class="log_loguru">' + msg_obj['text'] + '</li>' + global_logs['loguru']
logger.add(custom_function, level="TRACE", format="{time:HH:mm:ss} | {level: <10} | {message}", serialize=True)
logger.add(sys.stderr, level="TRACE", format="{time:HH:mm:ss} | {level: <10} | {message}")


#logger.trace("A trace message.")
#logger.debug("A debug message.")
logger.info("An info message.")
#logger.success("A success message.")
#logger.warning("A warning message.")
#logger.error("An error message.")
#logger.critical("A critical message.")


# Check for saved settings
if os.path.exists(settings_file_path):
    print('Settings file found:')
    f= open(settings_file_path,'r')
    contents =f.read()
    f.close()
    settings_data = json.loads(contents)
    print(settings_data)
else:
    print('Settings file not found, using defaults:')
    settings_data = {
        'name': 'Bob', 
        'age': 17,
        'OpenAI-Key': 'sk-1234'
    }
    print(settings_data)

#ui.dark_mode().enable()
ui.colors(primary='#64748b')


ui.add_head_html('''
    <style>
        header {
            padding-left: 15vw!important;
            height: 88px;
            padding-top: 40px;
        }
        aside {
            margin-left: 15vw!important
        }
        .q-page {
            margin-left: 15vw!important
        }
        .log_loguru {
            padding-left: 15px;
            text-indent: -15px;
        }
        .loguru_panel {
            background-color: transparent!important
        }
    </style>
''')

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

def runCyberApp():
    cyber_result1.text = 'Lorem ipsum dolor sit amet,' + global_logs['loguru'] + json.dumps(settings_data, sort_keys=False, indent=2)
    cyber_result2.value = 'Button was clicked'

def getSettingsAsText():
    settings_as_Text.value = json.dumps(settings_data, sort_keys=False, indent=2)
    logger.info("Get settings clicked. Some more text to check the log length.")

def saveSettings():
    f=open(settings_file_path,'w+')
    f.write(json.dumps(settings_data, sort_keys=False, indent=2))
    f.close()
    logger.info("Settings saved.")


def appMarketing(ui):
    ui.button('Button', on_click=lambda: ui.notify('Click'))
    with ui.row():
        ui.checkbox('Checkbox', on_change=show)
        ui.switch('Switch', on_change=show)
    ui.radio(['A', 'B', 'C'], value='A', on_change=show).props('inline')
    with ui.row():
        ui.input('Text input', on_change=show)
        ui.select(['One', 'Two'], value='One', on_change=show)
    ui.link('And many more...', '/documentation').classes('mt-8')


with ui.header().classes(replace='row items-center') as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    with ui.tabs() as tabs:
        ui.tab('Marketing')
        ui.tab('Cyber')
        ui.tab('AI Assistant')
        ui.tab('Settings')

with ui.footer(value=False) as footer:
    ui.label('Footer')

with ui.left_drawer().classes('bg-gray-100').props('width=300') as left_drawer:
    #ui.label('Side menu')
    debug_mode = ui.switch('Debug', value=True, on_change=show)
    with ui.column().bind_visibility_from(debug_mode, 'value'):
        with ui.tabs() as log_tabs:
            ui.tab('All logs')
            ui.tab('Main logs')
        with ui.tab_panels(log_tabs, value='All logs').classes('loguru_panel'): 
            with ui.tab_panel('All logs'):    
                global_logs_display = ui.html().bind_content_from(global_logs, 'loguru').style('height: max(200px, 40vh); overflow-y: auto;')
                #global_logs_display = ui.label().classes('text-l').bind_text_from(global_logs, 'loguru').style('height: max(200px, 40vh)')
                #global_logs_display2 = ui.textarea('Log:').bind_value(global_logs, 'loguru').style('height: max(200px, 40vh)')
            with ui.tab_panel('Main logs'):    
                global_logs_display2 = ui.html().bind_content_from(global_logs, 'loguru').style('height: max(100px, 20vh); overflow-y: auto;')
    ui.slider(min=1, max=3)
    ui.toggle({1: 'A', 2: 'B', 3: 'C'})
    ui.number()

with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
    ui.button(on_click=footer.toggle, icon='contact_support').props('fab')

with ui.tab_panels(tabs, value='Cyber').classes('w-full'): # default Tab is 'Marketing'
    with ui.tab_panel('Marketing'):
        appMarketing(ui)

    with ui.tab_panel('Cyber'):

        ui.label().bind_text_from(settings_data, 'name', backward=lambda n: f'Name: {n}')
        ui.label().bind_text_from(settings_data, 'age', backward=lambda a: f'Age: {a}')
        ui.button('Turn 18', on_click=lambda: settings_data.update(age=18))


        ui.label('Logging...').bind_visibility_from(debug_mode, 'value')
        ui.input('Text input', on_change=show).bind_visibility_from(debug_mode, 'value')
        ui.input('Text input', on_change=show).bind_visibility_from(debug_mode, 'value')


        ui.button('Run CyberApp', on_click=runCyberApp)

        ui.label('Here comes result text 1:')
        cyber_result1 = ui.label().classes('text-l')
        cyber_result2 = ui.input('Result text 2')













    with ui.tab_panel('AI Assistant'):
        ui.label('Content of AI Assistant')
    with ui.tab_panel('Settings'):
        ui.label('Content of Settings')   
        ui.input('OpenAI-Key', on_change=show).bind_value(settings_data, 'OpenAI-Key')
        ui.input('Text input', on_change=show)
        more_settings_visible = ui.switch('More Settings', value=False, on_change=show)
        with ui.column().bind_visibility_from(more_settings_visible, 'value'):
            ui.button('Show all setttings', on_click=getSettingsAsText)
            settings_as_Text = ui.textarea('Settings:')
            ui.button('Save setttings', on_click=saveSettings)
           


ui.run()






from nicegui import ui
from nicegui.events import ValueChangeEventArguments





