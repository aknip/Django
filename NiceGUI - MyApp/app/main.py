from nicegui import ui
from nicegui.events import ValueChangeEventArguments
import json
import os

if os.path.exists('/app/testfile.txt'):
    print('Config found')
    f= open('/app/testfile.txt','r')
    contents =f.read()
    print(contents)
    f.close()
else:
    print('Config not found')


settings_data = {
    'name': 'Bob', 
    'age': 17,
    'OpenAI-Key': 'sk-1234'}

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
    </style>
''')

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

def runCyberApp():
    cyber_result1.text = 'Lorem ipsum dolor sit amet,' + json.dumps(settings_data, sort_keys=False, indent=2)
    cyber_result2.value = 'Button was clicked'

def getSettingsAsText():
    settings_as_Text.value = json.dumps(settings_data, sort_keys=False, indent=2)

def saveSettings():
    f=open('/app/testfile.txt','w+')
    f.write(json.dumps(settings_data, sort_keys=False, indent=2))
    f.close()
    print('Save done.')


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
    ui.label('Side menu')
    debug_mode = ui.switch('Debug', value=True, on_change=show)
    with ui.column().bind_visibility_from(debug_mode, 'value'):
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





