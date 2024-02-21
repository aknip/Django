import json
from loguru import logger
from nicegui import app, ui
from helper_functions import show


def app_settings(ui, settings_data):
    ui.label('Content of Settings')   
    ui.input('OpenAI-Key', on_change=show).bind_value(settings_data, 'OpenAI-Key')
    ui.input('Text input', on_change=show)
    more_settings_visible = ui.switch('More Settings', value=False, on_change=show)
    with ui.column().bind_visibility_from(more_settings_visible, 'value'):
        settings_as_Text = None
        #ui.button('Show all setttings', on_click=getSettingsAsText(settings_data, settings_as_Text))
        ui.button('Show all setttings', on_click = lambda: getSettingsAsText(settings_data, ui_settings_as_Text))
        ui_settings_as_Text = ui.textarea('Settings:')
        ui.button('Save setttings', on_click = lambda: saveSettings(settings_data))


def getSettingsAsText(settings_data, ui_settings_as_Text):
    ui_settings_as_Text.value = json.dumps(settings_data, sort_keys=False, indent=2)
    logger.info("Get settings clicked. Some more text to check the log length.")

def saveSettings(settings_data):
    f=open(settings_data["settings_file_path"],'w+')
    f.write(json.dumps(settings_data, sort_keys=False, indent=2))
    f.close()
    logger.info("Settings saved.")

