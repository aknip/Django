import json
from loguru import logger
from nicegui import app, ui
from helper_functions import show



def app_home(ui, settings_data):
    ui.label().bind_text_from(settings_data, 'name', backward=lambda n: f'Name: {n}')
    ui.label().bind_text_from(settings_data, 'age', backward=lambda a: f'Age: {a}')
    ui.button('Turn 18', on_click=lambda: settings_data.update(age=settings_data['age']+1))


    ui.label('Logging...').bind_visibility_from(settings_data, 'debug_mode')
    ui.input('Text input', on_change=show).bind_visibility_from(settings_data, 'debug_mode') # 'Text input', on_change=show
    ui.input('Text input', on_change=show).bind_visibility_from(settings_data, 'debug_mode')


    ui.button('Run Serverside Function', on_click = lambda: runDemoFunction(settings_data, ui_cyber_result1, ui_cyber_result2))

    ui.label('Here comes result text 1:')
    ui_cyber_result1 = ui.label().classes('text-l')
    ui_cyber_result2 = ui.input('Result text 2')


def runDemoFunction(settings_data, ui_cyber_result1, ui_cyber_result2):
    ui_cyber_result1.text = 'Lorem ipsum dolor sit amet,' + app.storage.general['global_logs']['loguru']  + json.dumps(settings_data, sort_keys=False, indent=2)
    ui_cyber_result2.value = 'Button was clicked'

